// Oggetti 3D dello short 005 (PACCHI EXTRA UE): look NUOVO "magazzino giallo segnale" (giallo, blu cobalto, cartone kraft, nastro trasportatore, scaffali)
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export const THEME={bg:0xffcf2e,fogN:26,fogF:70,keyC:0xffffff,keyI:520,rimC:0x2a5bff,rimI:60,hemiS:0xfff3c0,hemiG:0xd9a400,hemiI:.9,floor:0xe8e2d4,fR:.72,fM:0,ring:0x14213d,ringK:.35,env:.85,expo:.92,bloom:.05,flashK:.25,dustC:0xffffff,dustO:.55};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.5,metalness:.05},o));
export function mats(){return {kraft:M(0xc99b5c,{roughness:.88}),kraftD:M(0xb0824a,{roughness:.9}),tape:M(0xead2a0,{roughness:.35,metalness:.05}),navy:M(0x14213d,{roughness:.55}),cobalt:M(0x2a5bff,{roughness:.38,metalness:.3}),
  white:M(0xf6f6f2,{roughness:.55}),chrome:M(0xe2e6ec,{metalness:1,roughness:.2}),rubber:M(0x1b1e26,{roughness:.8}),red:M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.3,roughness:.4}),
  green:M(0x25b36a,{roughness:.4}),pink:M(0xf2548d,{roughness:.45}),teal:M(0x20b8b0,{roughness:.45}),orange:M(0xff7a1a,{roughness:.45}),shelf:M(0x2a5bff,{roughness:.5,metalness:.3}),
  glass:M(0xdff0ff,{roughness:.05,transparent:true,opacity:.35})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// ---- fondale: parete gialla, scaffali con scatole, luci ----
export function backdrop(scene,m){
  const wall=new THREE.Mesh(new THREE.PlaneGeometry(140,40),new THREE.MeshStandardMaterial({color:0xffc400,roughness:.9}));wall.position.set(0,12,-26);wall.receiveShadow=true;scene.add(wall);
  const band=new THREE.Mesh(new THREE.PlaneGeometry(140,2.2),new THREE.MeshStandardMaterial({color:0x14213d,roughness:.7}));band.position.set(0,5.2,-25.9);scene.add(band);
  for(let k=0;k<7;k++){const x=-18+k*6;const rack=new THREE.Group();
    [-2.2,2.2].forEach(dx=>{const p=new THREE.Mesh(new THREE.BoxGeometry(.18,8,.18),m.shelf);p.position.set(dx,4,0);p.castShadow=true;rack.add(p);});
    [1.2,3.6,6.0].forEach((y,i)=>{const b=new THREE.Mesh(new THREE.BoxGeometry(4.6,.14,1.6),m.shelf);b.position.set(0,y,0);rack.add(b);
      for(let j=0;j<3;j++){const w=.9+rnd(k*9+i*3+j)*.7,h=.7+rnd(k*5+i*7+j+3)*.6;const bx=new THREE.Mesh(new THREE.BoxGeometry(w,h,1.1),rnd(k+i+j)>.5?m.kraft:m.kraftD);bx.position.set(-1.5+j*1.5,y+.07+h/2,0);bx.castShadow=true;rack.add(bx);}});
    rack.position.set(x,0,-20);scene.add(rack);}
  // luci a soffitto (strisce)
  for(let i=-6;i<=6;i++){const l=new THREE.Mesh(new THREE.BoxGeometry(.5,.08,9),new THREE.MeshBasicMaterial({color:0xffffff,toneMapped:false}));l.position.set(i*5,11,-6);scene.add(l);}
  // strisce gialle e nere sul pavimento
  for(let i=-1;i<=1;i+=2){const s=new THREE.Mesh(new THREE.PlaneGeometry(.22,40),new THREE.MeshBasicMaterial({color:0xffc400}));s.rotation.x=-Math.PI/2;s.position.set(i*2.1,.012,-8);scene.add(s);}}
