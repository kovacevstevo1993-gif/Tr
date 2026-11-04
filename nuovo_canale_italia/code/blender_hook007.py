# Hook dello short 007 (mutuo) in Blender (Cycles, solo CPU). Uso: python3 blender_hook007.py OUT_DIR FRAME_A FRAME_B [RES_Y] [SAMPLES]
import bpy, sys, math, os, time, bmesh
from mathutils import Vector
OUT=sys.argv[1]; A=int(sys.argv[2]); B=int(sys.argv[3]); RY=int(sys.argv[4]) if len(sys.argv)>4 else 960; SM=int(sys.argv[5]) if len(sys.argv)>5 else 28
os.makedirs(OUT,exist_ok=True)
FONT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','brand','fonts','ArchivoBlack-Regular.ttf')
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene; sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=SM; sc.cycles.use_denoising=True; sc.cycles.use_adaptive_sampling=True; sc.cycles.adaptive_threshold=0.03
sc.render.resolution_y=RY; sc.render.resolution_x=int(RY*1080/1920); sc.render.fps=30; sc.render.image_settings.file_format='PNG'
sc.view_settings.view_transform='Filmic' if 'Filmic' in [x.identifier for x in bpy.types.ColorManagedViewSettings.bl_rna.properties['view_transform'].enum_items] else 'AgX'
def mat(name,c,rough=.45,metal=0,emit=None,es=0,trans=0):
    m=bpy.data.materials.new(name); m.use_nodes=True; b=m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=c; b.inputs['Roughness'].default_value=rough; b.inputs['Metallic'].default_value=metal
    if emit: b.inputs['Emission Color'].default_value=emit; b.inputs['Emission Strength'].default_value=es
    if trans: b.inputs['Transmission Weight'].default_value=trans
    return m
cream=mat('cream',(.93,.88,.78,1),.7); roof=mat('roof',(.62,.22,.12,1),.55); wood=mat('wood',(.25,.14,.08,1),.5); gold=mat('gold',(1,.58,.08,1),.2,1); marble=mat('marble',(.92,.92,.9,1),.12)
win=mat('win',(.9,.8,.5,1),.2,0,(1,.75,.35,1),6); glass=mat('glass',(.8,.9,1,1),.03,0,None,0,1); green=mat('green',(.18,.55,.25,1),.8); white=mat('white',(.97,.97,.97,1),.35)
def box(loc,sc3,m,name='b'):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.scale=sc3; o.data.materials.append(m); o.name=name; return o
# piano di marmo lucido
bpy.ops.mesh.primitive_plane_add(size=60); o=bpy.context.object; o.data.materials.append(marble); o.name='floor'
# casetta (modello in miniatura)
HX,HY=0,3.2
box((HX,HY,1.1),(3.2,2.4,2.2),cream,'casa')
me=bpy.data.meshes.new('tetto'); vs=[(-1.75,-1.35,2.2),(1.75,-1.35,2.2),(1.75,1.35,2.2),(-1.75,1.35,2.2),(-1.75,0,3.3),(1.75,0,3.3)]; fs=[(0,1,5,4),(2,3,4,5),(0,4,3),(1,2,5),(0,3,2,1)]
me.from_pydata(vs,[],fs); me.update(); ro=bpy.data.objects.new('tetto',me); bpy.context.collection.objects.link(ro); ro.location=(HX,HY,0); ro.data.materials.append(roof)
box((HX-.9,HY-1.21,.8),(.7,.05,1.1),wood,'porta')
for wx in (HX+.55,HX+1.15):
    box((wx,HY-1.21,1.25),(.38,.05,.5),win,'finestra')
box((HX+1.2,HY+.3,3.4),(.35,.35,.8),cream,'camino')
# alberelli
for tx in (-2.6,2.7):
    bpy.ops.mesh.primitive_cylinder_add(radius=.08,depth=.6,location=(tx,HY-.2,.3)); t=bpy.context.object; t.data.materials.append(wood)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=.55,location=(tx,HY-.2,1.0)); t=bpy.context.object; t.data.materials.append(green)
