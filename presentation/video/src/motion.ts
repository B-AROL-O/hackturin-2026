// Analytic, seek-safe curves. No accumulated spring state.
export const clamp=(v:number)=>Math.max(0,Math.min(1,v));
export const mix=(a:number,b:number,p:number)=>a+(b-a)*p;
export const expo=(f:number,start:number,duration=18)=>{const t=clamp((f-start)/duration);return t===0?0:t===1?1:(1-Math.pow(2,-8*t))/(1-1/256);};
// Unit critically damped response, normalized to settle exactly at its endpoint.
export const damp=(f:number,start:number,duration=30)=>{const t=clamp((f-start)/duration),k=8;return (1-(1+k*t)*Math.exp(-k*t))/(1-(1+k)*Math.exp(-k));};
export const range=(f:number,a:number,b:number)=>clamp((f-a)/(b-a));
