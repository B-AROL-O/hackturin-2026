"""Generate exact narration locally; phrase clips give sample-accurate captions.
Re-synthesizes overlong scenes at an adjusted model speed (no time stretching).
"""
from pathlib import Path
import json, re, textwrap, hashlib
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
P=Path(__file__).resolve().parents[1]
chunks=[
['Your solar plant is covered in shit.', 'Literally.', 'But how much is that affecting production?', 'That is the question behind PoopVolt.'],
['An older solar plant still works.', 'But its owner cannot tell whether it produces', 'as much as it should.', 'The maintenance company needs clear evidence', 'to explain why an inspection is worth considering.'],
['PoopVolt compares observed production', 'with an expected reference over the same period.', 'Today, we have a comparison between inverters.', 'A theoretical reference adjusted for environmental conditions', 'is the next step.', 'A deviation tells us where to investigate,', 'not what caused it.'],
['The prototype uses Arduino UNO Q', 'with temperature, humidity, light, a display, and NFC.', 'The schematic also shows the current sensor', 'between the panel and the charging system.', 'Zero current has been checked;', 'measurements under light still need validation.', 'The board runs on USB power,', 'separate from the solar branch.'],
["In a replay of SOLARMA’s historical data,", 'we compare thirteen inverters.', 'From August first to September seventeenth, twenty nineteen,', 'inverter one reports zero energy', 'against roughly two hundred and ninety-two kilowatt-hours', 'expected from its peers.', 'The software flags it for inspection.', 'This is historical replay,', 'not our panel’s measurement or a soiling diagnosis.'],
['The technician investigates and proposes', 'cleaning, repair, or replacement where needed.', 'The owner decides.', 'Afterward, comparable measurements must verify the benefit;', 'the full gap may not be recoverable.', 'PoopVolt turns a production gap', 'into an understandable intervention proposal.']]
source=json.loads((P/'audio/transcript.json').read_text())
for i,ss in enumerate(chunks):
    assert ' '.join(ss).replace('’',"'")==source[f'V0{i+1}']
model=Kokoro(str(P/'.voice-model/kokoro-v1.0.onnx'),str(P/'.voice-model/voices-v1.0.bin'))
sr=24000
starts=[0,12,30,50,75,100]; budgets=[11,17,19,24,24,16]
cues=[]; manifest=[]; mix=np.zeros(120*sr,dtype=np.float32)
for i,ss in enumerate(chunks):
    speed=[.78,.73,.96,.86,1.02,1.03][i]
    for attempt in range(5):
        clips=[]
        for j,txt in enumerate(ss):
            spoken=txt.replace('PoopVolt','Poop Volt').replace('UNO Q','oo-no cue').replace('NFC','N F C').replace('SOLARMA','So-lar-ma')
            a,rate=model.create(spoken,voice='af_heart',speed=speed,lang='en-us')
            assert rate==sr
            # retain 40 ms silence around the measured speech, not model trailing gaps
            idx=np.flatnonzero(abs(a)>.002)
            a=a[max(0,idx[0]-960):min(len(a),idx[-1]+960)]
            clips.append(a)
        lengths=[len(a)/sr for a in clips]
        # modest phrase breathing; speech never crosses a scene boundary
        total=sum(lengths)+.12*(len(clips)-1)
        print(f'V0{i+1} attempt {attempt+1}: {total:.2f}s / {budgets[i]}s speed {speed:.3f}',flush=True)
        if total<=budgets[i]: break
        speed*=total/budgets[i]*1.015
    assert total<=budgets[i], 'Re-record window exceeded'
    # Spread spare room between phrases. Keep deadpan Literally pause.
    gap=min(.45,.12+(budgets[i]-total)/(len(clips)-1))
    if i==0: gap=min(.6,gap)
    offset=.5; local=np.zeros(int((budgets[i]+1)*sr),dtype=np.float32)
    for j,(txt,a) in enumerate(zip(ss,clips)):
        start=starts[i]+offset; end=start+len(a)/sr
        n=round(offset*sr); local[n:n+len(a)]=a
        cue_end=min(end+min(gap,.20), starts[i]+budgets[i]+.5)
        lines=textwrap.wrap(txt.replace('’',"'"),width=42,break_long_words=False)
        assert len(lines)<=2
        cues.append(dict(scene=f'V0{i+1}',start=round(start,4),end=round(cue_end,4),text='\n'.join(lines),speechEnd=round(end,4)))
        offset+=len(a)/sr+gap
    final_end=offset-gap
    take=local[:round((final_end+.15)*sr)]
    sf.write(P/f'audio/V0{i+1}.wav',take,sr,subtype='PCM_24')
    n=starts[i]*sr; mix[n:n+len(take)]+=take
    manifest.append(dict(scene=f'V0{i+1}',voice='af_heart',speed=speed,speechEnd=round(starts[i]+final_end,4),sampleRate=sr))
# Final voice normalization is done by FFmpeg, not per clip.
sf.write(P/'audio/narration-raw.wav',mix,sr,subtype='PCM_24')
(P/'captions/en.json').write_text(json.dumps(cues,indent=2)+'\n')
(P/'audio/takes.json').write_text(json.dumps(manifest,indent=2)+'\n')
def tc(t):
    ms=round(t*1000); return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(P/'captions/poopvolt-120-en.srt').write_text('\n\n'.join(f'{i+1}\n{tc(c["start"])} --> {tc(c["end"])}\n{c["text"]}' for i,c in enumerate(cues))+'\n')
