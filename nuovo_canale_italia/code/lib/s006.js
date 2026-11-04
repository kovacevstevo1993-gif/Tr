// Oggetti 3D dello short 006 (SOLDI FERMI SUL CONTO): look NUOVO "caveau di banca" (acciaio e verde petrolio, marmo lucido, banconote, vetri con i tassi)
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export const THEME={bg:0x0b3442,fogN:22,fogF:60,keyC:0xfff1d8,keyI:330,rimC:0x19d37a,rimI:70,hemiS:0xa9e3f0,hemiG:0x06222c,hemiI:.4,floor:0x0c2d39,fR:.12,fM:.55,ring:0xffffff,ringK:.12,env:.55,expo:.8,bloom:.1,flashK:.3,dustC:0xffffff,dustO:.3};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.5,metalness:.05},o));
export function mats(){return {steel:M(0x6f8794,{metalness:.85,roughness:.32}),steelD:M(0x3d5460,{metalness:.8,roughness:.4}),chrome:M(0xe3e8ee,{metalness:1,roughness:.18}),gold:M(0xf3be3a,{metalness:1,roughness:.3}),
  green:M(0x19d37a,{emissive:0x0a6a3c,emissiveIntensity:.6,roughness:.35}),red:M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.4,roughness:.4}),paper:M(0xf2efe6,{roughness:.8}),band:M(0xc99b5c,{roughness:.85}),
  navy:M(0x12303c,{roughness:.55}),marble:M(0xeef2f3,{roughness:.12,metalness:.05}),wood:M(0x5b3a22,{roughness:.5}),kraft:M(0xc99b5c,{roughness:.9})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// ---- fondale: parete di cassette di sicurezza e porta del caveau ----
export function backdrop(scene,m){
  const wall=new THREE.Mesh(new THREE.PlaneGeometry(90,40),new THREE.MeshStandardMaterial({color:0x2c4b58,roughness:.6,metalness:.4}));wall.position.set(0,10,-16);wall.receiveShadow=true;scene.add(wall);
  const cols=18,rows=9;const bx=new THREE.BoxGeometry(1.5,1.05,.5);
  const inst=new THREE.InstancedMesh(bx,new THREE.MeshStandardMaterial({color:0x8aa0ab,metalness:.9,roughness:.3}),cols*rows);const d=new THREE.Object3D();let k=0;
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){d.position.set(-13.4+c*1.58,.7+r*1.14,-15.6);d.scale.setScalar(.96+rnd(k)*.04);d.updateMatrix();inst.setMatrixAt(k++,d.matrix);}
  inst.castShadow=true;inst.receiveShadow=true;scene.add(inst);
  const kn=new THREE.InstancedMesh(new THREE.CylinderGeometry(.07,.07,.1,12),m.gold,cols*rows);k=0;
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){d.position.set(-13.4+c*1.58,.7+r*1.14,-15.3);d.rotation.set(Math.PI/2,0,0);d.scale.setScalar(1);d.updateMatrix();kn.setMatrixAt(k++,d.matrix);}
  scene.add(kn);
  // porta del caveau (disco d'acciaio con bulloni e ruota)
  const door=new THREE.Group();const disc=new THREE.Mesh(new THREE.CylinderGeometry(4.2,4.2,.7,64),m.steel);disc.rotation.x=Math.PI/2;door.add(disc);
  const ring=new THREE.Mesh(new THREE.TorusGeometry(4.2,.32,20,80),m.chrome);door.add(ring);
  for(let i=0;i<16;i++){const a=i/16*Math.PI*2;const b=new THREE.Mesh(new THREE.CylinderGeometry(.16,.16,.5,16),m.chrome);b.rotation.x=Math.PI/2;b.position.set(Math.cos(a)*3.5,Math.sin(a)*3.5,.45);door.add(b);}
  const hub=new THREE.Mesh(new THREE.CylinderGeometry(.9,.9,.6,32),m.gold);hub.rotation.x=Math.PI/2;hub.position.z=.55;door.add(hub);
  for(let i=0;i<3;i++){const sp=new THREE.Mesh(new THREE.BoxGeometry(5.4,.24,.24),m.chrome);sp.rotation.z=i/3*Math.PI;sp.position.z=.75;door.add(sp);}
  door.scale.setScalar(.8);door.position.set(0,7.6,-15.2);door.traverse(o=>{o.castShadow=true;});scene.add(door);door.userData.wheel=door.children[door.children.length-1];
  // strisce luminose a soffitto e pavimento riflettente (tappeto verde)
  for(let i=-3;i<=3;i++){const l=new THREE.Mesh(new THREE.BoxGeometry(.4,.06,10),new THREE.MeshBasicMaterial({color:0xffffff,toneMapped:false}));l.position.set(i*4,13,-4);scene.add(l);}
  return door;}
