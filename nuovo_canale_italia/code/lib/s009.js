// Oggetti 3D dello short 009 (PENSIONE DAL 2027): look NUOVO "spiaggia al tramonto"
// sabbia, mare turchese animato, cielo pesca/azzurro, passerella di legno verso la sdraio, cartelli con gli anni, clessidra, orologio
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export {makeAnchor} from '/code/lib/s006.js';
export {check,cross,stamp,heart} from '/code/lib/s008.js';
export const THEME={bg:0xcfe8f2,fogN:34,fogF:110,keyC:0xffddae,keyI:330,rimC:0x7fd4ff,rimI:35,hemiS:0xcfeaff,hemiG:0xe4c995,hemiI:.62,floor:0xe3c68c,fR:.95,fM:0,ring:0xffffff,ringK:0,env:.6,expo:.78,bloom:.16,flashK:.3,dustC:0xfff1d0,dustO:.22};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.6,metalness:.02},o));
export function mats(){return {wood:M(0xa8703c,{roughness:.7}),woodD:M(0x6b4423,{roughness:.75}),woodL:M(0xcf9a5e,{roughness:.7}),sand:M(0xe3c68c,{roughness:.95}),gold:M(0xf3be3a,{metalness:1,roughness:.25}),chrome:M(0xe3e8ee,{metalness:1,roughness:.2}),
  coral:M(0xff6b57,{roughness:.45}),teal:M(0x1fb8c4,{roughness:.4}),cream:M(0xf6ecd6,{roughness:.8}),white:M(0xffffff,{roughness:.5}),leaf:M(0x2f9a52,{roughness:.8,side:THREE.DoubleSide}),leafD:M(0x1f7a3f,{roughness:.8,side:THREE.DoubleSide}),
  glass:new THREE.MeshStandardMaterial({color:0xdff6ff,transparent:true,opacity:.28,roughness:.05,metalness:.1,side:THREE.DoubleSide,depthWrite:false}),sandG:M(0xf0c36a,{roughness:.9}),red:M(0xe5392b,{roughness:.5}),yellow:M(0xffc928,{roughness:.45}),dark:M(0x23262c,{roughness:.5,metalness:.3}),navy:M(0x12303a,{roughness:.5})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
const cvs=(w,h)=>{const c=document.createElement('canvas');c.width=w;c.height=h;return [c,c.getContext('2d')];};
const tex=(c)=>{const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;return t;};
// ---------------- spiaggia ----------------
export function beach(scene,m){
  // cielo (sfumatura) + sole
  const [sc,sg]=cvs(16,256);const gr=sg.createLinearGradient(0,0,0,256);gr.addColorStop(0,'#1f6fbf');gr.addColorStop(.5,'#5fb0e8');gr.addColorStop(.82,'#ffcf9a');gr.addColorStop(1,'#ff9f6e');sg.fillStyle=gr;sg.fillRect(0,0,16,256);
  const skyTex=tex(sc);const sky=new THREE.Mesh(new THREE.PlaneGeometry(260,90),new THREE.MeshBasicMaterial({map:skyTex,fog:false}));sky.position.set(0,32,-70);scene.add(sky);scene.userData.skyCtx={g:sg,tex:skyTex};
  const sun=new THREE.Mesh(new THREE.SphereGeometry(4,32,24),new THREE.MeshBasicMaterial({color:0xfff2c8,fog:false}));sun.position.set(14,10,-62);scene.add(sun);scene.userData.sun=sun;
  const [gc,gg]=cvs(256,256);const rg=gg.createRadialGradient(128,128,4,128,128,128);rg.addColorStop(0,'rgba(255,240,190,.9)');rg.addColorStop(1,'rgba(255,200,120,0)');gg.fillStyle=rg;gg.fillRect(0,0,256,256);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:tex(gc),transparent:true,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));glow.scale.set(34,34,1);glow.position.copy(sun.position);scene.add(glow);scene.userData.glow=glow;
  // nuvole
  const cl=[];for(let i=0;i<8;i++){const g=new THREE.Group();for(let k=0;k<5;k++){const s=new THREE.Mesh(new THREE.SphereGeometry(1.6+rnd(i*5+k)*1.2,16,12),new THREE.MeshBasicMaterial({color:0xffffff,fog:false,transparent:true,opacity:.92}));s.scale.y=.55;s.position.set(k*1.9-3.5,rnd(k+i)*.6,0);g.add(s);}g.position.set(-50+i*13,18+rnd(i+9)*9,-58);g.userData.sp=.2+rnd(i)*.2;scene.add(g);cl.push(g);}scene.userData.clouds=cl;
  // sabbia con grana
  const [dc,dg]=cvs(512,512);dg.fillStyle='#e6c88e';dg.fillRect(0,0,512,512);for(let i=0;i<5200;i++){const v=rnd(i)*40-20;dg.fillStyle=`rgba(${v>0?255:120},${v>0?240:90},${v>0?200:40},.07)`;dg.fillRect(rnd(i+3)*512,rnd(i+7)*512,2+rnd(i+11)*3,2);}
  for(let i=0;i<14;i++){dg.strokeStyle='rgba(150,110,50,.08)';dg.lineWidth=6;dg.beginPath();const y=i*38+10;dg.moveTo(0,y);dg.bezierCurveTo(150,y+14,330,y-14,512,y);dg.stroke();}
  const st=tex(dc);st.wrapS=st.wrapT=THREE.RepeatWrapping;st.repeat.set(10,10);
  const sand=new THREE.Mesh(new THREE.PlaneGeometry(90,44),new THREE.MeshStandardMaterial({map:st,roughness:.95}));sand.rotation.x=-Math.PI/2;sand.position.set(0,.02,0);sand.receiveShadow=true;scene.add(sand);
  // mare animato
  const sg2=new THREE.PlaneGeometry(220,70,90,28);const sea=new THREE.Mesh(sg2,new THREE.MeshStandardMaterial({color:0x1fb3c9,roughness:.18,metalness:.25,transparent:true,opacity:.96}));sea.rotation.x=-Math.PI/2;sea.position.set(0,-.02,-56);scene.add(sea);scene.userData.sea=sea;
  const foam=new THREE.Mesh(new THREE.PlaneGeometry(90,1.4),new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.7}));foam.rotation.x=-Math.PI/2;foam.position.set(0,.03,-21.5);scene.add(foam);scene.userData.foam=foam;
  // passerella di legno verso la sdraio
  const pl=new THREE.InstancedMesh(new THREE.BoxGeometry(3.6,.1,.55),m.wood,40);const d=new THREE.Object3D();for(let i=0;i<40;i++){d.position.set(rnd(i)*.04,.07,10-i*.62);d.rotation.y=(rnd(i+3)-.5)*.02;d.scale.set(1,1,1);d.updateMatrix();pl.setMatrixAt(i,d.matrix);pl.setColorAt(i,new THREE.Color().setHSL(.07,.5,.30+rnd(i+5)*.12));}pl.castShadow=true;pl.receiveShadow=true;scene.add(pl);
  [[-1.9],[1.9]].forEach(([x])=>{const rl=new THREE.Mesh(new THREE.BoxGeometry(.12,.12,26),m.woodD);rl.position.set(x,.55,-3);rl.castShadow=true;scene.add(rl);for(let i=0;i<14;i++){const po=new THREE.Mesh(new THREE.CylinderGeometry(.07,.08,.62,10),m.woodD);po.position.set(x,.3,10-i*1.9);po.castShadow=true;scene.add(po);}});
  // palme
  const palm=(x,z,s,h)=>{const g=new THREE.Group();const tr=new THREE.Mesh(new THREE.CylinderGeometry(.18*s,.3*s,h,12),M(0x8a5a30,{roughness:.9}));tr.position.y=h/2;tr.rotation.z=.12*Math.sign(-x||1);tr.castShadow=true;g.add(tr);
    const lv=new THREE.Group();for(let i=0;i<9;i++){const l=new THREE.Mesh(new THREE.PlaneGeometry(.7*s,3.6*s,1,6),i%2?m.leaf:m.leafD);const p=l.geometry.attributes.position;for(let q=0;q<p.count;q++){const y=p.getY(q);p.setZ(q,-Math.pow((y+1.8*s)/(3.6*s),2)*1.2*s);}l.geometry.computeVertexNormals();l.position.y=0;l.rotation.set(-1.15,i/9*Math.PI*2,0,'YXZ');l.castShadow=true;const w=new THREE.Group();w.add(l);l.position.set(0,0,0);lv.add(w);}
    lv.position.set(Math.sign(-x||1)*h*.12,h,0);g.add(lv);g.userData.lv=lv;g.position.set(x,0,z);scene.add(g);return g;};
  scene.userData.palms=[palm(-7.5,-4,1.2,7),palm(8.5,-8,1.3,8),palm(-12,-12,1.4,9),palm(13,-3,1.0,6)];
  // sdraio + ombrellone in fondo (la meta)
  const g=new THREE.Group();const fr=add(g,new THREE.Mesh(new THREE.BoxGeometry(.9,.07,1.9),M(0xffffff,{roughness:.8})),0,.55,0);fr.rotation.x=-.28;
  const st2=add(g,new THREE.Mesh(new THREE.BoxGeometry(.9,.07,.9),M(0xff6b57,{roughness:.8})),0,.9,-.75);st2.rotation.x=.9;
  [[-.45,.5],[.45,.5]].forEach(([x,z])=>add(g,new THREE.Mesh(new THREE.BoxGeometry(.06,.9,.06),m.woodL),x,.3,.7));
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.05,.05,3.2,10),m.woodL),1.3,1.6,-.2);
  const um=new THREE.Mesh(new THREE.ConeGeometry(1.9,.7,8),M(0xff6b57,{roughness:.7,side:THREE.DoubleSide}));um.position.set(1.3,3.3,-.2);um.castShadow=true;g.add(um);
  g.position.set(.2,0,-10);g.rotation.y=.35;scene.add(g);scene.userData.chair=g;
}
export function moveBeach(scene,t){const sea=scene.userData.sea;if(sea){const p=sea.geometry.attributes.position;for(let i=0;i<p.count;i++){const x=p.getX(i),y=p.getY(i);p.setZ(i,Math.sin(x*.18+t*1.1)*.18+Math.sin(y*.3-t*.9)*.14+Math.sin((x+y)*.11+t*.6)*.12);}p.needsUpdate=true;sea.geometry.computeVertexNormals();}
  (scene.userData.clouds||[]).forEach((c,i)=>{c.position.x=((-50+i*13)+t*c.userData.sp*3+80)%160-80;});
  (scene.userData.palms||[]).forEach((pm,i)=>{const lv=pm.userData.lv;lv.rotation.z=Math.sin(t*.9+i)*.05;lv.rotation.x=Math.sin(t*.7+i*2)*.04;});
  const g=scene.userData.glow;if(g)g.material.opacity=.85+.1*Math.sin(t*1.3);
  const f=scene.userData.foam;if(f){f.position.z=-21.5+Math.sin(t*.8)*.7;f.material.opacity=.55+.2*Math.sin(t*1.6);}}
