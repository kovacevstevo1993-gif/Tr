// Oggetti 3D dello short 008 (CEDOLARE SECCA / AFFITTI): look NUOVO "appartamento in affitto di sera"
// pareti verde petrolio, parquet, finestra sulla citta' di notte, luce calda di lampada, medaglioni d'oro, chiavi, calendario
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export {makeAnchor} from '/code/lib/s006.js';
export const THEME={bg:0x0a1f27,fogN:26,fogF:70,keyC:0xffd9a0,keyI:240,rimC:0x5fb8ff,rimI:40,hemiS:0x6fa3b8,hemiG:0x2a1a10,hemiI:.5,floor:0x6b4328,fR:.4,fM:0,ring:0xffffff,ringK:0,env:.55,expo:.78,bloom:.2,flashK:.3,dustC:0xffe6b8,dustO:.3};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.6,metalness:.02},o));
export function mats(){return {wall:M(0x1d5560,{roughness:.9}),wallD:M(0x153f48,{roughness:.9}),wood:M(0x7a4a28,{roughness:.45}),woodD:M(0x4a2a14,{roughness:.5}),
  sofa:M(0xc7683a,{roughness:.85}),sofaD:M(0xa5502a,{roughness:.85}),cream:M(0xf0e6d0,{roughness:.8}),gold:M(0xf3be3a,{metalness:1,roughness:.25}),chrome:M(0xe3e8ee,{metalness:1,roughness:.2}),
  paper:M(0xfbf8ee,{roughness:.8}),leaf:M(0x3f9a55,{roughness:.8}),pot:M(0xd9c7a8,{roughness:.7}),red:M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.35,roughness:.4}),
  mint:M(0x2fe0a0,{emissive:0x0a6a4c,emissiveIntensity:.5,roughness:.4}),shade:M(0xffe2a8,{emissive:0xffb347,emissiveIntensity:.45,roughness:.6}),dark:M(0x1a1d22,{roughness:.5,metalness:.3}),curtain:M(0xe6d8c0,{roughness:.9,side:THREE.DoubleSide})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
