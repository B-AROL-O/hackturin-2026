// Caption display text: written numerals, typographic apostrophes, phrase-aware breaks.
// Cue timing stays as voice.py aligned it. Run after voice.py or retake-hook.py:
//   node scripts/captions.mjs
import {readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
// Spoken form (exact narration) → written caption form. Each phrase sits inside one cue.
const WRITTEN=[
 ['From August first to September seventeenth, twenty nineteen,','From 1 August to 17 September 2019,'],
 ['thirteen inverters','13 inverters'],
 ['inverter one','inverter 1'],
 ['two hundred and ninety-two kilowatt-hours','292 kWh'],
 ["'",'’'],
];
export const written=text=>WRITTEN.reduce((t,[spoken,shown])=>t.split(spoken).join(shown),text);
const MAX=42;
const WEAK=new Set(['a','an','the','of','to','for','with','and','or','between','from','in','on','at','is','its','our','be','must','need','not']);
const OPENS=new Set(['a','an','the','to','for','with','or','whether','where','into','between','over']);
// Two balanced lines; prefer breaks after punctuation, never strand one word or end on a weak word.
export const wrap=text=>{
 if(text.length<=MAX)return text;
 let best=null;
 for(let i=text.indexOf(' ');i>0;i=text.indexOf(' ',i+1)){
  const a=text.slice(0,i),b=text.slice(i+1);
  if(a.length>MAX||b.length>MAX)continue;
  const last=a.split(' ').pop().toLowerCase();
  let score=Math.abs(a.length-b.length);
  if(/[,;:]$/.test(a))score-=15;
  if(WEAK.has(last))score+=20;
  if(OPENS.has(b.split(' ')[0].toLowerCase()))score-=4;
  if(!b.includes(' ')||!a.includes(' '))score+=100;
  if(!best||score<best.score)best={score,text:a+'\n'+b};
 }
 if(!best)throw Error('Caption cannot fit two lines: '+text);
 return best.text;
};
// Half-even millisecond rounding, matching Python's round() in voice.py.
const roundEven=x=>{const f=Math.floor(x),d=x-f;return d>.5?f+1:d<.5?f:f%2?f+1:f;};
const tc=t=>{const ms=roundEven(t*1000);return `${String(Math.floor(ms/3600000)).padStart(2,'0')}:${String(Math.floor(ms/60000)%60).padStart(2,'0')}:${String(Math.floor(ms/1000)%60).padStart(2,'0')},${String(ms%1000).padStart(3,'0')}`;};
if(process.argv[1]===fileURLToPath(import.meta.url)){
 const cues=JSON.parse(await readFile('captions/en.json','utf8'));
 for(const c of cues)c.text=wrap(written(c.text.replace(/\n/g,' ')));
 await writeFile('captions/en.json',JSON.stringify(cues,null,2)+'\n');
 await writeFile('captions/poopvolt-120-en.srt',cues.map((c,i)=>`${i+1}\n${tc(c.start)} --> ${tc(c.end)}\n${c.text}`).join('\n\n')+'\n');
 for(const c of cues)console.log(c.scene,(c.text.replace(/\n/g,' ').length/(c.end-c.start)).toFixed(1).padStart(5),JSON.stringify(c.text));
}
