// Oggetti 3D dello short 002 (BCE / Lagarde): poltrona, figura, casa, carta, punto interrogativo, quadrante, lucchetto, orologio, busta, timeline, urna, tavolo, giornali, bilancia, campanella.
import {THREE,clamp,prog,eo,eio,eb,rnd} from '/code/lib/stage.js';
const M=(c,o={})=>new THREE.MeshStandardMaterial(Object.assign({color:c,roughness:.5,metalness:.1},o));
export function rbox(w,h,d,r=.08,mat){const s=new THREE.Shape();const x=-w/2,y=-h/2;s.moveTo(x+r,y);s.lineTo(x+w-r,y);s.quadraticCurveTo(x+w,y,x+w,y+r);s.lineTo(x+w,y+h-r);s.quadraticCurveTo(x+w,y+h,x+w-r,y+h);s.lineTo(x+r,y+h);s.quadraticCurveTo(x,y+h,x,y+h-r);s.lineTo(x,y+r);s.quadraticCurveTo(x,y,x+r,y);
  const g=new THREE.ExtrudeGeometry(s,{depth:d-2*r*.5,bevelEnabled:true,bevelSize:r*.5,bevelThickness:r*.5,bevelSegments:3,curveSegments:6});g.translate(0,0,-(d-2*r*.5)/2);const m=new THREE.Mesh(g,mat);m.castShadow=true;m.receiveShadow=true;return m;}
const add=(g,m,x=0,y=0,z=0)=>{m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;g.add(m);return m;};
export function mats(){return {
  leather:M(0x7a1612,{roughness:.42,metalness:.15}),leather2:M(0x5a0f0c,{roughness:.5}),chrome:M(0xdde0e4,{metalness:1,roughness:.2}),gold:M(0xFFD23A,{metalness:1,roughness:.38}),
  suit:M(0x15171c,{roughness:.8}),skin:M(0x2a2d34,{roughness:.7}),paper:M(0xF3F0E8,{roughness:.7}),dark:M(0x23262c,{roughness:.5,metalness:.3}),
  red:M(0xE32119,{emissive:0x7a0f0a,emissiveIntensity:.9,roughness:.35}),yel:M(0xFFE14A,{emissive:0xffc83a,emissiveIntensity:.8,roughness:.4}),
  green:M(0x19A35B,{emissive:0x0a5a30,emissiveIntensity:.7,roughness:.4}),wood:M(0x3a2418,{roughness:.55}),wall:M(0xcfc6b2,{roughness:.8}),glassd:M(0x9fd3ff,{roughness:.1,metalness:.2,transparent:true,opacity:.55})};}
// poltrona direzionale (davanti = +z)
export function chair(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.12,.16,.9,20),m.chrome),0,.55,0);
  for(let i=0;i<5;i++){const a=i/5*Math.PI*2;const leg=new THREE.Mesh(new THREE.BoxGeometry(.9,.07,.12),m.chrome);leg.position.set(Math.sin(a)*.42,.14,Math.cos(a)*.42);leg.rotation.y=a;leg.castShadow=true;g.add(leg);
    add(g,new THREE.Mesh(new THREE.SphereGeometry(.08,12,12),m.dark),Math.sin(a)*.82,.08,Math.cos(a)*.82);}
  add(g,rbox(1.5,.28,1.4,.12,m.leather),0,1.12,0);
  const back=add(g,rbox(1.45,1.9,.34,.14,m.leather),0,2.15,-.66);back.rotation.x=-.08;
  add(g,rbox(.28,.16,1.1,.07,m.leather2),-.82,1.62,-.02);add(g,rbox(.28,.16,1.1,.07,m.leather2),.82,1.62,-.02);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.1,.5,.1),m.chrome),-.82,1.35,-.05);add(g,new THREE.Mesh(new THREE.BoxGeometry(.1,.5,.1),m.chrome),.82,1.35,-.05);
  // bottoni capitonne sullo schienale
  for(let r=0;r<3;r++)for(let c=0;c<3;c++)add(g,new THREE.Mesh(new THREE.SphereGeometry(.045,10,10),m.gold),(c-1)*.42,1.7+r*.42,-.47);
  return g;}
