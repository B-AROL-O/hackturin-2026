"""Verify media metadata, decode integrity, still holds and mix loudness."""
import subprocess,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def run(args):return subprocess.check_output(args,text=True)
results={}
for name in ['poopvolt-120-en.mp4','poopvolt-120-en-captioned.mp4']:
 f=P/'out'/name
 meta=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]))
 v=next(x for x in meta['streams'] if x['codec_type']=='video');a=next(x for x in meta['streams'] if x['codec_type']=='audio')
 assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',3600)
 assert abs(float(meta['format']['duration'])-120)<.01
 subprocess.run(['ffmpeg','-v','error','-i',str(f),'-f','null','-'],check=True)
 # Quantization may vary slightly between compressed frames. Test max pixel error.
 import numpy as np
 def block(start,duration,crop):
  b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(start),'-i',str(f),'-t',str(duration),'-vf',crop+',format=gray','-f','rawvideo','-'])
  return np.frombuffer(b,dtype=np.uint8)
 # Final composition including captions must stay still for every final frame.
 last=block(117,3,'scale=480:270').reshape((-1,270,480)).astype(np.int16)
 err=float(np.max(np.mean(abs(last-last[0]),axis=(1,2))));assert len(last)==90;assert err<.5,err
 # Exact chart region from 85–93; captions are outside the evidence region.
 hold=block(85,8,'crop=1250:560:96:205,scale=625:280').reshape((-1,280,625)).astype(np.int16)
 err2=float(np.max(np.mean(abs(hold-hold[0]),axis=(1,2))));assert len(hold)==240;assert err2<.5,err2
 r=subprocess.run(['ffmpeg','-hide_banner','-i',str(f),'-af','loudnorm=I=-16:TP=-1:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
 audio=json.loads(r.stderr[r.stderr.index('{'):r.stderr.index('}')+1]);assert float(audio['input_tp'])<0
 results[name]={'duration':meta['format']['duration'],'frames':v['nb_frames'],'frameRate':v['r_frame_rate'],'size':[v['width'],v['height']],'videoCodec':v['codec_name'],'audioCodec':a['codec_name'],'loudness':audio['input_i'],'truePeak':audio['input_tp'],'closing90FramesMaxMeanPixelDifference':err,'replay240FramesMaxMeanPixelDifference':err2,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
 print(name,results[name],flush=True)
(P/'out/verification.json').write_text(json.dumps(results,indent=2)+'\n')
