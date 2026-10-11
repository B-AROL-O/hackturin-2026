// Original restrained 120 BPM score, synthesized offline in Chromium.
// Purely tonal; no sampled music, random noise or third-party recordings.
import {openBrowser} from '@remotion/renderer';
import {readFile,writeFile} from 'node:fs/promises';
const cues=JSON.parse(await readFile('captions/en.json','utf8'));
const browser=await openBrowser('chrome');
try{
 const page=await browser.newPage({context:()=>null,logLevel:'error',indent:false,pageIndex:0,onBrowserLog:null,onLog:()=>{}});
 const samples=await page.evaluate(async(cues)=>{
  const sr=24000;const ctx=new OfflineAudioContext(1,sr*120,sr);
  const master=ctx.createGain();master.gain.value=.22;master.connect(ctx.destination);
  // A sparse, stable D / A / E harmonic bed. Half-second beat grid, long rests.
  function tone(t,d,f,a){const o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=f;o.connect(g);g.connect(master);g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(a,t+.025);g.gain.exponentialRampToValueAtTime(.00001,t+d);o.start(t);o.stop(t+d+.03);}
  for(let bar=0;bar<59;bar++){
   const t=bar*2;
   if(t>=85&&t<93)continue; // let the evidence breathe
   const f=[146.832,164.814,110,146.832][Math.floor(bar/4)%4];
   tone(t,1.8,f,.06);if(bar%2===0)tone(t+.5,.65,f*2,.075);
   if(bar%4===3&&t<112)tone(t+1.5,.4,440,.025);
  }
  for(const t of [12,30,50,75,100,114]){tone(t,2,293.665,.065);tone(t+.5,2,440,.04);}
  const a=(await ctx.startRendering()).getChannelData(0);
  for(let i=0;i<a.length;i++){const t=i/sr;let duck=1;for(const c of cues){if(t>=c.start-.12&&t<c.end+.22){duck=.32;break;}}a[i]*=duck*Math.min(1,t/1.2)*Math.max(0,Math.min(1,(119-t)/2));}
  // Transfer signed PCM, not a huge JSON float array.
  const b=new Uint8Array(a.length*2);const v=new DataView(b.buffer);for(let i=0;i<a.length;i++)v.setInt16(i*2,Math.round(Math.max(-1,Math.min(1,a[i]))*32767),true);
  let s='';for(let i=0;i<b.length;i+=32768)s+=String.fromCharCode(...b.subarray(i,i+32768));return btoa(s);
 },cues);
 const data=Buffer.from(samples,'base64'),header=Buffer.alloc(44);header.write('RIFF');header.writeUInt32LE(36+data.length,4);header.write('WAVEfmt ',8);header.writeUInt32LE(16,16);header.writeUInt16LE(1,20);header.writeUInt16LE(1,22);header.writeUInt32LE(24000,24);header.writeUInt32LE(48000,28);header.writeUInt16LE(2,32);header.writeUInt16LE(16,34);header.write('data',36);header.writeUInt32LE(data.length,40);await writeFile('audio/music.wav',Buffer.concat([header,data]));console.log('120 BPM OfflineAudioContext score rendered.');
}finally{await browser.close({silent:true});}
