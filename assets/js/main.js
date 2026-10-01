/* Gen ZEE AI — Neural Ascent header: Three.js (logo + neural network) + GSAP */
(function(){
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const bg=$('.burger'),mn=$('.menu');
if(bg)bg.addEventListener('click',()=>{const o=mn.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
/* navbar: dark over hero, light after; hide on scroll down */
const nav=$('.nav'),hero=$('.hero');let ly=0;
function navState(){const y=scrollY,lim=hero?hero.offsetHeight-90:0;nav.classList.toggle('dk',y<lim);
 ly=y}
addEventListener('scroll',navState,{passive:true});navState();
const f=$('#cform');if(f)f.addEventListener('submit',e=>{e.preventDefault();$('.ok').style.display='block';f.reset()});
/* AI prompt typewriter */
const ask=$('.ask');
if(ask){const Q=$('.q',ask),A=$('.a',ask);
 const D=[["Which AI track fits me?","Start with Machine Learning, then specialise in LLM or Computer Vision."],["Can my team hire validated AI talent?","Yes. Role matching, pay on placement."],["How fast can I become job-ready?","Close your skills gap in 90 days with mentor-reviewed projects."]];
 if(reduce){Q.textContent='> '+D[0][0];A.textContent=D[0][1]}else{
 const type=(el,s,sp)=>new Promise(r=>{el.textContent='';el.classList.add('on');let i=0;const id=setInterval(()=>{el.textContent=s.slice(0,++i);if(i>=s.length){clearInterval(id);el.classList.remove('on');r()}},sp)});
 const w=ms=>new Promise(r=>setTimeout(r,ms));
 (async()=>{let i=0;await w(1500);for(;;){const[q,a]=D[i++%D.length];A.textContent='';await type(Q,'> '+q,32);await w(350);await type(A,a,16);await w(2600)}})()}}
/* GSAP */
if(window.gsap&&!reduce){
 gsap.registerPlugin(ScrollTrigger);
 gsap.from('.nav',{y:-80,opacity:0,duration:.9,ease:'power3.out'});
 gsap.from('.hero .tag,.hero h1,.hero p.lead,.hero .cta>*,.hero .ask',{y:40,opacity:0,duration:.9,stagger:.12,ease:'power3.out',delay:.2});
 gsap.from('.stats div',{y:30,opacity:0,stagger:.1,duration:.7,delay:.9});
 $$('.rv').forEach(el=>gsap.to(el,{opacity:1,y:0,duration:.8,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%'}}));
 /* ScrollTrigger: progress bar, hero scrub, horizontal sections, image reveals */
 gsap.to('.sp i',{scaleX:1,ease:'none',scrollTrigger:{start:0,end:'max',scrub:.3}});
 if(hero){ScrollTrigger.create({trigger:hero,start:'top top',end:'bottom top',scrub:true,onUpdate:s=>{window.zeeP=s.progress}});
  gsap.to('.hero .wrap>div:first-child',{yPercent:-10,opacity:.15,ease:'none',scrollTrigger:{trigger:hero,start:'25% top',end:'bottom 20%',scrub:true}})}
 $$('.cp img').forEach(el=>gsap.from(el,{clipPath:'inset(0 0 100% 0 round 24px)',duration:1.1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 88%'}}));
 gsap.matchMedia().add('(min-width: 961px)',()=>{$$('.hs').forEach(sec=>{const tr=$('.h-track',sec),bar=$('.h-bar i',sec),d=()=>Math.max(0,tr.scrollWidth-innerWidth);
  const tw=gsap.to(tr,{x:()=>-d(),ease:'none',scrollTrigger:{trigger:sec,start:'top top',end:()=>'+='+d(),pin:true,scrub:.8,anticipatePin:1,invalidateOnRefresh:true,onUpdate:s=>bar.style.transform='scaleX('+s.progress+')'}});
  $$('.hp img',sec).forEach(im=>gsap.fromTo(im,{xPercent:-6},{xPercent:6,ease:'none',scrollTrigger:{trigger:im.closest('.hp'),containerAnimation:tw,start:'left right',end:'right left',scrub:true}}))})});
 addEventListener('load',()=>ScrollTrigger.refresh());
 $$('[data-count]').forEach(el=>{const n=parseFloat(el.dataset.count),s=el.dataset.suf||'',o={v:0};gsap.to(o,{v:n,duration:1.6,delay:1,ease:'power2.out',onUpdate:()=>el.textContent=Math.round(o.v)+s})});
}else{$$('.rv').forEach(e=>{e.style.opacity=1;e.style.transform='none'});$$('.hs').forEach(s=>s.classList.add('native'))}
/* ===== Three.js ===== */
const cv=$('#stage');if(!cv||!window.THREE)return;
let R;try{R=new THREE.WebGLRenderer({canvas:cv,antialias:true,alpha:true})}catch(e){return}
R.setPixelRatio(Math.min(devicePixelRatio,2));
const S=new THREE.Scene(),C=new THREE.PerspectiveCamera(38,1,.1,100);C.position.z=13;
S.add(new THREE.AmbientLight(0xffffff,.55));
const dl=new THREE.DirectionalLight(0xffffff,1.1);dl.position.set(4,6,8);S.add(dl);
const p1=new THREE.PointLight(0xFF7A00,2.2,30);p1.position.set(5,-4,5);S.add(p1);
const p2=new THREE.PointLight(0x6D28D9,2.4,30);p2.position.set(-6,4,4);S.add(p2);
function band(pts,t,col,depth){const sh=new THREE.Shape();pts.forEach((p,i)=>i?sh.lineTo(p[0],p[1]+t):sh.moveTo(p[0],p[1]+t));
 for(let i=pts.length-1;i>=0;i--)sh.lineTo(pts[i][0],pts[i][1]);
 return new THREE.Mesh(new THREE.ExtrudeGeometry(sh,{depth,bevelEnabled:true,bevelSize:.07,bevelThickness:.07,bevelSegments:4}),new THREE.MeshStandardMaterial({color:col,roughness:.32,metalness:.15,emissive:col,emissiveIntensity:.12}))}
const L=[[-2.4,-1.4],[-.3,.7],[.6,.7],[2.4,2.5]];
const G=new THREE.Group(),bands=[],W=new THREE.Group(),N=new THREE.Group();
const cols=[0x00D2BE,0x7C3AED,0xFF7A00];
[[1.9,0],[0,1],[-1.9,2]].forEach(([y,c])=>{const m=band(L.map(p=>[p[0],p[1]+y]),1,cols[c],.7);G.add(m);bands.push(m)});
const sp=band([[1,-4.5],[2.5,-3]],1,0xFF7A00,.7);G.add(sp);bands.push(sp);
G.position.set(-.1,-.6,0);W.add(G);S.add(W);S.add(N);
/* orbit ring with 3 satellites (logo colours) */
const ring=new THREE.Mesh(new THREE.TorusGeometry(4.3,.014,8,160),new THREE.MeshBasicMaterial({color:0x4FFFB0,transparent:true,opacity:.45}));
ring.rotation.x=1.15;W.add(ring);
const sats=cols.map(c=>{const m=new THREE.Mesh(new THREE.SphereGeometry(.14,16,16),new THREE.MeshBasicMaterial({color:c}));W.add(m);return m});
/* neural network that follows the three logo bands */
const tex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const x=c.getContext('2d'),g=x.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,'#fff');g.addColorStop(.35,'rgba(255,255,255,.55)');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;x.fillRect(0,0,64,64);return new THREE.CanvasTexture(c)})();
const base=[],nc=[],col=new THREE.Color();
function along(y,u){const seg=[[0,1],[1,2],[2,3]],s=Math.min(2,Math.floor(u*3)),l=u*3-s,a=L[seg[s][0]],b=L[seg[s][1]];return[a[0]+(b[0]-a[0])*l,a[1]+(b[1]-a[1])*l+y]}
[[1.9,0],[0,1],[-1.9,2]].forEach(([y,c])=>{for(let i=0;i<24;i++){const p=along(y+.5,Math.random());base.push(new THREE.Vector3(p[0]*1.5+(Math.random()-.5)*1.8,p[1]*1.5+(Math.random()-.5)*1.6,(Math.random()-.5)*5-1.2));nc.push(cols[c])}});
for(let i=0;i<26;i++){base.push(new THREE.Vector3((Math.random()-.5)*20,(Math.random()-.5)*12,-2-Math.random()*5));nc.push(0x6f86b8)}
const n=base.length,pos=new Float32Array(n*3),pcol=new Float32Array(n*3);
nc.forEach((c,i)=>{col.setHex(c);pcol.set([col.r,col.g,col.b],i*3)});
const pg=new THREE.BufferGeometry();pg.setAttribute('position',new THREE.BufferAttribute(pos,3));pg.setAttribute('color',new THREE.BufferAttribute(pcol,3));
N.add(new THREE.Points(pg,new THREE.PointsMaterial({size:.5,map:tex,vertexColors:true,transparent:true,depthWrite:false,blending:THREE.AdditiveBlending})));
const E=[];for(let i=0;i<n;i++){const d=[];for(let j=0;j<n;j++)if(i!==j)d.push([base[i].distanceTo(base[j]),j]);d.sort((a,b)=>a[0]-b[0]);d.slice(0,3).forEach(([dd,j])=>{if(dd<3.2&&i<j||dd<3.2&&!E.some(e=>e[0]===j&&e[1]===i))E.push([i,j])})}
const lp=new Float32Array(E.length*6),lc=new Float32Array(E.length*6);
E.forEach(([a,b],k)=>{lc.set([pcol[a*3]*.55,pcol[a*3+1]*.55,pcol[a*3+2]*.55,pcol[b*3]*.55,pcol[b*3+1]*.55,pcol[b*3+2]*.55],k*6)});
const lg=new THREE.BufferGeometry();lg.setAttribute('position',new THREE.BufferAttribute(lp,3));lg.setAttribute('color',new THREE.BufferAttribute(lc,3));
N.add(new THREE.LineSegments(lg,new THREE.LineBasicMaterial({vertexColors:true,transparent:true,opacity:.55,blending:THREE.AdditiveBlending,depthWrite:false})));
/* data pulses travelling along edges */
const NP=34,pp=new Float32Array(NP*3),pu=[];for(let i=0;i<NP;i++)pu.push({e:Math.floor(Math.random()*E.length),t:Math.random(),v:.004+Math.random()*.01});
const pgm=new THREE.BufferGeometry();pgm.setAttribute('position',new THREE.BufferAttribute(pp,3));
N.add(new THREE.Points(pgm,new THREE.PointsMaterial({size:.42,map:tex,color:0xffffff,transparent:true,depthWrite:false,blending:THREE.AdditiveBlending})));
function size(){const w=cv.clientWidth,h=cv.clientHeight;R.setSize(w,h,false);C.aspect=w/h;C.updateProjectionMatrix();const s=w<600?.58:.9;W.scale.setScalar(s);N.scale.setScalar(w<600?.7:1)}
size();addEventListener('resize',size);
let tx=0,ty=0,mx=0,my=0,drag=false,sx=0,rot=0;const host=cv.parentElement;
host.addEventListener('pointermove',e=>{const r=host.getBoundingClientRect();mx=((e.clientX-r.left)/r.width-.5)*2;my=((e.clientY-r.top)/r.height-.5)*2});
cv.addEventListener('pointerdown',e=>{drag=true;sx=e.clientX;cv.style.cursor='grabbing'});
addEventListener('pointerup',()=>{drag=false;cv.style.cursor='grab'});
addEventListener('pointermove',e=>{if(drag){rot+=(e.clientX-sx)*.01;sx=e.clientX}});
if(window.gsap&&!reduce){bands.forEach((b,i)=>{gsap.from(b.position,{x:-6,y:-4,z:-3,duration:1.6,delay:.3+i*.18,ease:'expo.out'});gsap.from(b.rotation,{z:.6,duration:1.6,delay:.3+i*.18,ease:'expo.out'})});
 gsap.from(W.scale,{x:.2,y:.2,z:.2,duration:1.4,ease:'back.out(1.4)'});gsap.from(N.scale,{x:.3,y:.3,z:.3,duration:2,ease:'expo.out'});gsap.from(ring.scale,{x:.1,y:.1,z:.1,duration:1.8,delay:.6,ease:'expo.out'})}
let vis=true;new IntersectionObserver(e=>vis=e[0].isIntersecting).observe(host);
const clk=new THREE.Clock(),P=new THREE.Vector3();
(function loop(){requestAnimationFrame(loop);if(!vis||document.hidden)return;const t=clk.getElapsedTime(),k=reduce?0:1;
 tx+=(mx*.5-tx)*.06;ty+=(my*.3-ty)*.06;
 const sp=(window.zeeP||0)*k;W.rotation.y=tx+rot+Math.sin(t*.5)*.12*k+sp*1.8;W.rotation.x=-ty*.8+sp*.3;W.position.y=-sp*1.2;N.position.y=sp*1.5;
 bands.forEach((b,i)=>b.position.z=Math.sin(t*1.2+i*1.1)*.28*k);G.position.y=-.6+Math.sin(t*.8)*.12*k;
 ring.rotation.z=t*.25*k;sats.forEach((s,i)=>{const a=t*.7*k+i*2.094;s.position.set(Math.cos(a)*4.3,Math.sin(a)*4.3*Math.cos(1.15)*1,Math.sin(a)*4.3*Math.sin(1.15))});
 const hh=4.5,hw=hh*C.aspect,mxw=mx*hw,myw=-my*hh;
 for(let i=0;i<n;i++){const b=base[i];let x=b.x+Math.sin(t*.6+i)*.25*k,y=b.y+Math.cos(t*.5+i*1.3)*.25*k,z=b.z;
  const dx=x-mxw,dy=y-myw,d=Math.hypot(dx,dy);if(d<2.4&&k){const f=(2.4-d)*.28;x+=dx/d*f;y+=dy/d*f;z+=f}
  pos[i*3]=x;pos[i*3+1]=y;pos[i*3+2]=z}
 pg.attributes.position.needsUpdate=true;
 E.forEach(([a,b],q)=>{lp.set([pos[a*3],pos[a*3+1],pos[a*3+2],pos[b*3],pos[b*3+1],pos[b*3+2]],q*6)});lg.attributes.position.needsUpdate=true;
 pu.forEach((u,i)=>{u.t+=u.v*(k?1:0);if(u.t>1){u.t=0;u.e=Math.floor(Math.random()*E.length)}const[a,b]=E[u.e];
  for(let c=0;c<3;c++)pp[i*3+c]=pos[a*3+c]+(pos[b*3+c]-pos[a*3+c])*u.t});pgm.attributes.position.needsUpdate=true;
 N.rotation.y=tx*.35;N.position.x=-tx*.3;p1.position.x=5+mx*3;p2.position.y=4-my*3;
 R.render(S,C)})();
})();