// figura anonima seduta/in piedi (senza volto)
export function figure(m){const g=new THREE.Group();const suit=M(0x2c313b,{roughness:.65}),shirt=M(0xf1efe8,{roughness:.7}),skin=M(0x8a8f98,{roughness:.6});
  add(g,rbox(1.1,1.25,.6,.22,suit),0,.1,0);
  const v=new THREE.Mesh(new THREE.ConeGeometry(.2,.55,3),shirt);v.rotation.set(Math.PI,0,0);v.position.set(0,.45,.31);g.add(v);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.07,.5,.03),m.red),0,.3,.33);
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.11,.13,.18,14),skin),0,.82,0);
  add(g,new THREE.Mesh(new THREE.SphereGeometry(.27,28,22),skin),0,1.07,0);
  [-1,1].forEach(s=>{const a=add(g,rbox(.24,.95,.28,.1,suit),s*.7,.0,.12);a.rotation.x=.85;
    const t=add(g,rbox(.3,.8,.3,.1,suit),s*.3,-.7,.55);t.rotation.x=Math.PI/2;});
  return g;}
export function standFigure(m,s=1){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CapsuleGeometry(.3*s,.62*s,8,16),m.suit),0,1.15*s,0);
  add(g,new THREE.Mesh(new THREE.SphereGeometry(.21*s,20,16),m.skin),0,1.95*s,0);
  add(g,new THREE.Mesh(new THREE.CapsuleGeometry(.1*s,.7*s,6,10),m.suit),-.14*s,.4*s,0);add(g,new THREE.Mesh(new THREE.CapsuleGeometry(.1*s,.7*s,6,10),m.suit),.14*s,.4*s,0);
  return g;}
export function house(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.BoxGeometry(2.2,1.5,1.8),m.wall),0,.75,0);
  const roof=add(g,new THREE.Mesh(new THREE.ConeGeometry(1.95,1.0,4),m.red),0,2.0,0);roof.rotation.y=Math.PI/4;roof.scale.z=.85;
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.5,.9,.06),m.wood),0,.45,.92);
  [-.7,.7].forEach(x=>add(g,new THREE.Mesh(new THREE.BoxGeometry(.4,.4,.06),m.yel),x,.95,.92));
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.28,.6,.28),m.dark),.7,2.35,-.3);
  return g;}
export function card(m){const g=new THREE.Group();
  add(g,rbox(2.4,1.5,.08,.12,M(0x1a3c8f,{metalness:.5,roughness:.3})),0,0,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(.5,.38,.02),m.gold),-.75,.28,.07);add(g,new THREE.Mesh(new THREE.BoxGeometry(1.9,.1,.02),m.paper),.0,-.45,.06);add(g,new THREE.Mesh(new THREE.BoxGeometry(1.2,.07,.02),m.paper),-.35,-.62,.06);
  return g;}
export function question(m){const g=new THREE.Group();
  const arc=add(g,new THREE.Mesh(new THREE.TorusGeometry(.52,.17,18,40,Math.PI*1.45),m.yel),0,.75,0);arc.rotation.z=Math.PI*.14;
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.17,.17,.5,18),m.yel),.0,.0,0);
  const dotm=add(g,new THREE.Mesh(new THREE.SphereGeometry(.22,18,18),m.yel),0,-.6,0);
  return g;}
// quadrante (tasso): lancetta ruotabile, 0-6 %
export function dial(m,{R=1.5}={}){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(R,R,.18,64),m.dark),0,0,0).rotation.x=Math.PI/2;
  const ring=add(g,new THREE.Mesh(new THREE.TorusGeometry(R,.09,16,64),m.chrome),0,0,.02);
  const face=add(g,new THREE.Mesh(new THREE.CircleGeometry(R*.93,64),M(0x0e1014,{roughness:.6})),0,0,.1);
  for(let i=0;i<=12;i++){const a=(-135+i*22.5)*Math.PI/180;const t=new THREE.Mesh(new THREE.BoxGeometry(.05,i%2?.16:.3,.03),i%2?m.paper:m.yel);t.position.set(Math.sin(a)*R*.8,Math.cos(a)*R*.8,.13);t.rotation.z=-a;g.add(t);}
  const needle=new THREE.Group();const nb=new THREE.Mesh(new THREE.BoxGeometry(.09,R*.78,.04),m.red);nb.position.y=R*.39;needle.add(nb);needle.position.z=.16;g.add(needle);
  add(g,new THREE.Mesh(new THREE.SphereGeometry(.14,16,16),m.chrome),0,0,.19);
  g.userData.needle=needle;g.userData.set=(pct)=>{needle.rotation.z=-(-135+pct/6*270)*Math.PI/180;};g.userData.set(0);return g;}
