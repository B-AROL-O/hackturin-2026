import React from 'react';
import {Box,Text,Header,Footer,Logo,Panel,Pic,Person,Flag,Schematic,Arrow} from './components';
import {C} from './theme';
import {expo,damp,mix} from './motion';
type Props={f:number;staticMode?:boolean};
// Complete, settled layouts are reviewed with staticMode before motion rendering.
export function V01({f,staticMode}:Props){if(staticMode)f=170;const q=expo(f,120,30),logo=expo(f,210,24)*(1-expo(f,351,9)),bird=damp(f,0,35);return <>
<Header n="01" label="A QUESTION WORTH ASKING"/>
<svg width="0" height="0"><defs><filter id="lateral-blur" x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur stdDeviation={`${Math.min(2.4,Math.abs(damp(f,0,35)-damp(f-.5,0,35))*690*.16)} 0`}/></filter></defs></svg>
<Panel x={mix(690,70,q)} y={mix(178,265,q)} w={mix(1120,600,q)} deposit={expo(f,66,8)}/>
{/* Mirrored to face its direction of travel; it lands on the frame's top edge above the deposit. */}
<Box x={mix(1960,1270,bird)-q*490} y={95-q*140} w={240} style={{opacity:expo(f,0,8)*(1-q)}}><Pic name="pigeon.svg" style={{width:240,transform:'scaleX(-1)',filter:'url(#lateral-blur)'}}/></Box>
<Text x={96} y={202} w={680} size={88} weight={600} style={{opacity:1-q}}>Your solar plant.</Text>
<Text x={96} y={407} w={630} size={108} weight={600} style={{opacity:expo(f,48,12)*(1-q)}}>Covered in<br/>shit.</Text>
<Text x={96} y={660} w={600} size={52} style={{opacity:expo(f,91,8)*(1-q)}}>Literally.</Text>
<Text x={760} y={270} w={970} size={88} weight={600} style={{opacity:q*(1-logo),transform:`translateX(${32*(1-q)}px)`}}>How much is it<br/>affecting production?</Text>
<Box x={760} y={520} w={mix(0,220,q)} h={8} style={{background:C.yellow,opacity:1-logo}}/>
<Logo x={720} y={177} w={1080} opacity={logo}/>
<Text x={800} y={674} w={910} size={39} style={{opacity:logo}}>How much is it affecting production?</Text>
<Footer status="Illustrative scene" source="PoopVolt · Suncheckers"/>
</>}
export function V02({f,staticMode}:Props){if(staticMode)f=480;const plant=damp(f,0,90),roles=expo(f,150,24),line=expo(f,300,24),question=expo(f,45,30);return <>
<Header n="02" label="THE OWNER’S QUESTION"/>
{/* The original panel stays the same object; its cells become the installation. */}
<Panel x={mix(70,420,plant)} y={mix(265,341,plant)} w={mix(600,720,plant)}/>
<svg width="1920" height="1080" style={{position:'absolute',opacity:plant}}><path d="M1070 557L1190 461L1310 557V721H1070Z" fill={C.light}/><path d="M1056 555L1190 450L1324 555" stroke={C.blue} strokeWidth="8" fill="none"/><rect x="1215" y="620" width="48" height="101" fill={C.line}/><path d="M520 747H1320" stroke={C.line} strokeWidth="2"/></svg>
<Box x={420} y={160} w={1080} h={175} style={{border:`2px solid ${C.line}`,opacity:question}}/>
<Text x={450} y={181} w={1020} size={67} weight={600} style={{textAlign:'center',opacity:question}}>It works. But is it<br/>performing as expected?</Text>
<Person x={203-32*(1-roles)} y={430} tech opacity={roles}/><Person x={1515+32*(1-roles)} y={430} opacity={roles}/>
<Text x={113} y={716} w={360} size={35} weight={600} style={{opacity:roles,textAlign:'center'}}>Maintenance company<br/>/ technician</Text>
<Text x={1460} y={716} w={300} size={35} weight={600} style={{opacity:roles,textAlign:'center'}}>Owner</Text>
<svg width="1920" height="1080" style={{position:'absolute',opacity:line}}><path d="M1575 411V368H294V411" fill="none" stroke={C.blue} strokeWidth="2" strokeDasharray={1600} strokeDashoffset={1600*(1-line)}/><circle cx="294" cy="411" r="7" fill={C.yellow}/><circle cx="1575" cy="411" r="7" fill={C.yellow}/></svg>
<Footer status="Illustrative owner scenario" source="Narrative · Proposed users"/>
</>}
export function V03({f,staticMode}:Props){if(staticMode)f=570;const frame=damp(f,0,30),obs=expo(f,15,18),exp=expo(f,30,18),peer=expo(f,150,24),future=expo(f,330,24),flag=expo(f,480,18);return <>
<Header n="03" label="MAKE THE GAP UNDERSTANDABLE"/>
<Box x={mix(420,96,frame)} y={160} w={mix(1080,1728,frame)} h={mix(175,565,frame)} style={{border:`2px solid ${C.line}`}}/>
<Text x={150} y={205} w={700} size={88} weight={600} style={{opacity:obs,transform:`translateX(${24*(1-obs)}px)`}}>Observed</Text>
<Text x={1060} y={205} w={700} size={88} weight={600} color={C.grey} style={{opacity:exp,transform:`translateX(${24*(1-exp)}px)`}}>Expected</Text>
<Box x={152} y={314} w={650*obs} h={5} style={{background:C.blue}}/><Box x={1064} y={314} w={650*exp} h={5} style={{borderTop:`4px dashed ${C.grey}`}}/>
<Text x={831} y={258} w={234} size={31} weight={600} style={{textAlign:'center',opacity:frame}}>Same period</Text>
<Box x={150} y={368} w={780} style={{opacity:peer}}><Text x={0} y={0} w={760} size={39} weight={600}>Peer comparison: available</Text><svg width="690" height="118" style={{marginTop:70}}>{[0,1,2,3].map(i=><g key={i} transform={`translate(${i*167} 0)`}><rect width="130" height="94" fill={C.light} stroke={C.line} strokeWidth="2"/><rect x="18" y="18" width="94" height="36" fill="none" stroke={C.grey} strokeWidth="2"/><path d="M24 73h82" stroke={C.blue} strokeWidth="3"/></g>)}</svg><Text x={0} y={185} w={750} size={30} color={C.grey}>Peer inverters · a shared reference</Text></Box>
<Box x={1060} y={364} w={708} h={235} style={{border:`2px dashed ${C.grey}`,opacity:future,padding:28}}><div style={{fontSize:39,lineHeight:1.18}}>Environmental theoretical<br/>reference: <b style={{fontWeight:600}}>future work</b></div><div style={{width:72,height:4,background:C.line,marginTop:29}}/></Box>
<Box x={130} y={637} w={1635} h={84} style={{opacity:flag}}><Text x={18} y={8} size={52} weight={600} w={850}>Deviation → Investigate</Text><Text x={946} y={14} size={37} w={690}>A flag is not a diagnosis</Text><Box x={18} y={74} w={598*flag} h={7} style={{background:C.yellow}}/></Box>
<Footer status="Comparison method · theoretical reference remains future work" source="Peer-comparison documentation"/>
</>}
const full:[number,number,number,number]=[0,0,419.989,297.0022];
// Schematic crops [x,y,w,h] in sheet millimetres, one per narration phrase:
// full sheet · I2C · UART+A0/A1 · current sensor in series · Waveshare charger · A1 sensor · full sheet.
const targets:[number,number,number,number][]=[full,[128,33,145,61],[128,93,145,62],[216,155,160,48],[313,77,92,49],[125,154,197,32],full];
const starts=[0,100,170,239,330,422,585];
// Viewport size per phase: the photo strip shares the row in phases 0 and 3–5.
const boxes:[number,number][]=[[1180,570],[1728,470],[1728,470],[1180,470],[1180,470],[1180,470],[1270,570]];
const headlines=['','I2C → AHT20 / LCD','UART → NFC · A0 → Light · A1 → Current sensor','Panel → Current sensor → Waveshare → LiPo','Panel → Current sensor → Waveshare → LiPo','A1 · Current: zero checked; under-light measurement pending'];
const sublines=['','Canonical schematic · original symbols, nets and connection context','UNO Q: USB-powered · original symbols, nets and connection context','Current sensor in series on the panel + wire','Waveshare USB OUT: unconnected','Solar branch separate from the UNO Q USB supply'];
// Zoom moves the centre linearly and the size geometrically, so apparent speed stays even.
const zoom=(a:typeof full,b:typeof full,t:number)=>{const w=Math.exp(mix(Math.log(a[2]),Math.log(b[2]),t)),h=Math.exp(mix(Math.log(a[3]),Math.log(b[3]),t));return [mix(a[0]+a[2]/2,b[0]+b[2]/2,t)-w/2,mix(a[1]+a[3]/2,b[1]+b[3]/2,t)-h/2,w,h] as typeof full;};
export function V04({f,staticMode}:Props){if(staticMode)f=290;let phase=0;while(phase<6&&f>=starts[phase+1])phase++;const t=phase===0?1:damp(f,starts[phase],30),prev=Math.max(0,phase-1);
const crop=zoom(targets[prev],targets[phase],t),bw=mix(boxes[prev][0],boxes[phase][0],t),bh=mix(boxes[prev][1],boxes[phase][1],t);
// Photos leave before the viewport grows over them and arrive after it has made room.
const leave=1-expo(f,starts[phase],8),arrive=expo(f,starts[phase]+18,12);
const outdoor=(n:number)=>n>=3&&n<=5?1:0,bench=phase===0?1:phase===1?leave:0,field=outdoor(phase)?(outdoor(prev)?1:arrive):outdoor(prev)?leave:0,lab=phase===0?1:expo(f,starts[phase]+6,14);
return <><Header n="04" label="THE PROTOTYPE"/><Text y={108} size={58} weight={600}>Prototype electrical schematic</Text>
<Schematic crop={crop} w={bw} h={bh} y={193}/>
{bench>0&&<Box x={1320} y={193} w={504} h={378} style={{overflow:'hidden',opacity:bench}}>
<Pic name="prototype-bench-01.jpg" style={{position:'absolute',width:504,height:378,objectFit:'cover'}}/>
{/* The second bench photo is a closer view of the display and Grove shield. */}
<Pic name="prototype-bench-02.jpg" style={{position:'absolute',width:504,height:378,objectFit:'cover',opacity:expo(f,52,9),transform:'scale(1.5)',transformOrigin:'58% 18%'}}/></Box>}
{bench>0&&<><Text x={1320} y={588} w={504} size={29} color={C.grey} style={{opacity:bench}}>Prototype photo</Text><Text x={1320} y={636} w={504} size={32} weight={600} style={{opacity:bench}}>UNO Q: USB-powered</Text></>}
{field>0&&<><Pic name="prototype-outdoor.jpg" style={{position:'absolute',left:1396,top:193,width:352,height:470,objectFit:'cover',opacity:field}}/><Text x={1320} y={678} w={504} size={29} color={C.grey} style={{opacity:field}}>Prototype setup photo · USB connected</Text></>}
{phase>0&&phase<6&&<>
<Text x={96} y={691} w={outdoor(phase)?1130:1728} size={phase>=3?34:42} weight={600} style={{opacity:lab}}>{headlines[phase]}</Text>
<Text x={96} y={750} w={outdoor(phase)?1150:1700} size={30} color={C.grey} style={{opacity:lab}}>{sublines[phase]}</Text>
</>}
{phase===6&&<Box x={1420} y={255} w={400} style={{opacity:lab}}><div style={{fontSize:43,fontWeight:600,lineHeight:1.16}}>UNO Q:<br/>USB-powered</div><div style={{width:90,height:6,background:C.yellow,margin:'38px 0'}}/><div style={{fontSize:34,lineHeight:1.25}}>Current: zero checked;<br/>under-light measurement pending</div><div style={{fontSize:29,marginTop:32,color:C.grey}}>Waveshare USB OUT:<br/>unconnected</div></Box>}
<Footer status="Prototype / reported bring-up" source="KiCad · hardware connection record"/></>}
export function V05({f,staticMode}:Props){if(staticMode)f=420;const nums=expo(f,150,24),flag=expo(f,540,18);return <>
<Header n="05" label="HISTORICAL REPLAY · SOLARMA · 13 INVERTERS"/>
<Text y={111} size={46} weight={600}>1 Aug–17 Sep 2019 · Inverter 1</Text>
{/* The entire original figure is visible from the hard cut; no path rewriting. */}
<Pic name="comparison-inverter-1-replayed.png" style={{position:'absolute',left:96,top:205,width:1250,height:1250*340/760}}/>
<Box x={1410} y={215} w={414} style={{opacity:nums}}><div style={{fontSize:31,color:C.grey}}>Observed:</div><div style={{fontSize:78,fontWeight:600,lineHeight:1.1,marginTop:8}}>0 kWh</div><div style={{height:2,background:C.line,margin:'28px 0'}}/><div style={{fontSize:31,color:C.grey}}>Expected from peers:</div><div style={{fontSize:73,fontWeight:600,lineHeight:1.1,marginTop:10}}>≈292 kWh</div></Box>
{/* External outline around the chart's own evaluation window; the chart itself stays untouched. */}
<Box x={636} y={292} w={686} h={402} style={{border:`3px solid ${C.yellow}`,opacity:flag}}/>
<Flag x={1380} y={624} w={444} opacity={flag}/>
<Footer status="Historical data · cause unconfirmed · benefit unmeasured" source="SOLARMA · comparison-results.md"/>
</>}
export function V06({f,staticMode}:Props){if(staticMode)f=300;const enter=damp(f,0,30),steps=expo(f,45,24),options=expo(f,85,24),owner=expo(f,165,18),verify=expo(f,205,18),close=damp(f,420,60);const workflow=1-close;
const stepAt=[[96,272],[430,203],[694,182],[937,208]],stepT=[0,89,166,204];let k=0;while(k<3&&f>=stepT[k+1])k++;const sp=k===0?1:expo(f,stepT[k],14),stepX=mix(stepAt[Math.max(0,k-1)][0],stepAt[k][0],sp),stepW=mix(stepAt[Math.max(0,k-1)][1],stepAt[k][1],sp);return <>
<Box style={{opacity:workflow}} w={1920} h={1080}><Header n="06" label="EVIDENCE BECOMES A HUMAN DECISION"/>
{/* Inspection flag continues at its previous position, then joins the technician. */}
<Flag x={mix(1380,96,enter)} y={mix(624,172,enter)} w={mix(444,550,enter)}/>
<Person x={203} y={383} tech opacity={enter}/><Person x={1515} y={383} opacity={enter}/>
<Text x={96} y={635} w={445} size={33} weight={600} style={{opacity:enter,textAlign:'center'}}>Maintenance company<br/>/ technician</Text><Text x={1450} y={635} w={310} size={33} weight={600} style={{opacity:enter,textAlign:'center'}}>Owner</Text>
<Text x={96} y={290} size={58} weight={600} style={{opacity:steps}}>Investigate → Propose → Choose → Measure</Text>
{/* The underline follows the spoken step. */}
<Box x={stepX} y={358} w={stepW} h={6} style={{background:C.yellow,opacity:steps}}/>
<Box x={575} y={398} w={750} h={258} style={{opacity:options*(1-verify),border:`2px solid ${C.line}`,padding:31}}><div style={{fontSize:32,color:C.grey,marginBottom:24}}>Technician-proposed options</div><div style={{fontSize:47,fontWeight:600,lineHeight:1.25}}>Cleaning · Repair<br/>Replacement</div></Box>
<Arrow x={1348} y={512} w={116} opacity={owner*(1-verify)}/>
<Text x={1400} y={717} w={425} size={35} weight={600} style={{opacity:owner*(1-verify),textAlign:'center'}}>The owner chooses</Text>
<Box x={575} y={398} w={750} h={258} style={{opacity:verify,border:`2px dashed ${C.grey}`,padding:31,background:C.white}}><div style={{fontSize:48,fontWeight:600}}>Verify benefit</div><div style={{fontSize:33,color:C.grey,marginTop:24}}>Comparable measurements</div><div style={{fontSize:32,color:C.grey,marginTop:13}}>—  After intervention  —</div></Box>
<Footer status="Proposed workflow · field benefit unmeasured" source="Maintenance architecture"/>
</Box>
{/* The review rectangle expands into the white title stage. No logo internals move. */}
{close>0&&<><Box x={mix(575,0,close)} y={mix(398,0,close)} w={mix(750,1920,close)} h={mix(258,1080,close)} style={{background:C.white,opacity:close}}/><Logo x={420} y={mix(215,165,close)} w={1080} opacity={close}/><Text y={680} size={49} weight={600} style={{textAlign:'center',opacity:close}}>Evidence for photovoltaic maintenance</Text><Text y={767} size={34} color={C.grey} style={{textAlign:'center',opacity:close}}>Suncheckers · hackTurin 2026</Text></>}
</>}
export const scenes=[V01,V02,V03,V04,V05,V06];