// ---- nastro trasportatore lungo l'asse z (i pacchi arrivano verso la camera) ----
export function conveyor(m){const g=new THREE.Group();
  const c=document.createElement('canvas');c.width=128;c.height=512;const x=c.getContext('2d');x.fillStyle='#1f2b4a';x.fillRect(0,0,128,512);x.strokeStyle='#3a4d7e';x.lineWidth=10;for(let i=0;i<8;i++){x.beginPath();x.moveTo(0,i*64+8);x.lineTo(64,i*64+40);x.lineTo(128,i*64+8);x.stroke();}
  const t=new THREE.CanvasTexture(c);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(1,9);t.colorSpace=THREE.SRGBColorSpace;
  const belt=new THREE.Mesh(new THREE.PlaneGeometry(2.4,36),new THREE.MeshStandardMaterial({map:t,roughness:.7}));belt.rotation.x=-Math.PI/2;belt.position.set(0,.62,-10);belt.receiveShadow=true;g.add(belt);
  [-1.3,1.3].forEach(dx=>{const r=new THREE.Mesh(new THREE.BoxGeometry(.2,.34,36),m.cobalt);r.position.set(dx,.62,-10);r.castShadow=true;g.add(r);});
  for(let i=0;i<10;i++){[-1.2,1.2].forEach(dx=>{const l=new THREE.Mesh(new THREE.BoxGeometry(.14,.6,.14),m.navy);l.position.set(dx,.3,-26+i*4);l.castShadow=true;g.add(l);});}
  g.userData.scroll=(tt)=>{t.offset.y=-(tt*.35)%1;};return g;}
// ---- pacco di cartone con nastro ed etichetta ----
export function parcel(m,{w=1.5,h=1.05,d=1.25}={}){const g=new THREE.Group();
  add(g,rbox(w,h,d,.06,m.kraft),0,h/2,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.28,.02,d+.01),m.tape),0,h+.005,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.28,h*.45,.02),m.tape),0,h*.78,d/2+.04);
  const lab=sheet((c,W,H)=>{c.fillStyle='#fff';c.fillRect(0,0,W,H);c.fillStyle='#14213d';c.fillRect(0,0,W,70);c.fillStyle='#fff';c.font='bold 44px PM';c.textAlign='left';c.textBaseline='middle';c.fillText('EXTRA-UE',22,38);
    c.fillStyle='#14213d';for(let i=0;i<46;i++)c.fillRect(24+i*9,110,(i%3)+3,100);c.fillStyle='#8a90a0';for(let i=0;i<4;i++)c.fillRect(24,240+i*34,W-48-(i%2)*80,14);},430,380,.8,null);
  lab.position.set(-.18,h*.38,d/2+.03);g.add(lab);
  const st=sheet(()=>{},300,200,.62,null);st.userData.set=(txt,col='#e5392b')=>{const {g:c,t}=st.userData;c.clearRect(0,0,300,200);c.fillStyle=col;c.beginPath();c.moveTo(20,10);c.lineTo(280,10);c.quadraticCurveTo(292,10,292,22);c.lineTo(292,178);c.quadraticCurveTo(292,190,280,190);c.lineTo(20,190);c.quadraticCurveTo(8,190,8,178);c.lineTo(8,22);c.quadraticCurveTo(8,10,20,10);c.fill();
    c.fillStyle='#fff';c.font='bold 62px AB';c.textAlign='center';c.textBaseline='middle';c.fillText(txt,150,104);t.needsUpdate=true;};
  st.material.transparent=true;st.position.set(.36,h*.55,d/2+.05);st.rotation.z=-.08;g.add(st);g.userData.sticker=st;g.userData.lab=lab;return g;}
// ---- oggetti piccoli (maglietta, scarpa, caricabatterie, cavo, cover) ----
export function tshirt(color=0xf2548d){const s=new THREE.Shape();const p=[[-.28,.5],[-.14,.5],[-.06,.42],[.06,.42],[.14,.5],[.28,.5],[.55,.28],[.42,.08],[.28,.16],[.28,-.5],[-.28,-.5],[-.28,.16],[-.42,.08],[-.55,.28]];
  s.moveTo(p[0][0],p[0][1]);p.slice(1).forEach(q=>s.lineTo(q[0],q[1]));s.closePath();
  const geo=new THREE.ExtrudeGeometry(s,{depth:.12,bevelEnabled:true,bevelSize:.03,bevelThickness:.03,bevelSegments:2});geo.translate(0,0,-.06);
  const m=new THREE.Mesh(geo,new THREE.MeshStandardMaterial({color,roughness:.8}));m.castShadow=true;return m;}