// ---------------- oggetti dei concetti ----------------
// cartello su palo con testo (anni / requisiti)
export function signPost(lines,{w=2.9,h=1.5,col='#f6ecd6',ink='#12303a',acc='#ff6b57'}={}){const g=new THREE.Group();
  const [c,x]=cvs(768,Math.round(768*h/w));x.fillStyle=col;x.beginPath();x.roundRect(8,8,752,c.height-16,40);x.fill();x.strokeStyle=acc;x.lineWidth=14;x.stroke();x.fillStyle=ink;x.textAlign='center';x.textBaseline='middle';
  lines.forEach((l,i)=>{let f=i===0?120:84;x.font='bold '+f+'px AB';while(x.measureText(l).width>690&&f>26){f-=4;x.font='bold '+f+'px AB';}x.fillStyle=i===0?acc:ink;x.fillText(l,384,c.height*((i+1)/(lines.length+1))+6);});
  const bd=new THREE.Mesh(new THREE.BoxGeometry(w,h,.14),[M(0x6b4423),M(0x6b4423),M(0x6b4423),M(0x6b4423),new THREE.MeshStandardMaterial({map:tex(c),roughness:.6}),M(0x6b4423)]);bd.position.y=h/2+1.2;bd.castShadow=true;g.add(bd);
  [[-w*.38],[w*.38]].forEach(([px])=>{const p=new THREE.Mesh(new THREE.CylinderGeometry(.09,.11,1.4+h*.4,10),M(0x6b4423));p.position.set(px,.7,-.1);p.castShadow=true;g.add(p);});g.userData.board=bd;return g;}
