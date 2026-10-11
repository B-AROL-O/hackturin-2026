from pathlib import Path
import json,textwrap
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
P=Path(__file__).resolve().parents[1];sr=24000
m=Kokoro(str(P/'.voice-model/kokoro-v1.0.onnx'),str(P/'.voice-model/voices-v1.0.bin'))
texts=['Your solar plant is covered in shit.','Literally.','But how much is that affecting production?','That is the question behind PoopVolt.']
starts=[.5,3.05,4.5,8.25];speeds=[.92,.92,.81,.84]
cues=[];take=np.zeros(12*sr,dtype=np.float32)
for j,(txt,start,speed) in enumerate(zip(texts,starts,speeds)):
 a,_=m.create(txt.replace('PoopVolt','Poop Volt'),voice='af_heart',speed=speed,lang='en-us');idx=np.flatnonzero(abs(a)>.002);a=a[max(0,idx[0]-960):min(len(a),idx[-1]+960)];end=start+len(a)/sr;assert end<(starts[j+1] if j<3 else 11.5),(txt,end)
 n=round(start*sr);take[n:n+len(a)]=a;cues.append(dict(scene='V01',start=start,end=min(end+.2,starts[j+1] if j<3 else 11.5),text='\n'.join(textwrap.wrap(txt,42)),speechEnd=end));print(txt,start,end,flush=True)
sf.write(P/'audio/V01.wav',take,sr,subtype='PCM_24')
old=json.loads((P/'captions/en.json').read_text());cues+=old[4:]
(P/'captions/en.json').write_text(json.dumps(cues,indent=2)+'\n')
mix=np.zeros(120*sr,dtype=np.float32)
for i,start in enumerate([0,12,30,50,75,100]):
 a,r=sf.read(P/f'audio/V0{i+1}.wav');mix[start*sr:start*sr+len(a)]=a
sf.write(P/'audio/narration-raw.wav',mix,sr,subtype='PCM_24')
takes=json.loads((P/'audio/takes.json').read_text());takes[0]['speed']=speeds;takes[0]['speechEnd']=cues[3]['speechEnd'];(P/'audio/takes.json').write_text(json.dumps(takes,indent=2)+'\n')
def tc(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(P/'captions/poopvolt-120-en.srt').write_text('\n\n'.join(f'{i+1}\n{tc(c["start"])} --> {tc(c["end"])}\n{c["text"]}' for i,c in enumerate(cues))+'\n')