export function shoe(color=0x2a5bff){const g=new THREE.Group();
  add(g,rbox(1.0,.3,.42,.12,new THREE.MeshStandardMaterial({color:0xf6f6f2,roughness:.6})),0,.15,0);
  add(g,rbox(.62,.34,.4,.14,new THREE.MeshStandardMaterial({color,roughness:.5})),-.14,.42,0);
  add(g,rbox(.4,.2,.38,.1,new THREE.MeshStandardMaterial({color,roughness:.5})),.26,.3,0);return g;}
export function charger(){const g=new THREE.Group();const w=new THREE.MeshStandardMaterial({color:0xf6f6f2,roughness:.45});
  add(g,rbox(.6,.6,.36,.1,w),0,.3,0);[-.12,.12].forEach(x=>add(g,new THREE.Mesh(new THREE.BoxGeometry(.06,.22,.03),new THREE.MeshStandardMaterial({color:0xc0c4cc,metalness:1,roughness:.2})),x,.7,0));return g;}
export function cable(){const g=new THREE.Group();const m=new THREE.MeshStandardMaterial({color:0x14213d,roughness:.5});for(let i=0;i<3;i++){const t=new THREE.Mesh(new THREE.TorusGeometry(.24+i*.07,.035,10,32),m);t.rotation.x=Math.PI/2;t.position.y=.06+i*.05;t.castShadow=true;g.add(t);}
  add(g,rbox(.12,.08,.1,.03,m),.45,.07,0);return g;}
export function cover(color=0x20b8b0){const g=new THREE.Group();add(g,rbox(.5,.9,.1,.1,new THREE.MeshStandardMaterial({color,roughness:.4})),0,.5,0);add(g,new THREE.Mesh(new THREE.CircleGeometry(.1,20),new THREE.MeshStandardMaterial({color:0x14213d,roughness:.4})),-.12,.8,.06);return g;}
// ---- timbro doganale (disegno) ----
export function stampMark(st,text='DOGANA',{color='#d7261e',w=640,h=260,sw=2.8}={}){
  return st.label((g,W,H)=>{g.translate(W/2,H/2);g.rotate(-.12);g.strokeStyle=color;g.fillStyle=color;g.lineWidth=14;g.strokeRect(-W/2+22,-H/2+22,W-44,H-44);g.lineWidth=4;g.strokeRect(-W/2+38,-H/2+38,W-76,H-76);g.font='bold 92px AB';g.textAlign='center';g.textBaseline='middle';g.fillText(text,0,6);},w,h,sw,'timbro');}
export function dustp(n=200,color=0xffffff,size=.07){const pos=new Float32Array(n*3);const p=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.BufferAttribute(pos,3)),new THREE.PointsMaterial({color,size,transparent:true,opacity:1,depthWrite:false}));
  p.userData.update=(t0,t,ox,oy,oz,spread=1.4)=>{const u=t-t0;const a=p.geometry.attributes.position.array;p.visible=u>0&&u<1.8;for(let i=0;i<n;i++){const r1=rnd(i),r2=rnd(i+7),r3=rnd(i+13);a[i*3]=ox+(r1-.5)*spread*(1+u);a[i*3+1]=oy+(r2-.4)*spread*.8+u*(.5+r3*1.4);a[i*3+2]=oz+(r3-.5)*.8;}p.geometry.attributes.position.needsUpdate=true;p.material.opacity=clamp(1-u/1.7);};return p;}
// ---- scritte ancorate allo schermo: posizione = camera + avanti*d + su*altezza (restano sempre nella zona sicura) ----
export function makeAnchor(st,KF){const cp=new THREE.Vector3(),lv=new THREE.Vector3(),f=new THREE.Vector3(),r=new THREE.Vector3(),u=new THREE.Vector3(),w=new THREE.Vector3();
  function pose(t){let i=0;while(i<KF.length-2&&t>KF[i+1][0])i++;const a=KF[i],b=KF[i+1];const k=t<=a[0]?0:clamp((t-a[0])/(b[0]-a[0]));const e=(a[3]==='w')?eio(k):k*k*(3-2*k);
    cp.set(...a[1]).lerp(w.set(...b[1]),e);lv.set(...a[2]).lerp(w.set(...b[2]),e);}
  return (s,t,wf,ndcY,show,extra=1,ndcX=0)=>{pose(t);f.copy(lv).sub(cp).normalize();r.crossVectors(f,new THREE.Vector3(0,1,0)).normalize();u.crossVectors(r,f).normalize();const d=8,th=.3443;
    const p=cp.clone().addScaledVector(f,d).addScaledVector(u,ndcY*th*d).addScaledVector(r,ndcX*th*d*st.W/st.H);
    const sc=wf*(2*th*d*st.W/st.H)/s.userData.sw*extra;st.setSprite(s,p.x,p.y,p.z,show,sc);};}
