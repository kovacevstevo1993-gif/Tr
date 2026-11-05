// Spiaggia RICCA (short 009 v2): barche a vela, gabbiani, faro, lampioni, bandierine, ombrelloni, granchio, pallone, persone lontane,
// ciclo del giorno (mattina -> tramonto) e NUMERI 3D veri (font extruso). Tutto PBR con ombre.
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import * as S9 from '/code/lib/s009.js';
import {FontLoader} from 'three/addons/loaders/FontLoader.js';
import {TextGeometry} from 'three/addons/geometries/TextGeometry.js';
export * from '/code/lib/s009.js';
export {THREE,clamp,prog,eo,eio,eb,rnd};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.6,metalness:.02},o));
const cvs=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return [c,c.getContext('2d')];};
const tex=(c)=>{const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;return t;};
export const THEME=Object.assign({},S9.THEME);
let FONT=null;export async function loadFont(){if(!FONT)FONT=await new FontLoader().loadAsync('/code/lib/three/fonts/helvetiker_bold.typeface.json');return FONT;}
// numero/scritta 3D (oro, bisello): centrata
export function num3d(text,{size=1,depth=.35,mat=null,color=0xf3be3a,rough=.22}={}){const g=new TextGeometry(text,{font:FONT,size,depth,curveSegments:10,bevelEnabled:true,bevelThickness:size*.05,bevelSize:size*.035,bevelSegments:4});g.computeBoundingBox();const bb=g.boundingBox;g.translate(-(bb.max.x+bb.min.x)/2,-(bb.max.y+bb.min.y)/2,-(bb.max.z+bb.min.z)/2);
  const m=new THREE.Mesh(g,mat||new THREE.MeshStandardMaterial({color,metalness:1,roughness:rough}));m.castShadow=true;m.receiveShadow=true;const grp=new THREE.Group();grp.add(m);grp.userData.w=bb.max.x-bb.min.x;grp.userData.h=bb.max.y-bb.min.y;return grp;}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// ---------------- ambiente ricco ----------------
