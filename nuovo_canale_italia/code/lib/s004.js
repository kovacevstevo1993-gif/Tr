// Oggetti 3D dello short 004 (BENZINA): look NUOVO "stazione di servizio al tramonto" (indaco, arancio tramonto, pensilina bianca, pompe bianche e blu, display ambra)
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
import {rbox,sheet} from '/code/lib/s002.js';
export {rbox,sheet,THREE,clamp,prog,eo,eio,eb,rnd};
export const THEME={bg:0x1c1b48,fogN:30,fogF:78,keyC:0xffd2a0,keyI:420,rimC:0x5a86ff,rimI:110,hemiS:0x7a83f0,hemiG:0x2d2236,hemiI:.62,floor:0x2b2f3b,fR:.8,fM:.06,ring:0xffb000,ringK:1.5,env:.6,expo:.98,bloom:.2,flashK:.4,dustC:0xffd9a0,dustO:.5};
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.45,metalness:.05},o));
export function mats(){return {white:M(0xf4f6fa,{roughness:.32,metalness:.1}),blue:M(0x2f6bff,{roughness:.32,metalness:.35}),navy:M(0x12183a,{roughness:.5}),black:M(0x0d0f16,{roughness:.4,metalness:.3}),
  chrome:M(0xe2e6ec,{metalness:1,roughness:.18}),rubber:M(0x14161c,{roughness:.8}),grey:M(0x8a90a0,{roughness:.6}),tile:M(0x3a4056,{roughness:.6}),
  orange:M(0xe8821a,{roughness:.36,metalness:.3,emissive:0x3a1800,emissiveIntensity:.3}),amber:M(0xffb000,{emissive:0xff9a00,emissiveIntensity:.9,roughness:.35}),lime:M(0xcdee3c,{emissive:0x7fa010,emissiveIntensity:.35,roughness:.25,metalness:.1}),
  limeIt:M(0x2f6bff,{emissive:0x1c44b0,emissiveIntensity:.4,roughness:.25,metalness:.15}),red:M(0xe5392b,{emissive:0x7a1008,emissiveIntensity:.5,roughness:.4}),green:M(0x25b36a,{emissive:0x0a5a30,emissiveIntensity:.4,roughness:.4}),
  glass:M(0xbfd8ff,{roughness:.05,metalness:.2,transparent:true,opacity:.35}),light:new THREE.MeshBasicMaterial({color:0xfff3d6,toneMapped:false})};}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
// ---- sfondo: cielo al tramonto + pensilina della stazione (fondale fisso, lunghissimo) ----
export function backdrop(scene,m){const c=document.createElement('canvas');c.width=1024;c.height=512;const g=c.getContext('2d');
  const gr=g.createLinearGradient(0,0,0,512);gr.addColorStop(0,'#0c0e2e');gr.addColorStop(.38,'#2e2870');gr.addColorStop(.62,'#8a3f8c');gr.addColorStop(.8,'#ff7a45');gr.addColorStop(1,'#ffb05a');g.fillStyle=gr;g.fillRect(0,0,1024,512);
  for(let i=0;i<110;i++){g.fillStyle='rgba(255,255,255,'+(.25+rnd(i+4)*.6)+')';const y=rnd(i+9)*190;g.fillRect(rnd(i)*1024,y,1.6,1.6);}
  const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;
  const sky=new THREE.Mesh(new THREE.PlaneGeometry(150,64),new THREE.MeshBasicMaterial({map:t,fog:false,toneMapped:false}));sky.position.set(0,23,-40);scene.add(sky);
  // sagome lontane (colline/citta)
  const sil=new THREE.Mesh(new THREE.PlaneGeometry(150,3.2),new THREE.MeshBasicMaterial({color:0x1a1840,fog:false,toneMapped:false}));sil.position.set(0,2.1,-39.5);scene.add(sil);
  for(let i=0;i<46;i++){const h=1+rnd(i+30)*4.2;const b=new THREE.Mesh(new THREE.PlaneGeometry(1+rnd(i+50)*1.6,h),new THREE.MeshBasicMaterial({color:0x1a1840,fog:false,toneMapped:false}));b.position.set(-60+i*2.7,h/2+1.6,-39.4);scene.add(b);}
  // pensilina
  const can=new THREE.Group();
  const roof=new THREE.Mesh(new THREE.BoxGeometry(160,.45,9),m.white);roof.position.set(0,8.2,-17);roof.castShadow=true;can.add(roof);
  const edge=new THREE.Mesh(new THREE.BoxGeometry(160,.5,.3),m.blue);edge.position.set(0,7.9,-12.4);can.add(edge);
  const strip=new THREE.Mesh(new THREE.BoxGeometry(160,.08,1.2),m.light);strip.position.set(0,7.94,-15.2);can.add(strip);
  for(let i=-8;i<=8;i++){const p=new THREE.Mesh(new THREE.CylinderGeometry(.28,.3,8,18),m.white);p.position.set(i*8,4,-14.5);p.castShadow=true;can.add(p);const s=new THREE.Mesh(new THREE.BoxGeometry(.5,.5,.5),m.light);s.position.set(i*8+4,7.9,-15);can.add(s);}
  scene.add(can);
  // strisce sul piazzale
  for(let i=-10;i<=10;i++){const s=new THREE.Mesh(new THREE.PlaneGeometry(.12,7),new THREE.MeshBasicMaterial({color:0xcfd4e4,transparent:true,opacity:.22,toneMapped:false}));s.rotation.x=-Math.PI/2;s.position.set(i*3.1,.01,-6.5);scene.add(s);}}
