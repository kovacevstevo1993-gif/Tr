// Oggetti 3D dello short 003 (MANOVRA 2027): palette chiara "luce del giorno" (menta, crema, verde acqua, corallo, sole, blu notte)
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet};
export const C={teal:0x1f9d8a,coral:0xff6b4a,sun:0xffc233,navy:0x17324d,cream:0xfaf4e6,mint:0xdff2ee,white:0xffffff,ink:'#17324d'};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.45,metalness:.05},o));
export function mats(){return {teal:M(C.teal,{roughness:.35,metalness:.25}),tealD:M(0x14705f,{roughness:.4}),coral:M(C.coral,{roughness:.4}),sun:M(C.sun,{roughness:.35,emissive:0x7a5200,emissiveIntensity:.25}),navy:M(C.navy,{roughness:.5}),
  cream:M(C.cream,{roughness:.8}),white:M(0xffffff,{roughness:.55}),chrome:M(0xe4e8ec,{metalness:1,roughness:.18}),tyre:M(0x1b1f26,{roughness:.8}),glass:M(0xbfe6ff,{roughness:.05,metalness:.2,transparent:true,opacity:.65}),
  gold:M(0xffc233,{metalness:1,roughness:.3}),stone:M(0xe2cfa6,{roughness:.6}),roof:M(0x9aa6b2,{roughness:.6}),green:M(0x25b36a,{roughness:.4,emissive:0x0a5a30,emissiveIntensity:.3})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// auto (davanti = +x), lunga ~3.4
export function car(m,body=m.teal){const g=new THREE.Group();
  add(g,rbox(3.4,.8,1.55,.22,body),0,.62,0);
  add(g,rbox(1.9,.7,1.38,.28,body),-.15,1.2,0);
  add(g,rbox(1.5,.5,1.42,.2,m.glass),-.12,1.25,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.04,.62,1.46),body),-.1,1.25,0);
  [[1.05,-.78],[1.05,.78],[-1.05,-.78],[-1.05,.78]].forEach(([x,z])=>{const w=add(g,new THREE.Mesh(new THREE.CylinderGeometry(.36,.36,.3,28),m.tyre),x,.36,z);w.rotation.x=Math.PI/2;
    const h=add(g,new THREE.Mesh(new THREE.CylinderGeometry(.19,.19,.32,20),m.chrome),x,.36,z);h.rotation.x=Math.PI/2;});
  [-.5,.5].forEach(z=>add(g,new THREE.Mesh(new THREE.SphereGeometry(.14,16,12),new THREE.MeshStandardMaterial({color:0xfff3c4,emissive:0xffe08a,emissiveIntensity:1.0})),1.68,.7,z*.9));
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.06,.18,.5),m.chrome),1.72,.42,0);
  return g;}
export function moto(m){const g=new THREE.Group();
  [-.85,.85].forEach(x=>{const w=add(g,new THREE.Mesh(new THREE.TorusGeometry(.42,.09,12,32),m.tyre),x,.5,0);add(g,new THREE.Mesh(new THREE.CylinderGeometry(.08,.08,.2,10),m.chrome),x,.5,0).rotation.x=Math.PI/2;});
  add(g,rbox(1.3,.4,.4,.15,m.coral),0,.95,0);add(g,rbox(.8,.18,.42,.07,m.navy),-.2,1.22,0);add(g,new THREE.Mesh(new THREE.CylinderGeometry(.04,.04,.9,8),m.chrome),.8,.95,0).rotation.z=-.4;
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.04,.04,.6,8),m.chrome),.95,1.4,0).rotation.x=Math.PI/2;return g;}
// libretto (carta di circolazione) con campo P.2
export function libretto(){const W=720,H=500;const mesh=sheet((g,w,h)=>{g.fillStyle='#e9f1f7';g.fillRect(0,0,w,h);g.fillStyle='#2b5aa8';g.fillRect(0,0,w,74);g.fillStyle='#fff';g.font='bold 34px PM';g.textAlign='left';g.textBaseline='middle';g.fillText('CARTA DI CIRCOLAZIONE',26,38);
  g.fillStyle='#17324d';g.font='bold 30px PM';const rows=[['A','TARGA','AA 000 AA'],['D.1','MARCA','——————'],['J','CATEGORIA','——————']];rows.forEach((r,i)=>{g.fillStyle='#8aa0b6';g.fillText(r[0],26,120+i*52);g.fillStyle='#17324d';g.fillText(r[1],110,120+i*52);g.fillStyle='#8aa0b6';g.fillText(r[2],360,120+i*52);});
  g.fillStyle='#8aa0b6';g.fillText('P.1',26,300);g.fillText('CILINDRATA',110,300);g.fillText('——————',360,300);
  g.fillStyle='#17324d';g.fillText('P.2',26,360);g.fillText('POTENZA kW',110,360);g.fillStyle='#17324d';g.font='bold 40px PM';g.fillText('—',560,360);
  g.fillStyle='#8aa0b6';g.font='bold 30px PM';g.fillText('Q',26,420);g.fillText('KW/KG',110,420);g.fillText('——————',360,420);g.strokeStyle='#2b5aa8';g.lineWidth=8;g.strokeRect(4,4,w-8,h-8);},W,H,3.0,null);
  const hl=new THREE.Mesh(new THREE.PlaneGeometry(2.72,.34),new THREE.MeshBasicMaterial({color:C.coral,transparent:true,opacity:.0}));hl.position.set(0,-.3,.03);mesh.add(hl);mesh.userData.hl=hl;
  return mesh;}