// ---- banconota da 50 euro (disegno generico a colori, senza simboli ufficiali) ----
let _bill=null;
export function billTex(){if(_bill)return _bill;const c=document.createElement('canvas');c.width=512;c.height=256;const g=c.getContext('2d');
  const gr=g.createLinearGradient(0,0,512,256);gr.addColorStop(0,'#f6a35a');gr.addColorStop(.5,'#f4b97c');gr.addColorStop(1,'#e98c3d');g.fillStyle=gr;g.fillRect(0,0,512,256);
  g.strokeStyle='rgba(120,60,10,.35)';g.lineWidth=2;for(let i=0;i<14;i++){g.beginPath();g.arc(120+i*22,128,20+i*8,0,7);g.stroke();}
  g.fillStyle='rgba(255,255,255,.35)';g.fillRect(30,24,70,208);g.fillStyle='#7a3a0a';g.font='bold 120px AB';g.textAlign='center';g.textBaseline='middle';g.fillText('50',280,120);
  g.font='bold 40px PM';g.fillText('EURO',430,70);g.strokeStyle='#7a3a0a';g.lineWidth=6;g.strokeRect(6,6,500,244);
  g.fillStyle='rgba(122,58,10,.5)';for(let i=0;i<30;i++)g.fillRect(130+i*12,206,6,10+(i%4)*4);
  _bill=new THREE.CanvasTexture(c);_bill.colorSpace=THREE.SRGBColorSpace;_bill.anisotropy=4;return _bill;}
// ---- mazzetta di banconote con fascetta (altezza regolabile) ----
export function noteStack(m,{w=2.6,d=1.3,h=.9}={}){const g=new THREE.Group();
  const sc=document.createElement('canvas');sc.width=256;sc.height=64;const sg=sc.getContext('2d');sg.fillStyle='#f3c08a';sg.fillRect(0,0,256,64);for(let i=0;i<32;i++){sg.fillStyle=i%2?'rgba(120,70,20,.35)':'rgba(255,255,255,.35)';sg.fillRect(0,i*2,256,1);}
  const st_=new THREE.CanvasTexture(sc);st_.colorSpace=THREE.SRGBColorSpace;const side=new THREE.MeshStandardMaterial({map:st_,roughness:.8});const top=new THREE.MeshStandardMaterial({map:billTex(),roughness:.7});
  const body=new THREE.Mesh(new THREE.BoxGeometry(1,1,1),[side,side,top,side,side,side]);body.castShadow=true;body.receiveShadow=true;g.add(body);
  const band=new THREE.Mesh(new THREE.BoxGeometry(1,1,1),m.band);band.castShadow=true;g.add(band);
  g.userData.set=(hh)=>{const H=Math.max(.001,hh);body.scale.set(w,H,d);body.position.y=H/2;band.scale.set(w*.16,H+.03,d+.03);band.position.y=H/2;};
  g.userData.set(h);return g;}
