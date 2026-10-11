import {readFile,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const json=async p=>JSON.parse(await readFile(p,'utf8'));
const t=await json('timing.json');let next=0;
assert.equal(t.durationInFrames,3600);assert.equal(t.fps,30);
for(const s of t.scenes){assert.equal(s.from,next);next+=s.durationInFrames;}
assert.equal(next,3600);
const source=await json('../sources/manifest.json');
const sourceText=JSON.stringify(source);for(const s of t.scenes)for(const id of s.sourceIds)assert(sourceText.includes('"'+id+'"'),'Missing source '+id);
const am=await json('assets/manifest.json');for(const a of am.assets){assert.equal(createHash('sha256').update(await readFile('assets/'+a.path)).digest('hex'),a.sha256);}
const script=await readFile('storyboard.md','utf8');const narration=await json('audio/transcript.json');
for(const txt of Object.values(narration)) assert(script.replace(/\n> /g,' ').includes(txt));
const cues=await json('captions/en.json');assert(cues.length>0);let end=0;let fastest=0;
for(const c of cues){assert(c.start>=end);assert(c.end>c.start);assert(c.end<=117);assert(c.text.split('\n').length<=2);assert(c.text.split('\n').every(x=>x.length<=42));const scene=t.scenes.find(s=>s.id===c.scene);assert(c.start>=scene.from/30);assert(c.end<=(scene.from+scene.durationInFrames)/30);end=c.end;fastest=Math.max(fastest,c.text.replace(/\n/g,' ').length/(c.end-c.start));}
for(const s of t.scenes){assert.equal(cues.filter(c=>c.scene===s.id).map(c=>c.text.replace(/\n/g,' ')).join(' '),narration[s.id]);}
for(const f of ['fonts/SourceSans3-Regular.otf','fonts/SourceSans3-Semibold.otf','fonts/LICENSE.md','audio/narration.wav'])assert((await stat(f)).size>1000);
console.log('PASS: 3600 contiguous frames; original asset hashes; source IDs; exact narration/captions; scene windows; local fonts and audio.');
console.log('Maximum caption characters/second:',fastest.toFixed(2));