// orologio grande con lancette (set(angolo minuti) ruota)
export function bigClock(m,r=1.5){const g=new THREE.Group();const [c,x]=cvs(512,512);x.fillStyle='#fffaf0';x.beginPath();x.arc(256,256,250,0,7);x.fill();x.strokeStyle='#12303a';x.lineWidth=14;x.stroke();
  for(let i=0;i<12;i++){const a=i/12*Math.PI*2;x.strokeStyle='#12303a';x.lineWidth=i%3?6:12;x.beginPath();x.moveTo(256+Math.sin(a)*205,256-Math.cos(a)*205);x.lineTo(256+Math.sin(a)*235,256-Math.cos(a)*235);x.stroke();}
  const face=new THREE.Mesh(new THREE.CircleGeometry(r,48),new THREE.MeshStandardMaterial({map:tex(c),roughness:.5}));g.add(face);
  const rim=new THREE.Mesh(new THREE.TorusGeometry(r,.1,16,56),m.gold);rim.castShadow=true;g.add(rim);
  const hand=(len,wd,col)=>{const p=new THREE.Group();const b=new THREE.Mesh(new THREE.BoxGeometry(wd,len,.05),M(col,{roughness:.4}));b.position.y=len/2-.1;b.castShadow=true;p.add(b);p.position.z=.07;g.add(p);return p;};
  const hh=hand(r*.55,.1,0x12303a),mh=hand(r*.8,.07,0xff6b57);g.userData.set=(min)=>{mh.rotation.z=-min/60*Math.PI*2;hh.rotation.z=-min/720*Math.PI*2;};g.userData.set(0);
  const cap=new THREE.Mesh(new THREE.CylinderGeometry(.09,.09,.12,16),m.gold);cap.rotation.x=Math.PI/2;cap.position.z=.1;g.add(cap);return g;}