// ---- banconota volante ----
export function flyNote(){const mm=new THREE.Mesh(new THREE.PlaneGeometry(1.3,.65),new THREE.MeshStandardMaterial({map:billTex(),roughness:.6,side:THREE.DoubleSide,transparent:true}));mm.castShadow=true;return mm;}
// ---- sacchetto della spesa con prodotti ----
export function bag(m){const g=new THREE.Group();
  add(g,rbox(1.7,2.0,1.0,.06,m.kraft),0,1.0,0);
  [-.35,.35].forEach(x=>{const h=new THREE.Mesh(new THREE.TorusGeometry(.38,.035,10,28,Math.PI),m.kraft);h.position.set(x,2.0,0);h.rotation.y=Math.PI/2;g.add(h);});
  const bt=new THREE.Mesh(new THREE.CylinderGeometry(.2,.24,1.1,24),new THREE.MeshStandardMaterial({color:0x2e7d4f,roughness:.2,metalness:.1}));bt.position.set(-.45,2.25,0);bt.castShadow=true;g.add(bt);
  const nk=new THREE.Mesh(new THREE.CylinderGeometry(.08,.14,.32,16),new THREE.MeshStandardMaterial({color:0x2e7d4f,roughness:.2}));nk.position.set(-.45,2.95,0);g.add(nk);
  const bread=new THREE.Mesh(new THREE.SphereGeometry(.4,24,16),new THREE.MeshStandardMaterial({color:0xd49a4a,roughness:.8}));bread.scale.set(1.4,.7,.7);bread.position.set(.35,2.15,0);bread.rotation.z=.35;bread.castShadow=true;g.add(bread);
  const car=new THREE.Mesh(new THREE.BoxGeometry(.5,.85,.4),new THREE.MeshStandardMaterial({color:0xf5f5f0,roughness:.6}));car.position.set(.1,2.3,.2);car.castShadow=true;g.add(car);
  const ap=new THREE.Mesh(new THREE.SphereGeometry(.2,20,14),new THREE.MeshStandardMaterial({color:0xd7261e,roughness:.35}));ap.position.set(.45,1.95,.4);ap.castShadow=true;g.add(ap);
  return g;}
// ---- lucchetto ----
export function padlock(m){const g=new THREE.Group();
  const sh=new THREE.Mesh(new THREE.TorusGeometry(.55,.12,16,40,Math.PI),m.chrome);sh.position.set(0,1.05,0);sh.castShadow=true;g.add(sh);
  [-.55,.55].forEach(x=>{const l=new THREE.Mesh(new THREE.CylinderGeometry(.12,.12,.4,16),m.chrome);l.position.set(x,.85,0);g.add(l);});
  add(g,rbox(1.9,1.4,.7,.2,m.gold),0,.2,0);
  const k=new THREE.Mesh(new THREE.CylinderGeometry(.14,.14,.1,20),m.navy);k.rotation.x=Math.PI/2;k.position.set(0,.3,.4);g.add(k);
  const kk=new THREE.Mesh(new THREE.BoxGeometry(.1,.36,.1),m.navy);kk.position.set(0,.08,.4);g.add(kk);g.userData.shackle=sh;return g;}
// ---- carta del conto ----
export function bankCard(m){const g=new THREE.Group();
  add(g,rbox(3.0,1.9,.08,.2,new THREE.MeshStandardMaterial({color:0x0f6e52,metalness:.5,roughness:.3})),0,0,0);
  const f=sheet((c,W,H)=>{const gr=c.createLinearGradient(0,0,W,H);gr.addColorStop(0,'#19d37a');gr.addColorStop(1,'#0a5a42');c.fillStyle=gr;c.fillRect(0,0,W,H);c.fillStyle='#e8c25a';c.fillRect(46,110,84,64);c.fillStyle='#14213d';c.font='bold 34px PM';c.textAlign='left';c.textBaseline='middle';c.fillText('CONTO CORRENTE',46,48);c.fillStyle='rgba(255,255,255,.8)';for(let i=0;i<4;i++)c.fillText('0000',46+i*130,238);},520,330,2.84,null);f.position.z=.05;g.add(f);return g;}