const cvs=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return [c,c.getContext('2d')];};
const tex=(c)=>{const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;return t;};
// ---------------- stanza ----------------
export function room(scene,m){
  // parquet a listelli
  const [pc,pg]=cvs(1024,1024);for(let r=0;r<16;r++)for(let k=0;k<4;k++){const sh=.82+rnd(r*7+k)*.3;pg.fillStyle=`rgb(${Math.round(122*sh)},${Math.round(76*sh)},${Math.round(42*sh)})`;const x=((k*256+(r%2)*128)%1024);pg.fillRect(x,r*64,252,60);
    pg.fillStyle='rgba(0,0,0,.18)';for(let q=0;q<6;q++)pg.fillRect(x+rnd(r*31+k*7+q)*240,r*64+8+q*8,40+rnd(q+r)*60,1.5);}
  const pt=tex(pc);pt.wrapS=pt.wrapT=THREE.RepeatWrapping;pt.repeat.set(3,2.4);
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(40,28),new THREE.MeshStandardMaterial({map:pt,roughness:.38,metalness:.05}));fl.rotation.x=-Math.PI/2;fl.position.set(0,.01,4);fl.receiveShadow=true;scene.add(fl);
  // pareti
  const bw=new THREE.Mesh(new THREE.PlaneGeometry(40,14),m.wall);bw.position.set(0,7,-6.2);bw.receiveShadow=true;scene.add(bw);
  const lw=new THREE.Mesh(new THREE.PlaneGeometry(28,14),m.wallD);lw.rotation.y=Math.PI/2;lw.position.set(-14,7,4);lw.receiveShadow=true;scene.add(lw);
  const rw=new THREE.Mesh(new THREE.PlaneGeometry(28,14),m.wallD);rw.rotation.y=-Math.PI/2;rw.position.set(14,7,4);rw.receiveShadow=true;scene.add(rw);
  // zoccolino
  add(scene,new THREE.Mesh(new THREE.BoxGeometry(40,.5,.12),m.cream),0,.26,-6.1);
  // finestra con citta' di notte
  const [sc,sg]=cvs(1024,640);const gr=sg.createLinearGradient(0,0,0,640);gr.addColorStop(0,'#0b1d3d');gr.addColorStop(.7,'#27406b');gr.addColorStop(1,'#d98a52');sg.fillStyle=gr;sg.fillRect(0,0,1024,640);
  for(let i=0;i<60;i++){sg.fillStyle='rgba(255,255,255,'+(.3+rnd(i)*.6)+')';sg.fillRect(rnd(i+5)*1024,rnd(i+9)*260,2,2);}
  for(let b=0;b<16;b++){const bx=b*66-10,bh=140+rnd(b+3)*300,bwid=52+rnd(b+8)*30;sg.fillStyle=b%2?'#0f1a30':'#15233f';sg.fillRect(bx,640-bh,bwid,bh);
    for(let wy=640-bh+14;wy<620;wy+=22)for(let wx=bx+7;wx<bx+bwid-10;wx+=15){if(rnd(wx*3+wy)>.45){sg.fillStyle=rnd(wx+wy)>.5?'#ffd27a':'#fff0c0';sg.fillRect(wx,wy,8,11);}}}
  const win=new THREE.Mesh(new THREE.PlaneGeometry(9,5.6),new THREE.MeshBasicMaterial({map:tex(sc),fog:false}));win.position.set(0,5.1,-6.1);scene.add(win);
  const fr=new THREE.Group();[[0,2.85,9.5,.28],[0,-2.85,9.5,.28],[-4.6,0,.28,5.9],[4.6,0,.28,5.9],[0,0,.1,5.6]].forEach(([x,y,w,h])=>add(fr,new THREE.Mesh(new THREE.BoxGeometry(w,h,.3),m.cream),x,y,0));fr.position.set(0,5.1,-6.0);scene.add(fr);
  // davanzale
  add(scene,new THREE.Mesh(new THREE.BoxGeometry(10,.2,.7),m.cream),0,2.15,-5.85);
  // macchine che passano (puntini luminosi nella finestra)
  const cars=[];for(let i=0;i<6;i++){const c=new THREE.Mesh(new THREE.SphereGeometry(.07,8,8),new THREE.MeshBasicMaterial({color:i%2?0xffe9a0:0xff5a4a,fog:false}));c.position.set(0,2.7+rnd(i)*.15,-6.05);scene.add(c);cars.push(c);}
  scene.userData.cars=cars;
  // tende
  const cur=[];[-5.4,5.4].forEach((x,i)=>{const cg=new THREE.PlaneGeometry(1.8,6.2,14,1);const c=new THREE.Mesh(cg,m.curtain);c.position.set(x,5,-5.6);c.castShadow=true;scene.add(c);c.userData.x0=x;cur.push(c);});scene.userData.curtains=cur;
  // quadri alle pareti
  [[-9,5,-6.1,3,2.2,0xe9b44c],[9,5.4,-6.1,2.4,3,0x4fb0a5],[-13.9,5,2,2.6,2,0xd9693a]].forEach(([x,y,z,w,h,c],i)=>{const g=new THREE.Group();add(g,new THREE.Mesh(new THREE.BoxGeometry(w+.3,h+.3,.1),m.woodD),0,0,0);
    const [qc,qg]=cvs(256,256);qg.fillStyle='#f4ecd8';qg.fillRect(0,0,256,256);qg.fillStyle='#'+c.toString(16).padStart(6,'0');qg.beginPath();qg.arc(110,130,70,0,7);qg.fill();qg.fillStyle='#12303a';qg.fillRect(130,60,70,150);
    const p=new THREE.Mesh(new THREE.PlaneGeometry(w,h),new THREE.MeshStandardMaterial({map:tex(qc),roughness:.7}));p.position.z=.06;g.add(p);g.position.set(x,y,z);if(i===2)g.rotation.y=Math.PI/2;scene.add(g);});
}
export function moveRoom(scene,t){(scene.userData.cars||[]).forEach((c,i)=>{const sp=.25+i*.07;const u=((t*sp+i*.37)%1);c.position.x=(i%2?-1:1)*(-4.2+u*8.4);});
  (scene.userData.curtains||[]).forEach((c,ci)=>{const p=c.geometry.attributes.position;for(let i=0;i<p.count;i++){const y=p.getY(i);p.setZ(i,Math.sin(y*1.3+t*1.4+ci)*.08*(1-(y+3.1)/6.2)+Math.sin(p.getX(i)*6+t*.9)*.03);}p.needsUpdate=true;c.geometry.computeVertexNormals();});}