// clessidra con sabbia (set(frazione caduta 0..1))
export function hourglass(m){const g=new THREE.Group();
  const prof=[[0.02,0],[.9,.05],[.9,.12],[.32,1.0],[.07,1.55],[.32,2.1],[.9,3.0],[.9,3.1],[.02,3.15]].map(([r,y])=>new THREE.Vector2(r,y));
  const gl=new THREE.Mesh(new THREE.LatheGeometry(prof,40),m.glass);gl.position.y=.15;g.add(gl);
  const topG=new THREE.ConeGeometry(.8,1.2,32);topG.rotateX(Math.PI);const top=new THREE.Mesh(topG,m.sandG);const bot=new THREE.Mesh(new THREE.ConeGeometry(.85,1,32),m.sandG);top.castShadow=bot.castShadow=true;g.add(top,bot);
  const stm=new THREE.Mesh(new THREE.CylinderGeometry(.025,.025,1.5,8),m.sandG);stm.position.y=1.0;g.add(stm);
  [0,3.3].forEach(y=>{const p=new THREE.Mesh(new THREE.CylinderGeometry(1.05,1.05,.16,36),m.woodL);p.position.y=y+.08;p.castShadow=true;g.add(p);});
  [[.95,0],[-.95,0],[0,.95],[0,-.95]].forEach(([x,z])=>{const r=new THREE.Mesh(new THREE.CylinderGeometry(.05,.05,3.2,10),m.woodD);r.position.set(x,1.7,z);g.add(r);});
  g.userData.set=(f)=>{f=clamp(f);const k=Math.max(.001,1-f);top.scale.set(k,k,k);top.position.y=1.82+1.2*k/2;const h2=Math.max(.001,f);bot.scale.set(.25+.75*h2,h2,.25+.75*h2);bot.position.y=.25+h2/2;stm.visible=f>.005&&f<.995;};
  g.userData.set(0);return g;}
// scala di anni: griglia di tessere (1 tessera = 1 anno), set(n) mostra n tessere piene piu una parziale
export function yearTiles(m,{cols=8,max=48,s=.34}={}){const geo=new THREE.BoxGeometry(s*.9,s*.9,s*.5);const mesh=new THREE.InstancedMesh(geo,new THREE.MeshStandardMaterial({color:0xffffff,roughness:.45,metalness:.1}),max);mesh.castShadow=true;mesh.receiveShadow=true;const d=new THREE.Object3D(),col=new THREE.Color();
  mesh.userData={set(x,c=0xf3be3a,c2=0xff6b57){for(let i=0;i<max;i++){const full=Math.floor(x);let k=0;if(i<full)k=1;else if(i===full)k=x-full;const r=Math.floor(i/cols),q=i%cols;d.position.set((q-(cols-1)/2)*s,(r)*s,0);d.scale.set(Math.max(.0001,k),Math.max(.0001,k),Math.max(.0001,k));d.updateMatrix();mesh.setMatrixAt(i,d.matrix);col.setHex(i===full&&x-full>0?c2:c);mesh.setColorAt(i,col);}mesh.instanceMatrix.needsUpdate=true;mesh.instanceColor.needsUpdate=true;}};
  mesh.userData.set(0);return mesh;}