// ---- arco di controllo doganale con laser ----
export function gate(m){const g=new THREE.Group();
  [-1.9,1.9].forEach(x=>add(g,rbox(.35,3.2,.5,.08,m.cobalt),x,1.6+.5,0));
  add(g,rbox(4.4,.55,.6,.12,m.cobalt),0,3.5,0);add(g,new THREE.Mesh(new THREE.BoxGeometry(3.6,.08,.1),new THREE.MeshBasicMaterial({color:0xffffff,toneMapped:false})),0,3.2,.3);
  const las=new THREE.Mesh(new THREE.PlaneGeometry(3.5,.05),new THREE.MeshBasicMaterial({color:0xff2a2a,transparent:true,opacity:.9,toneMapped:false,side:THREE.DoubleSide}));las.rotation.x=0;g.add(las);g.userData.laser=las;return g;}
// ---- scontrino (carrello) ----
export function receipt(){const W=420,H=760;const s=sheet((c,w,h)=>{c.fillStyle='#fbfbf6';c.fillRect(0,0,w,h);c.fillStyle='#14213d';c.font='bold 40px PM';c.textAlign='center';c.textBaseline='middle';c.fillText('IL TUO ORDINE',w/2,56);
  c.textAlign='left';c.font='bold 30px PM';const rows=[['maglietta','4,90'],['scarpe','18,50'],['cavo','3,20'],['cover','2,90']];rows.forEach((r,i)=>{c.fillStyle='#14213d';c.fillText(r[0],34,150+i*60);c.textAlign='right';c.fillText(r[1],w-34,150+i*60);c.textAlign='left';});
  c.fillStyle='#c4cbe0';c.fillRect(34,400,w-68,6);c.fillStyle='#14213d';c.font='bold 30px PM';c.fillText('dazio + comm.',34,450);c.fillText('IVA',34,510);c.fillStyle='#e5392b';c.fillRect(20,570,w-40,110);c.fillStyle='#fff';c.font='bold 38px PM';c.fillText('TOTALE FINALE',40,625);},W,H,1.9,null);return s;}
// ---- magazzino europeo ----
export function warehouse(m){const g=new THREE.Group();
  add(g,rbox(3.4,1.7,2.2,.08,m.white),0,.85,0);add(g,rbox(3.7,.3,2.5,.08,m.cobalt),0,1.85,0);add(g,rbox(.9,1.2,.1,.05,m.navy),-.7,.6,1.12);add(g,rbox(.9,1.2,.1,.05,m.navy),.7,.6,1.12);
  const f=sheet((c,W,H)=>{S4drawFlag(c,'EU',0,0,W,H);},300,200,.9,null);f.position.set(0,1.3,1.13);g.add(f);return g;}
function S4drawFlag(g,k,x,y,w,h){g.fillStyle='#003399';g.fillRect(x,y,w,h);g.fillStyle='#ffcc00';for(let i=0;i<12;i++){const a=i/12*Math.PI*2;g.beginPath();g.arc(x+w/2+Math.cos(a)*h*.33,y+h/2+Math.sin(a)*h*.33,h*.055,0,7);g.fill();}}
// ---- dichiarazione doganale ----
export function declaration(){const s=sheet((c,W,H)=>{c.fillStyle='#f7f7f2';c.fillRect(0,0,W,H);c.fillStyle='#14213d';c.fillRect(0,0,W,110);c.fillStyle='#fff';c.font='bold 40px PM';c.textAlign='center';c.textBaseline='middle';c.fillText('DICHIARAZIONE',W/2,56);
  c.fillStyle='#14213d';c.textAlign='left';c.font='bold 30px PM';['riga 1  maglietta','riga 2  scarpe','riga 3  cavo'].forEach((t,i)=>{c.fillText(t,34,170+i*70);c.fillStyle='#e5392b';c.fillRect(W-110,150+i*70,70,38);c.fillStyle='#14213d';});
  c.fillStyle='#c4cbe0';for(let i=0;i<4;i++)c.fillRect(34,420+i*44,W-68-(i%2)*80,18);c.strokeStyle='#14213d';c.lineWidth=8;c.strokeRect(4,4,W-8,H-8);},460,620,1.9,null);return s;}
