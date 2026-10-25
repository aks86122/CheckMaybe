// PIL-compatible bicubic resize (antialiased), so browser scores match the Python evaluation.
// src: RGBA bytes from getImageData; returns RGB floats 0-255, N x N.
function cub(x){x=Math.abs(x);const a=-0.5;return x<1?((a+2)*x-(a+3))*x*x+1:x<2?(((x-5)*x+8)*x-4)*a:0}
function coeffs(inS,outS){const sc=inS/outS,fs=Math.max(sc,1),sup=2*fs,W=[];
 for(let i=0;i<outS;i++){const ctr=(i+0.5)*sc;let x0=Math.max(0,Math.floor(ctr-sup+0.5)),x1=Math.min(inS,Math.floor(ctr+sup+0.5));const w=[];let t=0;
  for(let x=x0;x<x1;x++){const v=cub((x-ctr+0.5)/fs);w.push(v);t+=v}W.push([x0,w.map(v=>v/t)])}return W}
function resize(src,w,h,N){const H=coeffs(w,N),V=coeffs(h,N),tmp=new Float32Array(N*h*3),out=new Float32Array(N*N*3);
 for(let y=0;y<h;y++)for(let i=0;i<N;i++){const[x0,ws]=H[i];let r=0,g=0,b=0;for(let k=0;k<ws.length;k++){const p=(y*w+x0+k)*4;r+=src[p]*ws[k];g+=src[p+1]*ws[k];b+=src[p+2]*ws[k]}
  const q=(y*N+i)*3;tmp[q]=Math.min(255,Math.max(0,Math.round(r)));tmp[q+1]=Math.min(255,Math.max(0,Math.round(g)));tmp[q+2]=Math.min(255,Math.max(0,Math.round(b)))}
 for(let j=0;j<N;j++){const[y0,ws]=V[j];for(let i=0;i<N;i++){let r=0,g=0,b=0;for(let k=0;k<ws.length;k++){const q=((y0+k)*N+i)*3;r+=tmp[q]*ws[k];g+=tmp[q+1]*ws[k];b+=tmp[q+2]*ws[k]}
  const o=(j*N+i)*3;out[o]=Math.min(255,Math.max(0,Math.round(r)));out[o+1]=Math.min(255,Math.max(0,Math.round(g)));out[o+2]=Math.min(255,Math.max(0,Math.round(b)))}}return out}
