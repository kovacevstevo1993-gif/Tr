// Libreria comune delle scene 3D dello short 001 (stesso "palco" del blocco 1): luci, pavimento, post-processing, scritte, serbatoi, camera.
import * as THREE from 'three';
import {RoomEnvironment} from 'three/addons/environments/RoomEnvironment.js';
import {EffectComposer} from 'three/addons/postprocessing/EffectComposer.js';
import {RenderPass} from 'three/addons/postprocessing/RenderPass.js';
import {UnrealBloomPass} from 'three/addons/postprocessing/UnrealBloomPass.js';
import {OutputPass} from 'three/addons/postprocessing/OutputPass.js';
export {THREE};
export const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
export const prog=(t,a,b)=>clamp((t-a)/(b-a));
export const eo=x=>1-Math.pow(1-x,3), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
export const eb=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
export const rnd=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);};
export const RED=0xE32119,YEL=0xFFE14A,PAPER=0xF3F0E8;

export async function createStage({dur,centers=[0],kf}){
  const W=window.innerWidth,H=window.innerHeight;
  await Promise.all([new FontFace('AB','url(/brand/fonts/ArchivoBlack-Regular.ttf)'),new FontFace('PM','url(/brand/fonts/IBMPlexMono-Bold.ttf)')].map(f=>f.load().then(x=>document.fonts.add(x))));
  const renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'high-performance'});
  renderer.setSize(W,H);renderer.setPixelRatio(1);renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.0;document.body.appendChild(renderer.domElement);
  const scene=new THREE.Scene();scene.background=new THREE.Color(0x0b0c0f);scene.fog=new THREE.Fog(0x0b0c0f,16,46);
  const pm=new THREE.PMREMGenerator(renderer);scene.environment=pm.fromScene(new RoomEnvironment(),0.04).texture;scene.environmentIntensity=0.55;
  const cam=new THREE.PerspectiveCamera(38,W/H,0.1,120);
  const key=new THREE.SpotLight(0xffe2b0,270,60,0.5,0.7,1.6);key.castShadow=true;key.shadow.mapSize.set(2048,2048);key.shadow.bias=-0.0004;key.shadow.radius=5;scene.add(key,key.target);
  const rim=new THREE.PointLight(0xff3a2a,45,40,1.6);scene.add(rim);
  scene.add(new THREE.HemisphereLight(0x8e97b0,0x1a1210,0.28));
  const floor=new THREE.Mesh(new THREE.CircleGeometry(60,96),new THREE.MeshStandardMaterial({color:0x0a0b0e,roughness:.45,metalness:.3}));
  floor.rotation.x=-Math.PI/2;floor.receiveShadow=true;scene.add(floor);
  centers.forEach(cx=>[[3.4,.03,.20],[5.6,.025,.11],[7.8,.02,.06]].forEach(([r,w,o])=>{const m=new THREE.Mesh(new THREE.RingGeometry(r,r+w,128),new THREE.MeshBasicMaterial({color:PAPER,transparent:true,opacity:o,side:THREE.DoubleSide}));m.rotation.x=-Math.PI/2;m.position.set(cx,.004,0);scene.add(m);}));
  const mats={
    gold:new THREE.MeshStandardMaterial({color:0xFFD23A,metalness:1,roughness:.5}),
    red:new THREE.MeshStandardMaterial({color:0xE32119,metalness:.75,roughness:.28,emissive:0x5a0605,emissiveIntensity:.8}),
    redGlow:new THREE.MeshStandardMaterial({color:0xE32119,emissive:0xE32119,emissiveIntensity:1.1,roughness:.35}),
    chrome:new THREE.MeshStandardMaterial({color:0xdde0e4,metalness:1,roughness:.22}),
    paper:new THREE.MeshStandardMaterial({color:PAPER,roughness:.7}),
    dark:new THREE.MeshStandardMaterial({color:0x23262c,roughness:.5,metalness:.3}),
    yellow:new THREE.MeshStandardMaterial({color:YEL,emissive:0xffc83a,emissiveIntensity:.9,roughness:.4}),
    glass:new THREE.MeshStandardMaterial({color:0xffffff,transparent:true,opacity:.07,roughness:.05,metalness:.1,side:THREE.DoubleSide,depthWrite:false})
  };
  // polvere
  const dustN=220,dp=new Float32Array(dustN*3);for(let i=0;i<dustN;i++){dp[i*3]=(rnd(i)-.5)*30;dp[i*3+1]=rnd(i+1)*10;dp[i*3+2]=(rnd(i+2)-.5)*24-4;}
  const dust=new THREE.Points(new THREE.BufferGeometry().setAttribute('position',new THREE.BufferAttribute(dp.slice(),3)),new THREE.PointsMaterial({color:0xfff2d0,size:.045,transparent:true,opacity:.35,depthWrite:false}));scene.add(dust);
  const comp=new EffectComposer(renderer);comp.setPixelRatio(1);comp.setSize(W,H);comp.addPass(new RenderPass(scene,cam));
  const bloom=new UnrealBloomPass(new THREE.Vector2(W/2,H/2),.14,.45,.97);comp.addPass(bloom);comp.addPass(new OutputPass());
  // scritte (sprite)
  const sprites=[];
  function rr(g,x,y,w,h,r){g.beginPath();g.moveTo(x+r,y);g.arcTo(x+w,y,x+w,y+h,r);g.arcTo(x+w,y+h,x,y+h,r);g.arcTo(x,y+h,x,y,r);g.arcTo(x,y,x+w,y,r);g.closePath();}
  function label(draw,w,h,sw,name='?'){const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');draw(g,w,h);
    const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:t,transparent:true,depthTest:false,fog:false}));s.scale.set(sw,sw*h/w,1);s.renderOrder=10;s.visible=false;scene.add(s);s.userData={c,g,t,w,h,sw,name};sprites.push(s);return s;}
  function setSprite(s,x,y,z,show,sc=1){s.visible=show>.01&&sc>.001;s.material.opacity=clamp(show);s.position.set(x,y,z);s.scale.set(s.userData.sw*sc,s.userData.sw*sc*s.userData.h/s.userData.w,1);}
  // etichetta standard: pannello scuro con bordo e testo (una o due righe)
  function tag(lines,{border='#F3F0E8',font='bold 74px PM',w=760,h=null,sw=2.5,fill='#F3F0E8',bg='rgba(16,17,21,.9)'}={}){const hh=h||(lines.length>1?260:170);
    return label((g,W_,H_)=>{g.fillStyle=bg;rr(g,6,6,W_-12,H_-12,40);g.fill();g.strokeStyle=border;g.lineWidth=8;g.stroke();g.fillStyle=fill;g.font=font;g.textAlign='center';g.textBaseline='middle';
      lines.forEach((l,i)=>g.fillText(l,W_/2,H_*((i+1)/(lines.length+1))+4));},w,hh,sw,lines.join(' '));}
  // numero grande che cambia (conteggio)
  function counter({w=720,h=260,sw=2.0,color='#F3F0E8',border='#F3F0E8',font='140px AB',bg='rgba(16,17,21,.92)'}={}){let cur='';
    const s=label(()=>{},w,h,sw,'num');s.userData.set=(str)=>{if(str===cur)return;cur=str;const g=s.userData.g;g.clearRect(0,0,w,h);g.fillStyle=bg;rr(g,6,6,w-12,h-12,46);g.fill();g.strokeStyle=border;g.lineWidth=8;g.stroke();g.fillStyle=color;g.font=font;g.textAlign='center';g.textBaseline='middle';g.fillText(str,w/2,h/2+8);s.userData.t.needsUpdate=true;};return s;}
  // serbatoio di vetro con liquido e tacche (1 unita = 10%)
  function tank({x,z=0,r=.55,H=5.0,color=mats.red,ticks=true}){const g=new THREE.Group();g.position.set(x,0,z);
    const glass=new THREE.Mesh(new THREE.CylinderGeometry(r,r,H,48,1,true),mats.glass);glass.position.y=H/2;g.add(glass);
    const base=new THREE.Mesh(new THREE.CylinderGeometry(r+.12,r+.18,.16,48),mats.chrome);base.position.y=.08;base.castShadow=true;g.add(base);
    const cap=new THREE.Mesh(new THREE.TorusGeometry(r+.02,.05,12,48),mats.chrome);cap.rotation.x=Math.PI/2;cap.position.y=H;g.add(cap);
    const liq=new THREE.Mesh(new THREE.CylinderGeometry(r*.9,r*.9,1,48),color);liq.position.y=.16;liq.scale.y=.001;g.add(liq);
    if(ticks)for(let k=1;k<=Math.floor(H);k++){const tk=new THREE.Mesh(new THREE.BoxGeometry(.28,.035,.035),mats.chrome);tk.position.set(-r-.18,.16+k,0);g.add(tk);}
    scene.add(g);return {g,liq,set(level){const L=Math.max(level,.001);liq.scale.y=L;liq.position.y=.16+L/2;}};}
  // camera: tappe [t,[pos],[look],ease?] ('w'=stacco secco)
  const lv=new THREE.Vector3(),cp=new THREE.Vector3();
  function camAt(t){let i=0;while(i<kf.length-2&&t>kf[i+1][0])i++;const a=kf[i],b=kf[i+1];const u=t<=a[0]?0:clamp((t-a[0])/(b[0]-a[0]));const e=(a[3]==='w')?eio(u):u*u*(3-2*u);
    cp.set(...a[1]).lerp(new THREE.Vector3(...b[1]),e);lv.set(...a[2]).lerp(new THREE.Vector3(...b[2]),e);}
  function render(t,{shakes=[],flashes=[]}={}){
    const damp=1-eio(prog(t,dur-0.55,dur-0.06));
    const dpos=dust.geometry.attributes.position;for(let i=0;i<dustN;i++){dpos.array[i*3+1]=(dp[i*3+1]+t*(.15+rnd(i+9)*.25)*damp)%10;dpos.array[i*3]=dp[i*3]+Math.sin(t*.5+i)*.2*damp;}dpos.needsUpdate=true;
    camAt(t);let sh=0,fl=0;shakes.forEach(s=>{if(t>s)sh+=Math.exp(-(t-s)*9)*.22;});flashes.forEach(s=>{if(t>s)fl+=Math.exp(-(t-s)*12);});
    cam.position.set(cp.x+Math.sin(t*1.3)*.12*damp+Math.sin(t*80)*sh*.6,cp.y+Math.cos(t*1.1)*.08*damp+Math.cos(t*70)*sh*.5,cp.z);cam.lookAt(lv.x,lv.y,lv.z);
    key.position.set(lv.x-7,13,9);key.target.position.set(lv.x,1.5,0);rim.position.set(lv.x+7,5,-6);rim.intensity=45+15*Math.sin(t*5)*damp;
    renderer.toneMappingExposure=1.0+.6*fl;bloom.strength=.14+.3*fl;comp.render();return damp;}
  function bounds(){const bad=[];cam.updateMatrixWorld();const right=new THREE.Vector3().setFromMatrixColumn(cam.matrixWorld,0),up=new THREE.Vector3().setFromMatrixColumn(cam.matrixWorld,1);
    sprites.forEach(s=>{if(!s.visible||s.material.opacity<.05||Math.abs(s.position.x-cam.position.x)>5)return;const hw=s.scale.x/2,hh=s.scale.y/2;
      [[-1,-1],[1,-1],[1,1],[-1,1]].forEach(([a,b])=>{const q=s.position.clone().addScaledVector(right,a*hw).addScaledVector(up,b*hh).project(cam);const x=(q.x+1)/2*W,y=(1-q.y)/2*H;
        const kx=W/1080,ky=H/1920;if(x<24*kx||x>W-24*kx||y<150*ky||y>1560*ky)bad.push([s.userData.name,Math.round(x),Math.round(y)]);});});return bad;}
  return {THREE,renderer,scene,cam,key,rim,bloom,comp,mats,label,tag,counter,tank,setSprite,rr,render,bounds,W,H,camAt,dur};
}
export function boot(st,draw){window.draw=draw;window.bounds=()=>st.bounds();window.pronto=true;draw(0);}