// ---- schermo LCD ambra ----
export function lcd(wu=1.06){const W=640,H=520;const mesh=sheet(()=>{},W,H,wu,null);
  mesh.material.emissive=new THREE.Color(0xffffff);mesh.material.emissiveMap=mesh.material.map;mesh.material.emissiveIntensity=.85;mesh.material.roughness=.3;mesh.castShadow=false;
  const {g,t}=mesh.userData;let cur='';
  mesh.userData.set=(top,big,small,col='#ffb000')=>{const k=top+'|'+big+'|'+small+'|'+col;if(k===cur)return;cur=k;g.clearRect(0,0,W,H);g.fillStyle='#07090f';g.fillRect(0,0,W,H);g.strokeStyle='#3a2a05';g.lineWidth=10;g.strokeRect(5,5,W-10,H-10);
    g.textAlign='center';g.textBaseline='middle';g.fillStyle='#8a6a1a';g.font='bold 46px PM';g.fillText(top,W/2,72);
    g.fillStyle=col;g.shadowColor=col;g.shadowBlur=26;g.font=(big.length>6?'bold 118px AB':'bold 150px AB');g.fillText(big,W/2,H/2+14);g.shadowBlur=0;
    g.fillStyle='#8a6a1a';g.font='bold 42px PM';g.fillText(small,W/2,H-62);t.needsUpdate=true;};
  mesh.userData.set('','','');return mesh;}
// ---- pompa di benzina ----
export function pump(m,{accent=m.blue}={}){const g=new THREE.Group();
  add(g,rbox(2.0,.2,1.55,.07,m.navy),0,.1,0);
  add(g,rbox(1.5,3.0,1.05,.15,m.white),0,1.72,0);
  add(g,rbox(1.62,.55,1.15,.15,accent),0,3.42,0);
  add(g,rbox(1.54,.34,1.09,.1,accent),0,.5,0);
  add(g,rbox(.16,2.4,.05,.03,accent),-.6,1.85,.55);
  add(g,rbox(1.28,1.05,.16,.08,m.black),0,2.62,.52);
  const sc=lcd(1.1);sc.position.set(0,2.62,.61);g.add(sc);
  // pannello tasti
  add(g,rbox(1.0,.62,.1,.05,m.black),0,1.65,.54);
  for(let i=0;i<9;i++)add(g,new THREE.Mesh(new THREE.BoxGeometry(.2,.13,.05),i%4===0?m.amber:m.grey),-.27+(i%3)*.27,1.82-Math.floor(i/3)*.17,.6);
  add(g,rbox(.8,.1,.06,.03,m.chrome),0,1.22,.55);
  // portapistola + pistola + tubo
  add(g,rbox(.3,.7,.4,.1,m.black),.82,1.9,.08);
  const noz=new THREE.Group();add(noz,rbox(.2,.5,.22,.08,m.rubber),0,0,0);add(noz,rbox(.12,.12,.5,.04,m.chrome),0,.3,.26);add(noz,new THREE.Mesh(new THREE.CylinderGeometry(.04,.05,.5,12),m.chrome),0,.38,.5).rotation.x=Math.PI/2.4;noz.position.set(.82,2.0,.1);g.add(noz);
  const crv=new THREE.CatmullRomCurve3([new THREE.Vector3(.82,1.65,.1),new THREE.Vector3(1.2,1.2,.4),new THREE.Vector3(1.28,.7,.5),new THREE.Vector3(.95,.35,.62),new THREE.Vector3(.7,.3,.5)]);
  const tube=new THREE.Mesh(new THREE.TubeGeometry(crv,48,.05,10,false),m.rubber);tube.castShadow=true;g.add(tube);
  g.userData.lcd=sc;g.userData.noz=noz;return g;}
