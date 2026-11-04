// Oggetti 3D dello short 007 (MUTUO): look NUOVO "casa di giorno" (cielo azzurro, crema, terracotta, verde prato, oro)
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export {makeAnchor,coin} from '/code/lib/s006.js';
export const THEME={bg:0x8fc4ea,fogN:30,fogF:80,keyC:0xfff3dc,keyI:300,rimC:0xffd9a0,rimI:50,hemiS:0xcfe8ff,hemiG:0xe9e2cf,hemiI:.45,floor:0xcfc6b0,fR:.35,fM:0,ring:0xffffff,ringK:.1,env:.5,expo:.7,bloom:.03,flashK:.25,dustC:0xffffff,dustO:.25};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.55,metalness:.03},o));
export function mats(){return {cream:M(0xede4cf,{roughness:.75}),roof:M(0xb5482a,{roughness:.55}),wood:M(0x5b3a22,{roughness:.5}),win:M(0xffe3a0,{emissive:0xffc860,emissiveIntensity:.8}),green:M(0x5fae5b,{roughness:.85}),greenD:M(0x3f8a45,{roughness:.9}),
  blue:M(0x2a6fdb,{roughness:.4,metalness:.1}),terra:M(0xd0603a,{roughness:.5}),gold:M(0xf3be3a,{metalness:1,roughness:.25}),chrome:M(0xe3e8ee,{metalness:1,roughness:.2}),paper:M(0xfbfaf5,{roughness:.8}),navy:M(0x12263f,{roughness:.5}),red:M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.3,roughness:.4}),mint:M(0x19d37a,{emissive:0x0a6a3c,emissiveIntensity:.4,roughness:.4})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// ---- fondale: cielo con sfumatura, colline, nuvole, alberi ----
export function backdrop(scene,m){
  const c=document.createElement('canvas');c.width=16;c.height=256;const g=c.getContext('2d');const gr=g.createLinearGradient(0,0,0,256);gr.addColorStop(0,'#5aa6e6');gr.addColorStop(.6,'#bfe0f6');gr.addColorStop(1,'#f4efe2');g.fillStyle=gr;g.fillRect(0,0,16,256);
  const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;const sky=new THREE.Mesh(new THREE.PlaneGeometry(160,70),new THREE.MeshBasicMaterial({map:t,fog:false}));sky.position.set(0,22,-40);scene.add(sky);
  [[-14,-26,9],[10,-28,12],[26,-27,8],[-30,-27,10]].forEach(([x,z,r],i)=>{const h=new THREE.Mesh(new THREE.SphereGeometry(r,32,16),i%2?m.green:m.greenD);h.scale.y=.45;h.position.set(x,0,z);h.receiveShadow=true;scene.add(h);});
  for(let i=0;i<7;i++){const cl=new THREE.Group();for(let k=0;k<4;k++){const s=new THREE.Mesh(new THREE.SphereGeometry(1.3+rnd(i*4+k)*.9,16,12),new THREE.MeshBasicMaterial({color:0xffffff,fog:false}));s.scale.y=.6;s.position.set(k*1.5-2,rnd(k+i)*.5,0);cl.add(s);}cl.position.set(-26+i*9,12+rnd(i+9)*6,-33);cl.userData.sp=.15+rnd(i)*.1;scene.add(cl);scene.userData.clouds=(scene.userData.clouds||[]).concat([cl]);}
  for(let i=0;i<9;i++){const x=-18+i*4.6+rnd(i)*2,z=-14-rnd(i+3)*4;const tr=new THREE.Group();add(tr,new THREE.Mesh(new THREE.CylinderGeometry(.14,.18,1.2,10),m.wood),0,.6,0);add(tr,new THREE.Mesh(new THREE.SphereGeometry(.9,18,14),i%2?m.green:m.greenD),0,1.8,0);tr.position.set(x,0,z);scene.add(tr);}}
export function moveClouds(scene,t){(scene.userData.clouds||[]).forEach((c,i)=>{c.position.x=((-26+i*9)+t*c.userData.sp*3+40)%80-40;});}
// ---- casetta ----
export function house(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.BoxGeometry(3.2,2.2,2.4),m.cream),0,1.1,0);
  const sh=new THREE.Shape();sh.moveTo(-1.85,0);sh.lineTo(1.85,0);sh.lineTo(0,1.25);sh.closePath();const rg=new THREE.ExtrudeGeometry(sh,{depth:2.9,bevelEnabled:false});const ro=new THREE.Mesh(rg,m.roof);ro.rotation.y=Math.PI/2;ro.position.set(-1.45,2.2,0);ro.castShadow=true;g.add(ro);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.8,1.3,.08),m.wood),-.9,.65,1.24);
  [.45,1.2].forEach(x=>add(g,new THREE.Mesh(new THREE.BoxGeometry(.55,.65,.06),m.win),x,1.25,1.22));
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.4,.9,.4),m.cream),1.1,3.2,-.3);return g;}
// ---- colonna (cresce in altezza, 1 unita = 50.000 euro o 250 euro di rata) ----
export function bar(mat,w=1.5,d=1.2){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.BoxGeometry(1,1,1),mat);b.castShadow=true;b.receiveShadow=true;g.add(b);
  g.userData.set=(h,y0=0)=>{const H=Math.max(.001,h);b.scale.set(w,H,d);b.position.y=y0+H/2;};g.userData.set(.001);return g;}