export function magnifier(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.TorusGeometry(.62,.1,16,40),m.navy),0,0,0);const gl=add(g,new THREE.Mesh(new THREE.CircleGeometry(.58,40),new THREE.MeshStandardMaterial({color:0xffffff,transparent:true,opacity:.18,roughness:0})),0,0,0);gl.castShadow=false;
  const h=add(g,new THREE.Mesh(new THREE.CylinderGeometry(.1,.13,.95,14),m.navy),.62,-.62,0);h.rotation.z=Math.PI/4;return g;}
export function parliament(m){const g=new THREE.Group();const stepM=M(0x2b4a6b,{roughness:.55}),ped=M(0xe8956e,{roughness:.5});
  for(let i=0;i<3;i++)add(g,new THREE.Mesh(new THREE.BoxGeometry(5.2-i*.3,.22,2.6-i*.2),stepM),0,.11+i*.22,0);
  for(let i=0;i<6;i++)add(g,new THREE.Mesh(new THREE.CylinderGeometry(.19,.21,2.0,18),m.white),-2.05+i*.82,1.65,.5);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(5.0,.25,2.2),m.white),0,2.78,0);
  const sh=new THREE.Shape();sh.moveTo(-2.6,0);sh.lineTo(2.6,0);sh.lineTo(0,1.15);sh.closePath();const pg=new THREE.ExtrudeGeometry(sh,{depth:2.0,bevelEnabled:false});pg.translate(0,0,-1.0);add(g,new THREE.Mesh(pg,ped),0,2.9,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.9,1.5,.12),m.navy),0,1.0,1.02);
  add(g,new THREE.Mesh(new THREE.SphereGeometry(.22,16,16),m.sun),0,3.75,.9);
  return g;}
export function piggy(m){const g=new THREE.Group();
  const b=add(g,new THREE.Mesh(new THREE.SphereGeometry(1,40,32),m.coral),0,1.0,0);b.scale.set(1.25,1.0,1.0);
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.35,.38,.4,24),m.coral),1.25,.95,0).rotation.z=Math.PI/2;
  [-.1,.1].forEach(z=>add(g,new THREE.Mesh(new THREE.SphereGeometry(.05,10,8),m.navy),1.46,.97,z*2));
  [-.5,.5].forEach(z=>{const e=add(g,new THREE.Mesh(new THREE.ConeGeometry(.26,.4,4),m.coral),.7,1.8,z);e.rotation.z=-.3;});
  [[-.6,-.45],[-.6,.45],[.6,-.45],[.6,.45]].forEach(([x,z])=>add(g,new THREE.Mesh(new THREE.CylinderGeometry(.18,.2,.5,14),m.coral),x,.28,z));
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.6,.05,.1),m.navy),-.1,1.99,0);
  const tail=add(g,new THREE.Mesh(new THREE.TorusGeometry(.2,.05,8,16,Math.PI*1.5),m.coral),-1.25,1.2,0);
  return g;}
export function coin(m){const c=new THREE.Mesh(new THREE.CylinderGeometry(.3,.3,.07,28),m.gold);c.rotation.x=Math.PI/2;c.castShadow=true;return c;}
export function medbag(m){const g=new THREE.Group();
  add(g,rbox(2.0,1.5,.7,.2,m.white),0,.75,0);add(g,new THREE.Mesh(new THREE.BoxGeometry(.9,.26,.06),m.green),0,.8,.37);add(g,new THREE.Mesh(new THREE.BoxGeometry(.26,.9,.06),m.green),0,.8,.37);
  add(g,new THREE.Mesh(new THREE.TorusGeometry(.4,.07,10,24,Math.PI),m.navy),0,1.5,0);return g;}
export function bubble(m){const g=new THREE.Group();add(g,rbox(2.6,1.5,.3,.35,m.white),0,0,0);const t=add(g,new THREE.Mesh(new THREE.ConeGeometry(.28,.5,3),m.white),-.7,-.95,0);t.rotation.z=Math.PI;return g;}
// bandierina/barra scaglione: barra orizzontale lunga che cresce
export function bar(m,color){return new THREE.Mesh(new THREE.BoxGeometry(1,.5,.7),color);}
export function dust(n=200,color=0xffffff,size=.07){const pos=new Float32Array(n*3);const p=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.BufferAttribute(pos,3)),new THREE.PointsMaterial({color,size,transparent:true,opacity:1,depthWrite:false}));
  p.userData.update=(t0,t,ox,oy,oz,spread=1.4)=>{const u=t-t0;const a=p.geometry.attributes.position.array;p.visible=u>0&&u<1.8;for(let i=0;i<n;i++){const r1=rnd(i),r2=rnd(i+7),r3=rnd(i+13);
      a[i*3]=ox+(r1-.5)*spread*(1+u);a[i*3+1]=oy+(r2-.4)*spread*.8+u*(.5+r3*1.4);a[i*3+2]=oz+(r3-.5)*.8;}p.geometry.attributes.position.needsUpdate=true;p.material.opacity=clamp(1-u/1.7);};return p;}
export const THEME={bg:0x9fdfd2,fogN:30,fogF:80,keyC:0xfff2dc,keyI:380,rimC:0x2ec4b6,rimI:70,hemiS:0xffffff,hemiG:0xe8dcc0,hemiI:.75,floor:0xf3e9d0,fR:.85,fM:0,ring:0x1f9d8a,ringK:1.6,env:.8,expo:.86,bloom:.04,flashK:.1,dustC:0xffffff,dustO:.7};
export {THREE,clamp,prog,eo,eio,eb,rnd};