# numero 759 in oro (testo 3D)
bpy.ops.object.text_add(location=(0,0,0)); tx=bpy.context.object; tx.data.body='759'; tx.data.font=bpy.data.fonts.load(FONT); tx.data.size=2.15; tx.data.extrude=.22; tx.data.bevel_depth=.03; tx.data.align_x='CENTER'; tx.data.align_y='BOTTOM_BASELINE'
tx.data.materials.append(gold); tx.rotation_euler=(math.radians(90),0,0)
bpy.ops.object.text_add(location=(0,0,0)); t2=bpy.context.object; t2.data.body='€ AL MESE'; t2.data.font=tx.data.font; t2.data.size=.5; t2.data.extrude=.07; t2.data.bevel_depth=.012; t2.data.align_x='CENTER'; t2.data.align_y='BOTTOM_BASELINE'
t2.data.materials.append(mat('navy',(.05,.1,.18,1),.35)); t2.rotation_euler=(math.radians(90),0,0)
# luci e cielo
bpy.ops.object.light_add(type='SUN',location=(-6,-6,9)); s=bpy.context.object; s.data.energy=4.5; s.data.angle=math.radians(3); s.rotation_euler=(math.radians(52),0,math.radians(-35))
w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True; nt=w.node_tree; bg=nt.nodes['Background']
sky=nt.nodes.new('ShaderNodeTexSky'); sky.sky_type='NISHITA' if 'NISHITA' in [i.identifier for i in sky.bl_rna.properties['sky_type'].enum_items] else 'HOSEK_WILKIE'
try: sky.sun_elevation=math.radians(42); sky.sun_rotation=math.radians(40)
except Exception: pass
nt.links.new(sky.outputs[0],bg.inputs[0]); bg.inputs[1].default_value=1.7
# camera
cam_d=bpy.data.cameras.new('cam'); cam_d.lens=38; cam_d.sensor_fit='VERTICAL'; cam_d.sensor_width=36; cam_d.sensor_height=36; cam=bpy.data.objects.new('cam',cam_d); bpy.context.collection.objects.link(cam); sc.camera=cam
def ease_bounce(u):
    n1,d1=7.5625,2.75
    if u<1/d1: return n1*u*u
    if u<2/d1: u-=1.5/d1; return n1*u*u+.75
    if u<2.5/d1: u-=2.25/d1; return n1*u*u+.9375
    u-=2.625/d1; return n1*u*u+.984375
def setf(f):
    t=f/30.0
    u=min(1,t/0.28); z0=7.0*(1-ease_bounce(u))
    tx.location=(0,-1.0,.0+z0+0.02); tx.rotation_euler=(math.radians(90),0,math.radians(math.sin(t*1.6)*2.0*min(1,max(0,(t-.5)))))
    k=min(1,max(0,(t-1.7)/0.35)); k=1-(1-k)**3; t2.scale=(max(.001,k),max(.001,k),max(.001,k)); t2.location=(0,-2.4,.02+(1-k)*.3)
    # camera: spinta lenta in avanti + colpo (scossa) all'impatto
    sh=math.exp(-(t-.2)*10)*0.12 if t>.2 else 0
    cam.location=(math.sin(t*90)*sh, -10.4+t*0.3+ (0 if t>.2 else 0), 2.3+math.cos(t*80)*sh)
    tgt=Vector((0,0,1.7)); d=tgt-cam.location; cam.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
for f in range(A,B+1):
    if os.path.exists(os.path.join(OUT,'%05d.png'%f)) and os.environ.get('RESUME'): continue
    t0=time.time(); setf(f); sc.render.filepath=os.path.join(OUT,'%05d.png'%f); bpy.ops.render.render(write_still=True); print('f',f,round(time.time()-t0,1),flush=True)