// ---- contratto con riga evidenziata e penna ----
export function contract(){return sheet((c,W,H)=>{c.fillStyle='#fbfaf5';c.fillRect(0,0,W,H);c.fillStyle='#12263f';c.font='bold 36px AB';c.textAlign='center';c.textBaseline='middle';c.fillText('CONTRATTO DI MUTUO',W/2,90);
  c.fillStyle='#c9cfda';for(let i=0;i<7;i++)c.fillRect(60,170+i*52,W-120-(i%3)*60,16);
  c.fillStyle='rgba(255,225,74,.85)';c.fillRect(50,545,W-100,58);c.fillStyle='#12263f';c.font='bold 40px PM';c.textAlign='left';c.fillText('TASSO  ____ %',70,576);
  c.fillStyle='#c9cfda';for(let i=0;i<3;i++)c.fillRect(60,650+i*52,W-120-(i%2)*80,16);c.strokeStyle='#12263f';c.lineWidth=6;c.strokeRect(6,6,W-12,H-12);},520,760,2.5,null);}
export function pen(m){const g=new THREE.Group();const b=new THREE.Mesh(new THREE.CylinderGeometry(.07,.07,2.2,16),m.navy);b.rotation.z=Math.PI/2;b.castShadow=true;g.add(b);
  const tip=new THREE.Mesh(new THREE.ConeGeometry(.07,.28,16),m.gold);tip.rotation.z=-Math.PI/2;tip.position.x=1.24;g.add(tip);const cl=new THREE.Mesh(new THREE.BoxGeometry(.7,.03,.05),m.gold);cl.position.set(-.5,.08,0);g.add(cl);return g;}

// ---- torre di monete (ogni moneta = tot euro): n monete piene + una parziale; colori per fascia ----
export function coinTower(m,{max=70,r=.85,h=.11}={}){const geo=new THREE.CylinderGeometry(r,r,1,40);const mat=new THREE.MeshStandardMaterial({color:0xffffff,metalness:.95,roughness:.28});
  const mesh=new THREE.InstancedMesh(geo,mat,max);mesh.castShadow=true;mesh.receiveShadow=true;const d=new THREE.Object3D();const col=new THREE.Color();
  const bands=[];mesh.userData={bands,h,set(x){for(let i=0;i<max;i++){const full=Math.floor(x);let sy=0;if(i<full)sy=h*.94;else if(i===full)sy=h*.94*(x-full);
        d.position.set(0,i*h+(sy||.001)/2,0);d.rotation.y=i*.35;d.scale.set(1,Math.max(.0001,sy),1);d.updateMatrix();mesh.setMatrixAt(i,d.matrix);
        let c=0xf3be3a;for(const b of bands){if(i>=b[0])c=b[1];}col.setHex(c);mesh.setColorAt(i,col);}mesh.instanceMatrix.needsUpdate=true;mesh.instanceColor.needsUpdate=true;}};
  mesh.userData.set(0);return mesh;}
// ---- moneta che cade ----
export function fallCoin(m){const g=new THREE.Mesh(new THREE.CylinderGeometry(.5,.5,.09,28),new THREE.MeshStandardMaterial({color:0xf3be3a,metalness:1,roughness:.25}));g.castShadow=true;return g;}
// ---- chiave d'oro ----
export function key(m){const g=new THREE.Group();const ring=new THREE.Mesh(new THREE.TorusGeometry(.38,.1,14,32),m.gold);ring.position.y=.9;g.add(ring);
  const sh=new THREE.Mesh(new THREE.CylinderGeometry(.09,.09,1.4,14),m.gold);sh.position.y=0;g.add(sh);[.25,.05,-.15].forEach((y,i)=>{const t=new THREE.Mesh(new THREE.BoxGeometry(.36-i*.06,.12,.1),m.gold);t.position.set(.2,y-.35,0);g.add(t);});g.traverse(o=>{o.castShadow=true;});return g;}