export function padlock(m){const g=new THREE.Group();
  add(g,rbox(1.1,.9,.55,.14,m.gold),0,0,0);
  const sh=new THREE.Group();const arc=new THREE.Mesh(new THREE.TorusGeometry(.34,.08,12,28,Math.PI),m.chrome);arc.castShadow=true;sh.add(arc);
  [-.34,.34].forEach(x=>{const l=new THREE.Mesh(new THREE.CylinderGeometry(.08,.08,.28,12),m.chrome);l.position.set(x,-.14,0);sh.add(l);});sh.position.y=.45;g.add(sh);
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.09,.09,.1,12),m.dark),0,.05,.28).rotation.x=Math.PI/2;
  g.userData.shackle=sh;return g;}
export function clock(m,R=1.2){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(R,R,.16,64),m.paper),0,0,0).rotation.x=Math.PI/2;
  add(g,new THREE.Mesh(new THREE.TorusGeometry(R,.09,14,64),m.chrome),0,0,.02);
  for(let i=0;i<12;i++){const a=i*Math.PI/6;const t=new THREE.Mesh(new THREE.BoxGeometry(.06,i%3?.14:.24,.03),m.dark);t.position.set(Math.sin(a)*R*.82,Math.cos(a)*R*.82,.1);t.rotation.z=-a;g.add(t);}
  const hh=new THREE.Group(),mm=new THREE.Group();
  const hb=new THREE.Mesh(new THREE.BoxGeometry(.1,R*.5,.04),m.dark);hb.position.y=R*.25;hh.add(hb);const mb=new THREE.Mesh(new THREE.BoxGeometry(.07,R*.78,.04),m.red);mb.position.y=R*.39;mm.add(mb);
  hh.position.z=.14;mm.position.z=.17;g.add(hh,mm);add(g,new THREE.Mesh(new THREE.SphereGeometry(.09,12,12),m.chrome),0,0,.2);
  g.userData.set=(h,mi)=>{hh.rotation.z=-h*Math.PI/6;mm.rotation.z=-mi*Math.PI/30;};g.userData.set(10,10);return g;}
// foglio con testo disegnato a canvas
export function sheet(draw,w,h,wu,mat){const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');draw(g,w,h);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(wu,wu*h/w),new THREE.MeshStandardMaterial({map:t,roughness:.75,metalness:0,side:THREE.DoubleSide}));mesh.castShadow=true;mesh.receiveShadow=true;mesh.userData={c,g,t,w,h};return mesh;}
export function envelope(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.BoxGeometry(2.6,1.7,.1),M(0xe9dfc7,{roughness:.8})),0,0,0);
  const fl=new THREE.Group();const tri=new THREE.Shape();tri.moveTo(-1.3,0);tri.lineTo(1.3,0);tri.lineTo(0,-1.0);tri.closePath();
  const fm=new THREE.Mesh(new THREE.ShapeGeometry(tri),M(0xd8ccb0,{roughness:.8,side:THREE.DoubleSide}));fm.castShadow=true;fl.add(fm);fl.position.set(0,.85,.06);g.add(fl);
  g.userData.flap=fl;return g;}
export function ballotBox(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.BoxGeometry(2.0,1.7,1.4),M(0x1a3c8f,{roughness:.4,metalness:.3})),0,.85,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(1.0,.06,.12),m.dark),0,1.72,.0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(2.1,.12,1.5),m.chrome),0,1.76,0);
  add(g,new THREE.Mesh(new THREE.BoxGeometry(1.0,.07,.14),m.dark),0,1.83,0);
  return g;}
export function roundTable(m,n=12){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(2.2,2.2,.18,64),M(0xb07a45,{roughness:.4,metalness:.2})),0,1.0,0);add(g,new THREE.Mesh(new THREE.CylinderGeometry(.25,.4,1.0,24),m.dark),0,.5,0);
  add(g,new THREE.Mesh(new THREE.TorusGeometry(2.15,.05,10,64),m.gold),0,1.1,0).rotation.x=Math.PI/2;
  const seats=[];for(let i=0;i<n;i++){const a=i/n*Math.PI*2;const s=new THREE.Group();
    const f=standFigure(Object.assign({},m,{suit:M(0x56637a,{roughness:.6}),skin:M(0xc9ccd3,{roughness:.6})}),.62);f.position.y=-.1;s.add(f);s.position.set(Math.sin(a)*3.0,0,Math.cos(a)*3.0);s.lookAt(0,0,0);g.add(s);seats.push(s);}
  g.userData.seats=seats;return g;}