// ---- certificato BOT (disegno generico, non e un documento ufficiale) ----
export function certificate(){return sheet((c,W,H)=>{c.fillStyle='#f4efe0';c.fillRect(0,0,W,H);c.strokeStyle='#0f6e52';c.lineWidth=10;c.strokeRect(14,14,W-28,H-28);c.lineWidth=3;c.strokeRect(34,34,W-68,H-68);
  c.fillStyle='#0f6e52';c.font='bold 64px AB';c.textAlign='center';c.textBaseline='middle';c.fillText('BOT',W/2,120);c.font='bold 34px PM';c.fillText('TITOLO DI STATO',W/2,190);c.fillText('12 MESI',W/2,240);
  c.strokeStyle='#c4a24a';c.lineWidth=6;c.beginPath();c.arc(W/2,420,70,0,7);c.stroke();c.beginPath();c.arc(W/2,420,48,0,7);c.stroke();c.fillStyle='#c4a24a';c.font='bold 54px AB';c.fillText('€',W/2,424);
  c.fillStyle='#8a90a0';for(let i=0;i<5;i++)c.fillRect(70,540+i*30,W-140-(i%2)*90,12);},520,700,2.2,null);}
// ---- calendario ----
export function calendar(mese,giorno,col='#2a5bff'){return sheet((g,W,H)=>{g.fillStyle='#fffaf0';g.fillRect(0,0,W,H);g.fillStyle=col;g.fillRect(0,0,W,120);g.fillStyle='#fff';g.font='bold 58px PM';g.textAlign='center';g.textBaseline='middle';g.fillText(mese,W/2,64);
  g.fillStyle='#14213d';g.font='bold 280px AB';g.fillText(giorno,W/2,350);g.strokeStyle='#14213d';g.lineWidth=8;g.strokeRect(4,4,W-8,H-8);},420,520,1.6,null);}
// ---- bancone di marmo ----
export function counter(m){const g=new THREE.Group();add(g,rbox(7.4,.5,3.4,.1,m.marble),0,-.25,0);add(g,rbox(7.8,.16,3.8,.06,m.gold),0,-.58,0);return g;}
// ---- scritte ancorate allo schermo ----
export function makeAnchor(st,KF){const cp=new THREE.Vector3(),lv=new THREE.Vector3(),f=new THREE.Vector3(),r=new THREE.Vector3(),u=new THREE.Vector3(),w=new THREE.Vector3();
  function pose(t){let i=0;while(i<KF.length-2&&t>KF[i+1][0])i++;const a=KF[i],b=KF[i+1];const k=t<=a[0]?0:clamp((t-a[0])/(b[0]-a[0]));const e=(a[3]==='w')?eio(k):k*k*(3-2*k);
    cp.set(...a[1]).lerp(w.set(...b[1]),e);lv.set(...a[2]).lerp(w.set(...b[2]),e);}
  return (s,t,wf,ndcY,show,extra=1,ndcX=0)=>{pose(t);f.copy(lv).sub(cp).normalize();r.crossVectors(f,new THREE.Vector3(0,1,0)).normalize();u.crossVectors(r,f).normalize();const d=8,th=.3443;
    const p=cp.clone().addScaledVector(f,d).addScaledVector(u,ndcY*th*d).addScaledVector(r,ndcX*th*d*st.W/st.H);
    const sc=wf*(2*th*d*st.W/st.H)/s.userData.sw*extra;st.setSprite(s,p.x,p.y,p.z,show,sc);};}

// ---- moneta d'oro con euro ----
export function coin(m,{r=1.25}={}){const g=new THREE.Group();
  const body=new THREE.Mesh(new THREE.CylinderGeometry(r,r,.2,64),m.gold);body.rotation.x=Math.PI/2;body.castShadow=true;g.add(body);
  const rim=new THREE.Mesh(new THREE.TorusGeometry(r*.93,.06,12,64),m.gold);rim.position.z=.1;g.add(rim);const rim2=rim.clone();rim2.position.z=-.1;g.add(rim2);
  const mk=(z,ry)=>{const f=sheet((c,W,H)=>{c.clearRect(0,0,W,H);c.fillStyle='#b88a1c';c.font='bold 330px AB';c.textAlign='center';c.textBaseline='middle';c.fillText('€',W/2,H/2+14);},256,256,r*1.3,null);f.material.transparent=true;f.position.z=z;f.rotation.y=ry;g.add(f);};
  mk(.115,0);mk(-.115,Math.PI);return g;}