export function extras(scene,m){const U=scene.userData;
  // barche a vela
  const boat=(x,z,s,col)=>{const g=new THREE.Group();const hs=new THREE.Shape();hs.moveTo(-1.6,0);hs.lineTo(1.6,0);hs.quadraticCurveTo(1.2,-.7,.4,-.8);hs.lineTo(-.9,-.8);hs.quadraticCurveTo(-1.4,-.5,-1.6,0);
    const hull=new THREE.Mesh(new THREE.ExtrudeGeometry(hs,{depth:.8,bevelEnabled:false}),M(0xf4efe4,{roughness:.5}));hull.position.z=-.4;hull.castShadow=true;g.add(hull);
    const stripe=new THREE.Mesh(new THREE.BoxGeometry(3.2,.12,.82),M(col));stripe.position.set(0,-.05,0);g.add(stripe);
    const mast=new THREE.Mesh(new THREE.CylinderGeometry(.04,.05,4.2,8),M(0xcfc6b0));mast.position.set(0,2.0,0);mast.castShadow=true;g.add(mast);
    const sailG=new THREE.BufferGeometry();sailG.setAttribute('position',new THREE.Float32BufferAttribute([0,.3,0, 0,4.0,0, -1.6,.5,0],3));sailG.computeVertexNormals();const sail=new THREE.Mesh(sailG,M(0xffffff,{roughness:.8,side:THREE.DoubleSide}));sail.castShadow=true;g.add(sail);
    const jG=new THREE.BufferGeometry();jG.setAttribute('position',new THREE.Float32BufferAttribute([.1,.3,0, .1,3.4,0, 1.5,.4,0],3));jG.computeVertexNormals();const jib=new THREE.Mesh(jG,M(col,{roughness:.8,side:THREE.DoubleSide}));jib.castShadow=true;g.add(jib);
    g.scale.setScalar(s);g.position.set(x,.05,z);scene.add(g);return g;};
  U.boats=[boat(-10,-30,1.4,0xff6b57),boat(14,-38,1.1,0x1fb8c4),boat(2,-50,.8,0xf3be3a)];
  // gabbiani
  const gull=()=>{const g=new THREE.Group();const b=new THREE.Mesh(new THREE.SphereGeometry(.25,12,8),M(0xffffff));b.scale.set(1.8,.7,.7);g.add(b);
    const wg=new THREE.PlaneGeometry(1.1,.35);[-1,1].forEach(sd=>{const w=new THREE.Group();const wm=new THREE.Mesh(wg,M(0xf2f2f2,{side:THREE.DoubleSide}));wm.position.x=sd*.55;w.add(wm);g.add(w);w.userData.sd=sd;});g.userData.wings=g.children.filter(o=>o!==b);return g;};
  U.gulls=[];for(let i=0;i<7;i++){const g=gull();g.userData.c=[-8+rnd(i)*16,9+rnd(i+3)*5,-14-rnd(i+5)*14];g.userData.r=3+rnd(i+7)*5;g.userData.sp=.25+rnd(i+9)*.2;g.userData.ph=rnd(i+11)*6.28;scene.add(g);U.gulls.push(g);}
  // faro a righe
  const [lc,lg]=cvs(64,256);for(let i=0;i<8;i++){lg.fillStyle=i%2?'#ffffff':'#d8322a';lg.fillRect(0,i*32,64,32);}
  const lh=new THREE.Group();lh.add(Object.assign(new THREE.Mesh(new THREE.CylinderGeometry(.8,1.3,7,24),new THREE.MeshStandardMaterial({map:tex(lc),roughness:.6})),{castShadow:true,position:new THREE.Vector3(0,3.5,0)}));
  const lamp=new THREE.Mesh(new THREE.CylinderGeometry(.55,.55,.9,16),M(0xffe9a0,{emissive:0xffd060,emissiveIntensity:1.4}));lamp.position.y=7.45;lh.add(lamp);const roof=new THREE.Mesh(new THREE.ConeGeometry(.9,.8,20),M(0x2a2f36));roof.position.y=8.3;lh.add(roof);
  const [bc,bg2]=cvs(256,64);const gr=bg2.createLinearGradient(0,0,256,0);gr.addColorStop(0,'rgba(255,230,150,.95)');gr.addColorStop(1,'rgba(255,230,150,0)');bg2.fillStyle=gr;bg2.fillRect(0,0,256,64);
  const beam=new THREE.Mesh(new THREE.PlaneGeometry(14,2.2),new THREE.MeshBasicMaterial({map:tex(bc),transparent:true,blending:THREE.AdditiveBlending,depthWrite:false,fog:false,side:THREE.DoubleSide}));beam.position.set(7,7.45,0);const bp=new THREE.Group();bp.add(beam);bp.position.y=0;lh.add(bp);U.beam=bp;
  lh.position.set(-17,0,-24);scene.add(lh);U.lamp=lamp;
  // lampioni lungo la passerella + bandierine
  U.bulbs=[];for(let i=0;i<7;i++)[-1].forEach(()=>{[-1.9,1.9].forEach(x=>{if(i%2)return;const g=new THREE.Group();const po=new THREE.Mesh(new THREE.CylinderGeometry(.05,.07,2.6,10),M(0x2a2f36,{metalness:.6,roughness:.4}));po.position.y=1.3;po.castShadow=true;g.add(po);
    const arm=new THREE.Mesh(new THREE.BoxGeometry(.5,.05,.05),M(0x2a2f36));arm.position.set(-x*.12,2.55,0);g.add(arm);const bulb=new THREE.Mesh(new THREE.SphereGeometry(.16,14,10),M(0xfff0c0,{emissive:0xffcf70,emissiveIntensity:.2}));bulb.position.set(-x*.3,2.4,0);g.add(bulb);U.bulbs.push(bulb);
    g.position.set(x,0,8-i*2.3);scene.add(g);});});
  const FL=[0xff6b57,0xf3be3a,0x1fb8c4,0xffffff,0x7ad66f];const nF=2*13*5;const fg=new THREE.InstancedMesh(new THREE.ConeGeometry(.12,.3,3),M(0xffffff,{roughness:.8,side:THREE.DoubleSide}),nF);fg.castShadow=true;U.flags=fg;U.flagDef=[];
  let q=0;[-1.9,1.9].forEach(x=>{for(let sp=0;sp<13;sp++)for(let k=0;k<5;k++){const z=8.6-sp*1.9-k*.38;U.flagDef.push([x,z,sp+k]);fg.setColorAt(q,new THREE.Color(FL[(sp+k)%5]));q++;}});scene.add(fg);
  // ombrelloni con asciugamani, tavolo, sdraio, tavola da surf, secchiello e castello
  const [uc,ug]=cvs(256,64);for(let i=0;i<8;i++){ug.fillStyle=i%2?'#ffffff':'#ff6b57';ug.fillRect(i*32,0,32,64);}const umbTex=tex(uc);
  const umb=(x,z,ry,col)=>{const g=new THREE.Group();const po=new THREE.Mesh(new THREE.CylinderGeometry(.04,.04,2.8,8),M(0xd9c7a8));po.position.y=1.4;po.rotation.z=.12;po.castShadow=true;g.add(po);
    const top=new THREE.Mesh(new THREE.ConeGeometry(1.5,.55,16),new THREE.MeshStandardMaterial({map:umbTex,roughness:.75,side:THREE.DoubleSide}));top.position.set(-.16,2.85,0);top.castShadow=true;g.add(top);
    const [tc,tg]=cvs(128,256);tg.fillStyle=col;tg.fillRect(0,0,128,256);for(let i=0;i<6;i++){tg.fillStyle='rgba(255,255,255,.7)';tg.fillRect(0,i*42,128,12);}
    const tw=new THREE.Mesh(new THREE.PlaneGeometry(1.1,2.1),new THREE.MeshStandardMaterial({map:tex(tc),roughness:.9,side:THREE.DoubleSide}));tw.rotation.x=-Math.PI/2;tw.position.set(.3,.035,.8);tw.receiveShadow=true;g.add(tw);
    g.position.set(x,0,z);g.rotation.y=ry;scene.add(g);return g;};
  umb(6.2,-1.5,.4,'#1fb8c4');umb(-6.8,.8,-.5,'#f3be3a');umb(9.5,2.5,.2,'#ff6b57');umb(-9.8,-3.5,-.3,'#7ad66f');
  const surf=(x,z,col)=>{const g=new THREE.Mesh(new THREE.CapsuleGeometry(.26,2.4,6,14),M(col,{roughness:.35,metalness:.1}));g.scale.set(1,1,.18);g.position.set(x,1.35,z);g.rotation.z=.08;g.castShadow=true;scene.add(g);};surf(4.8,-3.3,0xffffff);surf(5.3,-3.2,0xf3be3a);
  const castle=new THREE.Group();[[0,0,.75,.55],[.9,.1,.5,.4],[-.8,.1,.55,.45]].forEach(([x,z,r,h])=>{const c=new THREE.Mesh(new THREE.CylinderGeometry(r*.7,r,h*1.6,16),M(0xdcbf86,{roughness:1}));c.position.set(x,h*.8,z);c.castShadow=true;castle.add(c);const t=new THREE.Mesh(new THREE.ConeGeometry(r*.4,.4,12),M(0xff6b57));t.position.set(x,h*1.6+.2,z);castle.add(t);});castle.position.set(-5.2,0,3.4);scene.add(castle);
  // pallone che rimbalza
  const ball=new THREE.Mesh(new THREE.SphereGeometry(.36,24,16),new THREE.MeshStandardMaterial({map:(()=>{const [c,g]=cvs(256,128);for(let i=0;i<6;i++){g.fillStyle=['#ff6b57','#fff','#1fb8c4','#f3be3a','#fff','#7ad66f'][i];g.fillRect(i*43,0,43,128);}return tex(c);})(),roughness:.4}));ball.castShadow=true;scene.add(ball);U.ball=ball;
  // granchio
  const crab=new THREE.Group();const cb=new THREE.Mesh(new THREE.SphereGeometry(.2,14,10),M(0xe4573d));cb.scale.set(1.4,.6,1);crab.add(cb);[-1,1].forEach(sd=>{const cl=new THREE.Mesh(new THREE.SphereGeometry(.09,10,8),M(0xe4573d));cl.position.set(sd*.34,.04,.18);crab.add(cl);for(let k=0;k<3;k++){const lg2=new THREE.Mesh(new THREE.CylinderGeometry(.015,.015,.28,6),M(0xc2412a));lg2.position.set(sd*.28,-.02,-.1+k*.1);lg2.rotation.z=sd*1.0;crab.add(lg2);}
    [-1,1].forEach(e=>{const ey=new THREE.Mesh(new THREE.SphereGeometry(.035,8,6),M(0x111111));ey.position.set(e*.09,.13,.2);crab.add(ey);});});crab.traverse(o=>o.castShadow=true);scene.add(crab);U.crab=crab;
  // persone lontane (silhouette 3D semplici)
  U.walkers=[];[[0x1d5560,.2],[0xd9693a,.35],[0x7a4a8a,.5],[0x1d5560,.65]].forEach(([col,ph],i)=>{const g=new THREE.Group();const body=new THREE.Mesh(new THREE.CapsuleGeometry(.14,.7,4,10),M(col));body.position.y=.75;body.castShadow=true;g.add(body);const hd=new THREE.Mesh(new THREE.SphereGeometry(.14,12,10),M(0xe8b88a));hd.position.y=1.38;g.add(hd);g.userData.ph=ph;g.userData.z=-15.5-i*1.1;scene.add(g);U.walkers.push(g);});
  // rocce vicino al mare e sabbia bagnata
  for(let i=0;i<7;i++){const r=new THREE.Mesh(new THREE.DodecahedronGeometry(.5+rnd(i)*.7,0),M(0x7a746c,{roughness:.95}));r.position.set(-14+i*4.6+rnd(i+4)*2,.2,-19.5-rnd(i+9)*1.2);r.scale.y=.6;r.castShadow=true;scene.add(r);}
  const wet=new THREE.Mesh(new THREE.PlaneGeometry(90,3.2),new THREE.MeshStandardMaterial({color:0xb99a63,roughness:.15,metalness:.35}));wet.rotation.x=-Math.PI/2;wet.position.set(0,.03,-20);scene.add(wet);
}
// ciclo del giorno: u = 0 mattina ... 1 tramonto
const L=(a,b,u)=>new THREE.Color(a).lerp(new THREE.Color(b),u);
export function setDay(scene,st,u){u=clamp(u);const K=scene.userData.skyCtx;if(K){const g=K.g;const top=L(0x1f78cc,0x2a3b78,u),mid=L(0x7fc4ee,0xd8758a,u),low=L(0xfff0c8,0xffb066,u),hz=L(0xffe6b0,0xff8a4c,u);
    const gr=g.createLinearGradient(0,0,0,256);gr.addColorStop(0,'#'+top.getHexString());gr.addColorStop(.5,'#'+mid.getHexString());gr.addColorStop(.82,'#'+low.getHexString());gr.addColorStop(1,'#'+hz.getHexString());g.fillStyle=gr;g.fillRect(0,0,16,256);K.tex.needsUpdate=true;}
  const sun=scene.userData.sun,glow=scene.userData.glow;const sx=-12+u*32,sy=26-u*23;if(sun){sun.position.set(sx,sy,-62);sun.material.color.set(L(0xfff6d8,0xffb55a,u));}if(glow){glow.position.set(sx,sy,-62);glow.scale.setScalar(30+u*22);}
  st.key.color.copy(L(0xfff3de,0xff9a58,u));st.key.intensity=330-60*u;st.rim.color.copy(L(0x8fd4ff,0xff7a9a,u));
  const bg=L(0xcfe8f2,0xf0a77d,u);scene.background=bg;scene.fog.color.copy(bg);
  const sea=scene.userData.sea;if(sea)sea.material.color.copy(L(0x1fb3c9,0x2a7f9a,u*.9));
  (scene.userData.bulbs||[]).forEach(b=>{b.material.emissiveIntensity=.2+3.2*clamp((u-.55)/.45);});if(scene.userData.lamp)scene.userData.lamp.material.emissiveIntensity=.6+2.4*clamp((u-.4)/.6);
  scene.userData.dayU=u;}