// ---- bandiere ----
export function drawFlag(g,k,x,y,w,h){const R=(c,a,b,cw,ch)=>{g.fillStyle=c;g.fillRect(x+a*w,y+b*h,cw*w+.5,ch*h+.5);};
  if(k==='ES'){R('#c60b1e',0,0,1,.25);R('#ffc400',0,.25,1,.5);R('#c60b1e',0,.75,1,.25);}
  else if(k==='AT'){R('#ed2939',0,0,1,.34);R('#ffffff',0,.33,1,.34);R('#ed2939',0,.66,1,.34);}
  else if(k==='IT'){R('#009246',0,0,.34,1);R('#ffffff',.33,0,.34,1);R('#ce2b37',.66,0,.34,1);}
  else if(k==='DE'){R('#111111',0,0,1,.34);R('#dd0000',0,.33,1,.34);R('#ffce00',0,.66,1,.34);}
  else if(k==='FR'){R('#0055a4',0,0,.34,1);R('#ffffff',.33,0,.34,1);R('#ef4135',.66,0,.34,1);}
  else if(k==='EU'){R('#003399',0,0,1,1);g.fillStyle='#ffcc00';for(let i=0;i<12;i++){const a=i/12*Math.PI*2;g.beginPath();g.arc(x+w/2+Math.cos(a)*h*.33,y+h/2+Math.sin(a)*h*.33,h*.055,0,7);g.fill();}}
  g.strokeStyle='rgba(255,255,255,.55)';g.lineWidth=3;g.strokeRect(x,y,w,h);}
export function flagTag(st,name,flag,{border='#ffb000',sw=2.6,w=720,h=170,font='bold 58px PM',fill='#ffffff',bg='rgba(14,16,40,.93)',sub=null}={}){
  return st.label((g,W_,H_)=>{g.fillStyle=bg;st.rr(g,6,6,W_-12,H_-12,44);g.fill();g.strokeStyle=border;g.lineWidth=8;g.stroke();drawFlag(g,flag,38,H_/2-34,100,68);
    g.fillStyle=fill;g.font=font;g.textAlign='left';g.textBaseline='middle';g.fillText(name,170,H_/2+4);if(sub){g.fillStyle=border;g.font='bold 40px PM';g.textAlign='right';g.fillText(sub,W_-40,H_/2+4);}},w,h,sw,name);}
// ---- telefono con mappa a pin (illustrazione generica) ----
export function phone(m){const g=new THREE.Group();
  add(g,rbox(2.1,4.1,.24,.22,m.black),0,0,0);
  const scr=sheet((c,W,H)=>{c.fillStyle='#1f2a58';c.fillRect(0,0,W,H);c.fillStyle='#2a376c';
    for(let i=0;i<9;i++)for(let j=0;j<14;j++){if((i*7+j*3)%5===0)continue;c.fillRect(30+i*62,150+j*76,46,56);}
    c.strokeStyle='#5f72b8';c.lineWidth=7;[[0,300,600,380],[0,640,600,560],[160,100,230,1180],[430,100,360,1180]].forEach(p=>{c.beginPath();c.moveTo(p[0],p[1]);c.lineTo(p[2],p[3]);c.stroke();});
    c.fillStyle='#ffb000';c.fillRect(0,0,W,120);c.fillStyle='#14163a';c.font='bold 40px PM';c.textAlign='center';c.textBaseline='middle';c.fillText('DISTRIBUTORI VICINI',W/2,62);
    [[150,460],[430,360],[300,700],[130,860],[470,900],[330,1040]].forEach((p,i)=>{c.fillStyle=i===2?'#25b36a':'#e5392b';c.beginPath();c.arc(p[0],p[1],i===2?46:34,0,7);c.fill();c.fillStyle='#fff';c.font=(i===2?'bold 52px AB':'bold 40px AB');c.fillText('€',p[0],p[1]+3);});
  },600,1180,1.86,null);scr.material.emissive=new THREE.Color(0xffffff);scr.material.emissiveMap=scr.material.map;scr.material.emissiveIntensity=.55;scr.position.set(0,-.02,.13);g.add(scr);
  return g;}
export function speech(m){const g=new THREE.Group();add(g,rbox(2.9,1.7,.3,.4,m.white),0,0,0);const t=add(g,new THREE.Mesh(new THREE.ConeGeometry(.3,.55,3),m.white),-.8,-1.1,0);t.rotation.z=Math.PI;return g;}
export function dustp(n=200,color=0xffffff,size=.07){const pos=new Float32Array(n*3);const p=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.BufferAttribute(pos,3)),new THREE.PointsMaterial({color,size,transparent:true,opacity:1,depthWrite:false}));
  p.userData.update=(t0,t,ox,oy,oz,spread=1.4)=>{const u=t-t0;const a=p.geometry.attributes.position.array;p.visible=u>0&&u<1.8;for(let i=0;i<n;i++){const r1=rnd(i),r2=rnd(i+7),r3=rnd(i+13);a[i*3]=ox+(r1-.5)*spread*(1+u);a[i*3+1]=oy+(r2-.4)*spread*.8+u*(.5+r3*1.4);a[i*3+2]=oz+(r3-.5)*.8;}p.geometry.attributes.position.needsUpdate=true;p.material.opacity=clamp(1-u/1.7);};return p;}
