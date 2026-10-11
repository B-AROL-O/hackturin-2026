import React from 'react';
import {AbsoluteFill,Audio,Composition,Sequence,staticFile,useCurrentFrame} from 'remotion';
import {loadFont} from '@remotion/fonts';
import timing from '../timing.json';
import cueData from '../captions/en.json';
const cues=cueData as {start:number;end:number;text:string}[];
import {scenes} from './scenes';
import {C,font} from './theme';
for(const [weight,file] of [['400','Regular'],['600','Semibold']]) loadFont({family:font,url:staticFile(`fonts/SourceSans3-${file}.otf`),weight});
export type FilmProps={captions:boolean;audioMode:'final'|'off';staticMode:boolean};
const Scene=({index,staticMode}:{index:number;staticMode:boolean})=>{const f=useCurrentFrame();const Component=scenes[index];return <Component f={f} staticMode={staticMode}/>};
export const Film=({captions,audioMode,staticMode}:FilmProps)=>{const f=useCurrentFrame();const cue=cues.find(c=>f/30>=c.start&&f/30<c.end);return <AbsoluteFill style={{background:C.white,color:C.blue,fontFamily:`"${font}"`}}>
{timing.scenes.map((s,i)=><Sequence style={{fontFamily:`"${font}"`,color:C.blue}} key={s.id} from={s.from} durationInFrames={s.durationInFrames}><Scene index={i} staticMode={staticMode}/></Sequence>)}
{audioMode==='final'&&<Audio src={staticFile('audio/narration.wav')}/>}
{captions&&cue&&<div style={{position:'absolute',bottom:66,left:180,right:180,display:'flex',justifyContent:'center'}}><div style={{background:C.blue,color:C.white,fontSize:50,lineHeight:1.12,fontWeight:400,textAlign:'center',whiteSpace:'pre-line',padding:'12px 34px'}}>{cue.text}</div></div>}
</AbsoluteFill>};
export const Root=()=> <Composition id={timing.compositionId} component={Film} durationInFrames={timing.durationInFrames} fps={timing.fps} width={timing.width} height={timing.height} defaultProps={{captions:false,audioMode:'final',staticMode:false}}/>;