// ---------------- arredo ----------------
export function sofa(m){const g=new THREE.Group();add(g,rbox(5.2,.9,2.1,.25,m.sofa),0,.7,0);add(g,rbox(5.2,1.6,.7,.28,m.sofaD),0,1.5,-.75);add(g,rbox(.7,1.3,2.0,.25,m.sofaD),-2.5,1.05,0);add(g,rbox(.7,1.3,2.0,.25,m.sofaD),2.5,1.05,0);
  [[-1.3,0xf0e6d0],[1.2,0x2fa58a]].forEach(([x,c])=>{const cu=rbox(.95,.95,.3,.12,M(c,{roughness:.9}));cu.rotation.set(-.2,x*.1,x*.08);add(g,cu,x,1.5,.1);});
  [[-2.2,.2,.8],[2.2,.2,.8],[-2.2,.2,-.8],[2.2,.2,-.8]].forEach(([x,y,z])=>add(g,new THREE.Mesh(new THREE.CylinderGeometry(.09,.07,.4,10),m.woodD),x,y,z));return g;}
export function lamp(m){const g=new THREE.Group();add(g,new THREE.Mesh(new THREE.CylinderGeometry(.45,.5,.1,24),m.dark),0,.05,0);add(g,new THREE.Mesh(new THREE.CylinderGeometry(.04,.04,4.4,10),m.chrome),0,2.3,0);
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.55,.95,1.05,32,1,true),m.shade),0,4.6,0);const l=new THREE.PointLight(0xffb86b,60,16,1.7);l.position.y=4.5;g.add(l);g.userData.light=l;return g;}
export function plant(m){const g=new THREE.Group();add(g,new THREE.Mesh(new THREE.CylinderGeometry(.55,.4,.9,20),m.pot),0,.45,0);
  for(let i=0;i<9;i++){const a=i/9*6.28;const lf=new THREE.Mesh(new THREE.SphereGeometry(.45,12,10),m.leaf);lf.scale.set(.35,1.3,.12);lf.position.set(Math.cos(a)*.35,1.7+rnd(i)*.5,Math.sin(a)*.35);lf.rotation.set(Math.sin(a)*.5,a,Math.cos(a)*.5);lf.castShadow=true;g.add(lf);}return g;}
export function rug(){const [c,g]=cvs(512,512);g.fillStyle='#b8a47c';g.fillRect(0,0,512,512);g.strokeStyle='#c7683a';g.lineWidth=14;g.strokeRect(24,24,464,464);g.strokeStyle='#1d5560';g.lineWidth=8;g.strokeRect(54,54,404,404);
  for(let i=0;i<5;i++){g.strokeStyle='#d9a441';g.lineWidth=4;g.beginPath();g.moveTo(256,96+i*8);g.lineTo(416-i*40,256);g.lineTo(256,416-i*8);g.lineTo(96+i*40,256);g.closePath();g.stroke();}
  const r=new THREE.Mesh(new THREE.PlaneGeometry(13,9),new THREE.MeshStandardMaterial({map:tex(c),roughness:.95}));r.rotation.x=-Math.PI/2;r.position.set(0,.025,1.2);r.receiveShadow=true;return r;}
export function boxes(m){const g=new THREE.Group();[[0,.55,0,1.4,1.1,1.1],[1.5,.4,.2,1.1,.8,1.0],[.5,1.4,-.1,1.0,.8,.9]].forEach(([x,y,z,w,h,d],i)=>{const b=add(g,new THREE.Mesh(new THREE.BoxGeometry(w,h,d),M(0xc9a066,{roughness:.9})),x,y,z);b.rotation.y=i*.2;
  add(g,new THREE.Mesh(new THREE.BoxGeometry(w*.98,.08,d*.2),M(0x8c6a3a)),x,y+h/2+.01,z).rotation.y=i*.2;});return g;}
