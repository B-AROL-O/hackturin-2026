import {readFile,writeFile} from 'node:fs/promises';
// Extract only the authored explanatory layers; never alter canonical evidence.
const panel=await readFile('assets/panel-rgb.svg','utf8');
const plant=await readFile('assets/plant-owner.svg','utf8');
const base=panel.replace(/<g id="deposit"[\s\S]*?<\/g>/,'').replace('<rect width="1200" height="760" fill="#FFFFFF"/>','').trim().replace(/^<svg[^>]*>|<\/svg>$/g,'');
const deposit=panel.match(/<g id="deposit"[\s\S]*?<\/g>/)[0];
const owner=plant.match(/<g id="owner"[\s\S]*?<\/g>/)[0];
await writeFile('src/art.ts',`export const panelMarkup = ${JSON.stringify(base)};\nexport const depositMarkup = ${JSON.stringify(deposit)};\nexport const ownerMarkup = ${JSON.stringify(owner)};\n`);