// casco da lavoro (lavori gravosi)
export function hardHat(m){const g=new THREE.Group();const dome=new THREE.Mesh(new THREE.SphereGeometry(.9,32,20,0,Math.PI*2,0,Math.PI/2),m.yellow);dome.castShadow=true;g.add(dome);
  const br=new THREE.Mesh(new THREE.CylinderGeometry(1.1,1.1,.07,40),m.yellow);br.position.y=.02;br.castShadow=true;g.add(br);const vis=new THREE.Mesh(new THREE.CylinderGeometry(.55,.55,.06,24,1,false,-Math.PI/2.2,Math.PI/1.1),M(0xe8a800));vis.rotation.x=0;vis.position.set(0,.04,.78);vis.scale.set(1,1,.6);g.add(vis);return g;}
// estratto conto (foglio con righe e barra totale)
export function statement(){return sheet((c,W,H)=>{c.fillStyle='#fbfaf5';c.fillRect(0,0,W,H);c.fillStyle='#12303a';c.fillRect(0,0,W,110);c.fillStyle='#fff';c.font='bold 40px AB';c.textAlign='center';c.textBaseline='middle';c.fillText('ESTRATTO CONTO',W/2,56);
  for(let i=0;i<9;i++){c.fillStyle=i%2?'#eef1f4':'#fbfaf5';c.fillRect(30,140+i*58,W-60,54);c.fillStyle='#9aa4b2';c.fillRect(50,158+i*58,150,16);c.fillStyle='#1fb8c4';c.fillRect(W-250,152+i*58,60+((i*37)%110),24);}
  c.fillStyle='#ff6b57';c.font='bold 44px AB';c.textAlign='left';c.fillText('ANNI VERSATI',50,H-70);c.strokeStyle='#12303a';c.lineWidth=6;c.strokeRect(6,6,W-12,H-12);},520,740,2.6,null);}
export function star(){const s=new THREE.Shape();for(let i=0;i<10;i++){const a=i/10*Math.PI*2-Math.PI/2,r=i%2?.55:1.2;const px=Math.cos(a)*r,py=Math.sin(a)*r;i?s.lineTo(px,py):s.moveTo(px,py);}s.closePath();
  const m=new THREE.Mesh(new THREE.ExtrudeGeometry(s,{depth:.4,bevelEnabled:true,bevelSize:.08,bevelThickness:.08,bevelSegments:3}),M(0xf3be3a,{metalness:1,roughness:.28}));m.castShadow=true;return m;}
// pagina di calendario per i mesi che si aggiungono
export function monthPlate(txt,sub,col='#ff6b57'){const [c,g]=cvs(512,512);g.fillStyle='#fbf8ee';g.beginPath();g.roundRect(8,8,496,496,44);g.fill();g.fillStyle=col;g.beginPath();g.roundRect(8,8,496,130,44);g.fill();g.fillRect(8,90,496,48);
  g.fillStyle='#fff';g.font='bold 64px AB';g.textAlign='center';g.textBaseline='middle';g.fillText(sub,256,76);g.fillStyle='#12303a';let f=250;g.font='bold '+f+'px AB';while(g.measureText(txt).width>440){f-=8;g.font='bold '+f+'px AB';}g.fillText(txt,256,320);
  g.strokeStyle='#12303a';g.lineWidth=8;g.beginPath();g.roundRect(8,8,496,496,44);g.stroke();
  const p=new THREE.Mesh(new THREE.PlaneGeometry(1.8,1.8),new THREE.MeshStandardMaterial({map:tex(c),roughness:.6,side:THREE.DoubleSide}));p.castShadow=true;return p;}
// simbolo infinito (senza limite di eta): due anelli affiancati
export function infinity(m){const g=new THREE.Group();[-.62,.62].forEach(x=>{const t=new THREE.Mesh(new THREE.TorusGeometry(.6,.16,18,48),m.gold);t.position.x=x;t.castShadow=true;g.add(t);});return g;}