// ---------------- oggetti dei concetti ----------------
// medaglione d'oro con scritta (10 %, 5 %, 1 %)
export function medal(m,text,{r=1.35,face='#f3be3a',ink='#5a3a00',ring='#fff1b8'}={}){const g=new THREE.Group();
  const [c,x]=cvs(512,512);const gr=x.createRadialGradient(256,230,40,256,256,256);gr.addColorStop(0,'#fff2b0');gr.addColorStop(.6,face);gr.addColorStop(1,'#b8811a');x.fillStyle=gr;x.beginPath();x.arc(256,256,256,0,7);x.fill();
  x.strokeStyle=ring;x.lineWidth=14;x.beginPath();x.arc(256,256,226,0,7);x.stroke();x.strokeStyle='rgba(120,80,0,.5)';x.lineWidth=5;x.beginPath();x.arc(256,256,206,0,7);x.stroke();
  x.fillStyle=ink;x.textAlign='center';x.textBaseline='middle';x.font='bold '+(text.length>3?170:230)+'px AB';x.fillText(text,256,268);
  const t=tex(c);t.center.set(.5,.5);t.rotation=Math.PI/2;const side=M(0xd9a02a,{metalness:1,roughness:.3});const face_=new THREE.MeshStandardMaterial({map:t,metalness:.6,roughness:.3});
  const cy=new THREE.Mesh(new THREE.CylinderGeometry(r,r,.28,64),[side,face_,face_]);cy.rotation.x=Math.PI/2;cy.castShadow=true;g.add(cy);
  const rim=new THREE.Mesh(new THREE.TorusGeometry(r,.07,16,64),side);g.add(rim);g.userData.mat=face_;return g;}
// mazzo di chiavi con targhetta
export function keychain(m,label,tagCol='#2fe0a0'){const g=new THREE.Group();
  const ring=new THREE.Mesh(new THREE.TorusGeometry(.5,.05,12,40),m.chrome);ring.position.y=1.2;g.add(ring);
  for(let k=0;k<2;k++){const kk=new THREE.Group();const head=new THREE.Mesh(new THREE.TorusGeometry(.26,.09,12,28),m.gold);kk.add(head);
    const sh=new THREE.Mesh(new THREE.CylinderGeometry(.07,.07,1.5,12),m.gold);sh.position.y=-.95;kk.add(sh);[-.9,-1.2,-1.5].forEach((y,i)=>{const tt=new THREE.Mesh(new THREE.BoxGeometry(.34-i*.05,.13,.09),m.gold);tt.position.set(.2,y,0);kk.add(tt);});
    kk.traverse(o=>o.castShadow=true);kk.position.set(k?.25:-.25,.95,0);kk.rotation.z=k?.25:-.25;g.add(kk);}
  const [c,x]=cvs(512,256);x.fillStyle=tagCol;x.beginPath();x.roundRect(8,8,496,240,40);x.fill();x.fillStyle='#07222a';x.textAlign='center';x.textBaseline='middle';
  let f=96;x.font='bold '+f+'px AB';while(x.measureText(label).width>440&&f>30){f-=4;x.font='bold '+f+'px AB';}x.fillText(label,256,134);
  const tg=new THREE.Mesh(new THREE.BoxGeometry(1.7,.85,.08),[M(0x222),M(0x222),M(0x222),M(0x222),new THREE.MeshStandardMaterial({map:tex(c),roughness:.5}),new THREE.MeshStandardMaterial({map:tex(c),roughness:.5})]);tg.position.set(0,1.5,.05);g.add(tg);
  g.userData.tag=tg;g.rotation.x=0;return g;}
export function check(){const g=new THREE.Group();const mt=M(0x2fe0a0,{emissive:0x0f8a63,emissiveIntensity:.8,roughness:.4});
  const a=new THREE.Mesh(new THREE.BoxGeometry(.36,.8,.2),mt);a.position.set(-.35,-.1,0);a.rotation.z=.75;const b=new THREE.Mesh(new THREE.BoxGeometry(.36,1.5,.2),mt);b.position.set(.28,.25,0);b.rotation.z=-.75;g.add(a,b);g.traverse(o=>o.castShadow=true);return g;}
export function cross(){const g=new THREE.Group();const mt=M(0xff4a3d,{emissive:0x9a1810,emissiveIntensity:.8,roughness:.4});
  [.785,-.785].forEach(r=>{const b=new THREE.Mesh(new THREE.BoxGeometry(.36,1.7,.2),mt);b.rotation.z=r;g.add(b);});g.traverse(o=>o.castShadow=true);return g;}