// movimento di tutto l'ambiente
export function liveBeach(scene,t){const U=scene.userData;S9.moveBeach(scene,t);
  (U.boats||[]).forEach((b,i)=>{b.position.x=((-10+i*14+t*(.4+i*.12)+40)%80)-40;b.position.y=.05+Math.sin(t*1.1+i*2)*.12;b.rotation.z=Math.sin(t*.9+i)*.05;b.rotation.y=.12*Math.sin(t*.3+i);});
  (U.gulls||[]).forEach(g=>{const a=t*g.userData.sp+g.userData.ph;g.position.set(g.userData.c[0]+Math.cos(a)*g.userData.r,g.userData.c[1]+Math.sin(a*2)*.6,g.userData.c[2]+Math.sin(a)*g.userData.r*.5);g.rotation.y=-a+Math.PI/2;g.rotation.z=Math.cos(a)*.25;g.userData.wings.forEach(w=>{w.rotation.z=w.userData.sd*Math.sin(t*9+g.userData.ph)*.7;});});
  if(U.beam)U.beam.rotation.y=t*1.2;
  if(U.flags){const d=new THREE.Object3D();U.flagDef.forEach(([x,z,k],i)=>{const sag=-.34*Math.sin(((z+10)%1.9)/1.9*Math.PI)*0;d.position.set(x,1.28-.25*Math.abs(Math.sin((z*.5)*Math.PI)),z);d.rotation.set(Math.PI,0,Math.sin(t*3+k)*.35);d.scale.set(1,1,1);d.updateMatrix();U.flags.setMatrixAt(i,d.matrix);});U.flags.instanceMatrix.needsUpdate=true;}
  if(U.ball){const ph=(t*1.1)%1;U.ball.position.set(8.2+Math.sin(t*.4)*1.4,.36+Math.abs(Math.sin(ph*Math.PI))*1.9,-5.2);U.ball.rotation.set(t*2,t*1.3,0);}
  if(U.crab){U.crab.position.set(3.6+Math.sin(t*.5)*1.6,.15,2.2+Math.sin(t*.9)*.15);U.crab.rotation.y=Math.PI/2*Math.sign(Math.cos(t*.5)||1);U.crab.children.forEach((c,i)=>{if(i>0)c.rotation.x=Math.sin(t*12+i)*.12;});}
  (U.walkers||[]).forEach((w,i)=>{w.position.set(((t*.5*(i%2?1:-1)+w.userData.ph*60+40)%80)-40,Math.abs(Math.sin(t*6+i))*.05,w.userData.z);w.rotation.y=(i%2?1:-1)*Math.PI/2;});}
