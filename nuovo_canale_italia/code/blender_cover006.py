# Fondo della copertina short 006 (Blender, Cycles CPU): mazzetta di banconote, banconote che volano via, "- 512 €" rosso 3D, caveau sullo sfondo.
# Uso: python3 blender_cover006.py out.png [RES_Y] [SAMPLES]
import bpy, sys, math, os, random
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont
OUT=sys.argv[1]; RY=int(sys.argv[2]) if len(sys.argv)>2 else 1920; SM=int(sys.argv[3]) if len(sys.argv)>3 else 48
HERE=os.path.dirname(os.path.abspath(__file__)); FONT=os.path.join(HERE,'..','brand','fonts','ArchivoBlack-Regular.ttf'); MONO=os.path.join(HERE,'..','brand','fonts','IBMPlexMono-Bold.ttf')
TMP='/tmp/claude-0/cover006_tex'; os.makedirs(TMP,exist_ok=True)
# texture banconota da 50 euro (disegno generico) e lato mazzetta
im=Image.new('RGB',(1024,512),(246,170,100)); d=ImageDraw.Draw(im)
for i in range(30): d.ellipse((240-i*8,256-i*8-20,240+i*18,256+i*8),outline=(214,140,80))
d.rectangle((60,50,200,462),fill=(250,205,160)); f=ImageFont.truetype(FONT,250); d.text((470,250),'50',font=f,fill=(120,58,10),anchor='mm'); d.text((870,140),'EURO',font=ImageFont.truetype(MONO,70),fill=(120,58,10),anchor='mm')
for i in range(36): d.rectangle((270+i*18,420,270+i*18+8,450+(i%4)*8),fill=(150,80,30))
d.rectangle((8,8,1016,504),outline=(120,58,10),width=10); im.save(TMP+'/bill.png')
sd=Image.new('RGB',(256,128),(243,192,138)); dd=ImageDraw.Draw(sd)
for i in range(128): dd.line((i*2,0,i*2,128),fill=(255,255,255) if i%2 else (150,90,40))
sd.save(TMP+'/side.png')
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene; sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=SM; sc.cycles.use_denoising=True; sc.cycles.use_adaptive_sampling=True
sc.render.resolution_y=RY; sc.render.resolution_x=int(RY*1080/1920); sc.render.image_settings.file_format='PNG'; sc.render.filepath=OUT
try: sc.view_settings.view_transform='AgX'
except Exception: pass
def mat(name,c,rough=.45,metal=0,emit=None,es=0,img=None):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; b=nt.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value=c; b.inputs['Roughness'].default_value=rough; b.inputs['Metallic'].default_value=metal
    if emit: b.inputs['Emission Color'].default_value=emit; b.inputs['Emission Strength'].default_value=es
    if img:
        t=nt.nodes.new('ShaderNodeTexImage'); t.image=bpy.data.images.load(img); nt.links.new(t.outputs[0],b.inputs['Base Color'])
    return m
floor=mat('floor',(.5,.56,.58,1),.14); steel=mat('steel',(.22,.28,.31,1),.5,.8); gold=mat('gold',(1,.62,.12,1),.2,1); red=mat('red',(.55,.01,.01,1),.3,0,(1,.02,.02,1),.0)
bill=mat('bill',(1,1,1,1),.6,0,None,0,TMP+'/bill.png'); side=mat('side',(1,1,1,1),.8,0,None,0,TMP+'/side.png'); band=mat('band',(.78,.6,.34,1),.8)
def obj(o,m): o.data.materials.append(m); return o
bpy.ops.mesh.primitive_plane_add(size=60); obj(bpy.context.object,floor)
# muro di cassette di sicurezza dietro
random.seed(3)
for r in range(7):
    for c in range(14):
        bpy.ops.mesh.primitive_cube_add(size=1,location=(-9.5+c*1.45,8.0,.6+r*1.02)); o=bpy.context.object; o.scale=(1.38,.3,.95); obj(o,steel)
# porta del caveau (disco) dietro a sinistra
bpy.ops.mesh.primitive_cylinder_add(radius=3.2,depth=.6,location=(-2.2,7.4,4.6),rotation=(math.radians(90),0,0)); obj(bpy.context.object,steel)
bpy.ops.mesh.primitive_torus_add(location=(-2.2,7.05,4.6),rotation=(math.radians(90),0,0),major_radius=3.2,minor_radius=.25); obj(bpy.context.object,gold)
# mazzetta di banconote
bpy.ops.mesh.primitive_cube_add(size=1,location=(0,0,.6)); st=bpy.context.object; st.scale=(2.7,1.4,1.2)
st.data.materials.append(side); st.data.materials.append(bill)
for p in st.data.polygons: p.material_index=1 if p.normal.z>.9 else 0
bpy.ops.mesh.primitive_cube_add(size=1,location=(0,0,.6)); b=bpy.context.object; b.scale=(.45,1.46,1.26); obj(b,band)
# banconote che volano via
random.seed(7)
for i in range(9):
    bpy.ops.mesh.primitive_plane_add(size=1,location=(random.uniform(-2.2,2.2),random.uniform(-.8,.6),random.uniform(1.6,4.6)),rotation=(random.uniform(.4,1.5),random.uniform(-.6,.6),random.uniform(0,6.2))); n=bpy.context.object; n.scale=(1.3,.65,1); obj(n,bill)
# testo "- 512 €" rosso 3D
bpy.ops.object.text_add(location=(0,-3.4,2.55)); tx=bpy.context.object; tx.data.body='- 512 €'; tx.data.font=bpy.data.fonts.load(FONT); tx.data.size=.78; tx.data.extrude=.2; tx.data.bevel_depth=.03; tx.data.align_x='CENTER'; tx.data.align_y='CENTER'; obj(tx,red); tx.rotation_euler=(math.radians(82),0,0)
# luci e mondo
bpy.ops.object.light_add(type='AREA',location=(-4,-6,7)); l=bpy.context.object; l.data.energy=650; l.data.size=6; l.rotation_euler=(math.radians(50),0,math.radians(-30))
bpy.ops.object.light_add(type='AREA',location=(5,-3,4)); l=bpy.context.object; l.data.energy=220; l.data.size=4; l.rotation_euler=(math.radians(60),0,math.radians(50))
w=bpy.data.worlds.new('w'); sc.world=w; w.use_nodes=True; w.node_tree.nodes['Background'].inputs[0].default_value=(.05,.14,.17,1); w.node_tree.nodes['Background'].inputs[1].default_value=.6
cd=bpy.data.cameras.new('c'); cd.lens=38; cd.sensor_fit='VERTICAL'; cd.sensor_width=36; cd.sensor_height=36; cam=bpy.data.objects.new('c',cd); bpy.context.collection.objects.link(cam); sc.camera=cam
cam.location=(.4,-9.0,4.2); tgt=Vector((0,0,float(os.environ.get('LOOKZ','1.3')))); cam.rotation_euler=(tgt-cam.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.render.render(write_still=True); print('FATTO',OUT)