// contratto di locazione
export function lease(label='CONTRATTO DI LOCAZIONE',sub='CANONE CONCORDATO'){return sheet((c,W,H)=>{c.fillStyle='#fbf8ee';c.fillRect(0,0,W,H);c.fillStyle='#12303a';c.font='bold 34px AB';c.textAlign='center';c.textBaseline='middle';c.fillText(label,W/2,86);
  c.fillStyle='#d9a441';c.font='bold 30px PM';c.fillText(sub,W/2,140);c.fillStyle='#c9cfda';for(let i=0;i<9;i++)c.fillRect(60,200+i*46,W-120-(i%3)*70,13);
  c.strokeStyle='#12303a';c.lineWidth=5;c.beginPath();c.moveTo(70,H-110);c.bezierCurveTo(130,H-190,170,H-60,230,H-120);c.bezierCurveTo(260,H-150,290,H-80,340,H-130);c.stroke();
  c.strokeStyle='#12303a';c.lineWidth=6;c.strokeRect(8,8,W-16,H-16);},520,740,2.6,null);}
// timbro (testo inclinato su rettangolo con bordo)
export function stamp(text,col='#e5392b'){const [c,g]=cvs(640,240);g.strokeStyle=col;g.lineWidth=16;g.beginPath();g.roundRect(14,14,612,212,26);g.stroke();g.fillStyle=col;g.textAlign='center';g.textBaseline='middle';
  let f=120;g.font='bold '+f+'px AB';while(g.measureText(text).width>540&&f>30){f-=4;g.font='bold '+f+'px AB';}g.fillText(text,320,126);
  const p=new THREE.Mesh(new THREE.PlaneGeometry(3.4,3.4*240/640),new THREE.MeshBasicMaterial({map:tex(c),transparent:true,depthWrite:false,toneMapped:false}));p.renderOrder=5;return p;}
// calendario: foglio che si stacca (anno)
export function calPage(year,col='#fbf8ee'){const [c,g]=cvs(512,640);g.fillStyle=col;g.fillRect(0,0,512,640);g.fillStyle='#e5392b';g.fillRect(0,0,512,120);g.fillStyle='#fff';g.font='bold 70px AB';g.textAlign='center';g.textBaseline='middle';g.fillText('DICEMBRE',256,64);
  g.fillStyle='#12303a';g.font='bold 190px AB';g.fillText(String(year),256,330);g.fillStyle='#c9cfda';for(let i=0;i<6;i++)for(let j=0;j<7;j++)g.fillRect(40+j*66,470+i*0,0,0);g.fillStyle='#12303a';g.font='bold 120px AB';g.fillText('31',256,540);
  const p=new THREE.Mesh(new THREE.PlaneGeometry(2.6,3.25),new THREE.MeshStandardMaterial({map:tex(c),roughness:.7,side:THREE.DoubleSide}));p.castShadow=true;return p;}
// casetta di citta' (per la mappa del comune)
export function townHouse(m,col=0xe9d9b8,roof=0xb5482a){const g=new THREE.Group();add(g,new THREE.Mesh(new THREE.BoxGeometry(1.1,.9,1),M(col,{roughness:.8})),0,.45,0);
  const rf=new THREE.Mesh(new THREE.ConeGeometry(.95,.6,4),M(roof,{roughness:.6}));rf.rotation.y=Math.PI/4;rf.position.y=1.2;rf.castShadow=true;g.add(rf);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.22,.34,.04),M(0xffd27a,{emissive:0xffb347,emissiveIntensity:.8})),0,.5,.52);return g;}
export function pin(){const g=new THREE.Group();const mt=M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.4,roughness:.35});const s=new THREE.Mesh(new THREE.SphereGeometry(.55,24,18),mt);s.position.y=1.3;g.add(s);
  const c=new THREE.Mesh(new THREE.ConeGeometry(.5,1.2,24),mt);c.rotation.x=Math.PI;c.position.y=.55;g.add(c);const h=new THREE.Mesh(new THREE.SphereGeometry(.2,12,10),M(0xffffff));h.position.set(0,1.35,.42);g.add(h);g.traverse(o=>o.castShadow=true);return g;}
