import {bundle} from '@remotion/bundler';
import {selectComposition,renderStill,renderMedia,openBrowser} from '@remotion/renderer';
import {mkdir,copyFile,readFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import './prepare.mjs';
const mode=process.argv[2]??'stills';
const inputProps={captions:mode==='captioned'||mode==='beats'||mode==='determinism',audioMode:mode==='stills'||mode==='beats'||mode==='determinism'?'off':'final',staticMode:mode==='stills'};
await mkdir('out/review',{recursive:true});
const serveUrl=await bundle({entryPoint:'src/index.ts'});
const browser=await openBrowser('chrome');
const composition=await selectComposition({serveUrl,id:'PoopVoltPitch120',inputProps,puppeteerInstance:browser});
try {
if(mode==='stills'||mode==='beats'||mode==='determinism'){
 let frames=mode==='stills'?[170,840,1470,1790,2700,3330]:[0,30,65,120,200,250,359,360,405,510,660,810,899,900,945,1080,1260,1410,1499,1500,1574,1575,1649,1680,1780,1890,1979,1980,2030,2120,2200,2249,2250,2400,2549,2550,2670,2789,2790,2820,2940,2999,3000,3030,3180,3330,3420,3465,3510,3599];
 if(mode==='beats'){const beatMap=JSON.parse(await readFile('beat-map.json','utf8'));const t=JSON.parse(await readFile('timing.json','utf8'));frames=[...new Set([...frames,...beatMap.beats.map(b=>b.frame),...t.scenes.flatMap(s=>[s.from-1,s.from,s.from+1])])].filter(f=>f>=0&&f<3600).sort((a,b)=>a-b);}
 if(mode==='determinism')frames=[3599,2670,0,2670,3599];
 let index=0;
 for(const frame of frames){await renderStill({serveUrl,composition,inputProps,frame,output:`out/review/${mode}-${String(frame).padStart(4,'0')}${mode==='determinism'?'-'+index++:''}.png`,puppeteerInstance:browser,logLevel:'error'});console.log('Reviewed frame rendered',frame);}
 if(mode==='beats'){await copyFile('out/review/beats-3599.png','out/poster.png');}
} else {
 const name=`poopvolt-120-en${mode==='captioned'?'-captioned':''}.mp4`;
 await renderMedia({serveUrl,composition,inputProps,codec:'h264',outputLocation:'out/'+name,crf:17,pixelFormat:'yuv420p',concurrency:4,imageFormat:'png',puppeteerInstance:browser,audioCodec:'aac',audioBitrate:'192k',onProgress:({progress})=>{if(Math.floor(progress*100)%10===0)process.stdout.write(`\r${name} ${Math.floor(progress*100)}%`);}});
 console.log('\nCompleted',name);
}
}finally{await browser.close({silent:true});}
