import {mkdir,cp,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const manifest=JSON.parse(await readFile('assets/manifest.json','utf8'));
for(const a of manifest.assets){const b=await readFile('assets/'+a.path);if(createHash('sha256').update(b).digest('hex')!==a.sha256)throw Error('Asset changed: '+a.path);}
await mkdir('public',{recursive:true});
for(const name of ['assets','fonts','audio']) await cp(name,'public/'+name,{recursive:true});
console.log('Local assets staged; supplied hashes verified.');