export function paperCard(lines,{w=640,h=420,wu=1.7,bg='#F3F0E8',ink='#16181D',bar=false}={}){
  return sheet((g,W,H)=>{g.fillStyle=bg;g.fillRect(0,0,W,H);g.fillStyle='#d4cfc1';g.fillRect(0,0,W,16);g.fillStyle=ink;g.textAlign='center';g.textBaseline='middle';g.font='bold 120px PM';g.fillText(lines[0],W/2,H*.38);g.font='bold 54px PM';g.fillStyle='#8A8F98';g.fillText(lines[1]||'',W/2,H*.7);},w,h,wu);}
export function scale(m){const g=new THREE.Group();
  add(g,new THREE.Mesh(new THREE.CylinderGeometry(.7,.9,.2,36),m.dark),0,.1,0);add(g,new THREE.Mesh(new THREE.CylinderGeometry(.1,.14,3.6,18),m.chrome),0,1.9,0);
  const beam=new THREE.Group();beam.position.y=3.7;g.add(beam);add(beam,new THREE.Mesh(new THREE.BoxGeometry(5.0,.14,.2),m.gold),0,0,0);add(beam,new THREE.Mesh(new THREE.SphereGeometry(.18,16,16),m.gold),0,0,0);
  const mkpan=(x)=>{const p=new THREE.Group();p.position.set(x,0,0);beam.add(p);
    [-1,1].forEach(s=>{const ch=new THREE.Mesh(new THREE.CylinderGeometry(.015,.015,1.6,6),m.chrome);ch.position.set(s*.62,-.8,0);ch.rotation.z=-s*.35;p.add(ch);});
    const pan=new THREE.Mesh(new THREE.CylinderGeometry(.95,.7,.12,40),m.chrome);pan.position.y=-1.6;pan.castShadow=true;p.add(pan);return p;};
  const L=mkpan(-2.4),R=mkpan(2.4);g.userData={beam,L,R};
  g.userData.tilt=(a)=>{beam.rotation.z=a;L.rotation.z=-a;R.rotation.z=-a;};return g;}
export function bell(m){const g=new THREE.Group();const pts=[];for(let i=0;i<=16;i++){const u=i/16;pts.push(new THREE.Vector2(.06+.72*Math.pow(u,.55)+(u>.86?.14*(u-.86)/.14:0),1.2*(1-u)));}
  const body=new THREE.Mesh(new THREE.LatheGeometry(pts,48),new THREE.MeshStandardMaterial({color:0xFFD23A,metalness:1,roughness:.3,side:THREE.DoubleSide}));body.castShadow=true;g.add(body);add(g,new THREE.Mesh(new THREE.SphereGeometry(.13,14,14),m.gold),0,1.3,0);
  const tong=add(g,new THREE.Mesh(new THREE.SphereGeometry(.15,14,14),m.chrome),0,-.08,0);g.userData.tong=tong;return g;}
// particelle che salgono (dissolvenza): Points con posizioni analitiche
export function dust(n=260,color=0xFFD23A){const pos=new Float32Array(n*3);const p=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.BufferAttribute(pos,3)),new THREE.PointsMaterial({color,size:.07,transparent:true,opacity:1,depthWrite:false,blending:THREE.AdditiveBlending}));
  p.userData.update=(t0,t,ox,oy,oz)=>{const u=t-t0;const a=p.geometry.attributes.position.array;p.visible=u>0&&u<2.2;for(let i=0;i<n;i++){const r1=rnd(i),r2=rnd(i+7),r3=rnd(i+13);
      a[i*3]=ox+(r1-.5)*.9+Math.sin(u*2+i)*.1*u;a[i*3+1]=oy+(r2-.3)*1.6+u*(.6+r3*1.6);a[i*3+2]=oz+(r3-.5)*.7;}p.geometry.attributes.position.needsUpdate=true;p.material.opacity=clamp(1-u/2.1);};return p;}
export {THREE,clamp,prog,eo,eio,eb,rnd};