// cuore (mi piace)
export function heart(){const s=new THREE.Shape();s.moveTo(0,-1);s.bezierCurveTo(-1.6,-.1,-1.1,1.1,0,.55);s.bezierCurveTo(1.1,1.1,1.6,-.1,0,-1);
  const m=new THREE.Mesh(new THREE.ExtrudeGeometry(s,{depth:.45,bevelEnabled:true,bevelSize:.1,bevelThickness:.1,bevelSegments:4,curveSegments:24}),M(0xff3b5c,{emissive:0x8a1030,emissiveIntensity:.5,roughness:.3}));m.castShadow=true;return m;}
// giornale con titolo (fonte)
export function paper(title){return sheet((c,W,H)=>{c.fillStyle='#ece5d3';c.fillRect(0,0,W,H);c.fillStyle='#1b1b1b';c.font='bold 54px AB';c.textAlign='center';c.textBaseline='middle';c.fillText(title,W/2,70);c.fillRect(30,118,W-60,5);
  for(let i=0;i<11;i++){c.fillStyle='#9a9484';c.fillRect(40,150+i*40,W-80-(i%4)*50,10);}c.fillStyle='#c9bfa5';c.fillRect(W-210,150,170,150);},520,520,2.4,null);}
// torre di monete (1 moneta = 60 euro): n monete, spessore h; bande di colore
export function coinTower(m,{max=24,r=.8,h=.32}={}){const geo=new THREE.CylinderGeometry(r,r,1,40);const mat=new THREE.MeshStandardMaterial({color:0xffffff,metalness:.95,roughness:.28});
  const mesh=new THREE.InstancedMesh(geo,mat,max);mesh.castShadow=true;mesh.receiveShadow=true;const d=new THREE.Object3D();const col=new THREE.Color();let base=0xf3be3a;
  mesh.userData={set(x,c=base){for(let i=0;i<max;i++){const full=Math.floor(x);let sy=0;if(i<full)sy=h*.92;else if(i===full)sy=h*.92*(x-full);d.position.set(0,i*h+(sy||.001)/2,0);d.rotation.y=i*.35;d.scale.set(sy>0?1:0,Math.max(.0001,sy),sy>0?1:0);d.updateMatrix();mesh.setMatrixAt(i,d.matrix);col.setHex(c);mesh.setColorAt(i,col);}mesh.instanceMatrix.needsUpdate=true;mesh.instanceColor.needsUpdate=true;}};
  mesh.userData.set(0);return mesh;}
// cartellino in piedi (percentuale sotto la torre)
export function plaque(text,col='#f3be3a'){const [c,g]=cvs(512,256);g.fillStyle='#0a262e';g.beginPath();g.roundRect(8,8,496,240,36);g.fill();g.strokeStyle=col;g.lineWidth=10;g.stroke();g.fillStyle=col;g.textAlign='center';g.textBaseline='middle';g.font='bold 150px AB';g.fillText(text,256,134);
  const p=new THREE.Mesh(new THREE.PlaneGeometry(2.1,1.05),new THREE.MeshStandardMaterial({map:tex(c),roughness:.5,emissive:0x111111}));p.castShadow=true;return p;}
// ---------------- arredo completo (stessa stanza in tutti i blocchi) ----------------
export function furnish(scene,m){room(scene,m);scene.add(rug());
  const so=sofa(m);so.position.set(4.4,0,-4.0);so.rotation.y=-.3;scene.add(so);
  const la=lamp(m);la.position.set(-7.2,0,-4.4);scene.add(la);scene.userData.lamp=la;
  const pl=plant(m);pl.position.set(-5.6,0,-3.2);scene.add(pl);const pl2=plant(m);pl2.position.set(7.8,0,-3.0);pl2.scale.setScalar(1.2);scene.add(pl2);
  const bx=boxes(m);bx.position.set(-4.4,0,-1.6);bx.rotation.y=.4;scene.add(bx);
  const bx2=boxes(m);bx2.position.set(6.6,0,-1.0);bx2.rotation.y=-.5;bx2.scale.setScalar(.9);scene.add(bx2);}
export function liveRoom(scene,t){moveRoom(scene,t);const l=scene.userData.lamp;if(l)l.userData.light.intensity=60+Math.sin(t*3.1)*3+Math.sin(t*7.7)*1.5;}
