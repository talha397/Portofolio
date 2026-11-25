"""
Builds the PLACEHOLDER scene for the portfolio and exports it as web/public/models/me.glb.

It is a stand-in until Talha's real head scan is ready. Open `placeholder.blend`
(made by this script) in Blender to see the exact structure the website needs:

  Camera            camera whose animation is named "CameraAction"
                    frame 0 = hero, frames 50/100/150/200/250 = résumé stops,
                    frames 250-350 = projects section
  focus-0           hero focus point (between the eyes)
  focus-1..focus-5  one focus point per résumé entry (the camera looks at these)
  focus-works       focus point for the projects section
  eye_L / eye_R     eyes: any mesh with "eye" in its name follows the cursor.
                    Their ORIGIN must be the centre of the eyeball.

Run it headless (from the repo root):
  blender --background --python blender/build_placeholder.py
"""
import math
import os

import bpy
from mathutils import Vector

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GLB_OUT = os.path.join(ROOT, "web", "public", "models", "me.glb")
BLEND_OUT = os.path.join(ROOT, "blender", "placeholder.blend")

# Head = an ellipsoid. Blender is Z-up and the face looks toward -Y.
HEAD_C = Vector((0.0, 0.0, 0.45))
HEAD_R = Vector((0.33, 0.31, 0.38))  # radii x, y, z

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.fps = 24
scene.frame_start = 0
scene.frame_end = 350


def material(name, color, roughness=0.6):
    m = bpy.data.materials.new(name)
    bsdf = m.node_tree.nodes.get("Principled BSDF") if m.use_nodes else None
    if bsdf is None:
        m.use_nodes = True
        bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = roughness
    return m


def smooth(obj):
    for p in obj.data.polygons:
        p.use_smooth = True


def surface_point(theta_deg, phi_deg, lift=0.0):
    """Point on the head ellipsoid. theta = left/right angle from the front (+ = model's left / screen right),
    phi = up/down angle (+ = up). Returns (point, outward normal)."""
    t, p = math.radians(theta_deg), math.radians(phi_deg)
    d = Vector((math.sin(t) * math.cos(p), -math.cos(t) * math.cos(p), math.sin(p)))
    pt = Vector((d.x * HEAD_R.x, d.y * HEAD_R.y, d.z * HEAD_R.z))
    n = Vector((pt.x / HEAD_R.x**2, pt.y / HEAD_R.y**2, pt.z / HEAD_R.z**2)).normalized()
    return HEAD_C + pt + n * lift, n


skin = material("skin", (0.80, 0.58, 0.45), 0.55)
white = material("eye_white", (0.95, 0.95, 0.93), 0.25)
black = material("pupil", (0.02, 0.02, 0.02), 0.2)
cap_mat = material("grad_cap", (0.03, 0.03, 0.05), 0.5)
gold = material("tassel", (0.95, 0.72, 0.15), 0.35)

# ---------- Head (swap this for the scan later) ----------
bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=1, location=HEAD_C)
head = bpy.context.object
head.name = "head"
head.scale = HEAD_R
bpy.ops.object.transform_apply(scale=True)
head.data.materials.append(skin)
smooth(head)

bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.07, location=(0, -0.33, 0.36))
nose = bpy.context.object
nose.name = "nose"
nose.scale = (0.7, 0.8, 1.0)
nose.data.materials.append(skin)
smooth(nose)

for side in (-1, 1):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=0.07, location=(side * 0.33, 0.0, 0.42))
    ear = bpy.context.object
    ear.name = "ear_L" if side > 0 else "ear_R"
    ear.scale = (0.4, 0.8, 1.2)
    ear.data.materials.append(skin)
    smooth(ear)

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.13, depth=0.35, location=(0, 0.02, 0.02))
neck = bpy.context.object
neck.name = "neck"
neck.data.materials.append(skin)
smooth(neck)

bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=1, location=(0, 0.04, -0.32))
shoulders = bpy.context.object
shoulders.name = "shoulders"
shoulders.scale = (0.62, 0.3, 0.26)
shoulders.data.materials.append(material("shirt", (0.15, 0.22, 0.35), 0.8))
smooth(shoulders)

# ---------- Eyes (googly). Origin = eyeball centre, pupil faces -Y (forward) ----------
for name, x in (("eye_R", -0.115), ("eye_L", 0.115)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=0.065, location=(x, -0.265, 0.49))
    eye = bpy.context.object
    eye.name = name
    eye.data.materials.append(white)
    eye.data.materials.append(black)
    for poly in eye.data.polygons:
        poly.use_smooth = True
        if poly.normal.y < -0.86:  # front cap = pupil
            poly.material_index = 1

# ---------- Graduation cap ----------
cap_pos, cap_n = surface_point(0, 72, lift=0.02)
bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=0.2, depth=0.1, location=cap_pos - cap_n * 0.02)
cap_base = bpy.context.object
cap_base.name = "grad-cap-base"
cap_base.data.materials.append(cap_mat)
bpy.ops.mesh.primitive_cube_add(size=1, location=cap_pos + Vector((0, 0, 0.05)))
board = bpy.context.object
board.name = "grad-cap-board"
board.scale = (0.5, 0.5, 0.02)
board.rotation_euler = (math.radians(-8), 0, math.radians(45))
board.data.materials.append(cap_mat)
bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.008, depth=0.22,
                                    location=cap_pos + Vector((0.3, -0.12, -0.04)))
tassel = bpy.context.object
tassel.name = "grad-cap-tassel"
tassel.data.materials.append(gold)

# ---------- Placeholder stickers (round discs; real sticker images come later) ----------
STICKERS = [
    # name,        theta, phi, colour,             radius
    ("sticker-1", 55, 5, (0.95, 0.35, 0.30), 0.07),     # undergrad
    ("sticker-2", 40, -28, (0.30, 0.60, 0.95), 0.065),  # grad program
    ("sticker-3", -55, 8, (0.40, 0.85, 0.45), 0.07),    # research
    ("sticker-4", -38, -30, (0.98, 0.80, 0.25), 0.06),  # experience
]
for name, theta, phi, col, r in STICKERS:
    pos, n = surface_point(theta, phi, lift=0.004)
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=r, depth=0.006, location=pos)
    st = bpy.context.object
    st.name = name
    st.rotation_mode = "QUATERNION"
    st.rotation_quaternion = n.to_track_quat("Z", "Y")
    st.data.materials.append(material(name, col, 0.4))

# ---------- Focus points (empties) ----------
FOCUS = {
    "focus-0": (Vector((0, -0.31, 0.47)), None),
    "focus-1": surface_point(55, 5),
    "focus-2": surface_point(40, -28),
    "focus-3": surface_point(-55, 8),
    "focus-4": surface_point(-38, -30),
    "focus-5": (cap_pos + Vector((0, 0, 0.05)), None),
    "focus-works": (Vector((0, -0.3, 0.4)), None),
}
for name, (pos, _n) in FOCUS.items():
    e = bpy.data.objects.new(name, None)
    e.empty_display_type = "SPHERE"
    e.empty_display_size = 0.02
    e.location = pos
    scene.collection.objects.link(e)

# ---------- Camera + CameraAction ----------
cam_data = bpy.data.cameras.new("Camera")
cam_data.lens = 55
cam = bpy.data.objects.new("Camera", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam.rotation_mode = "QUATERNION"


def cam_from(target, n=None, dist=1.0, offset=Vector((0, 0, 0))):
    """Camera position looking at `target` from `dist` along the surface normal (or straight on)."""
    direction = (n if n is not None else Vector((0, -1, 0))).copy()
    direction.normalize()
    return target + direction * dist + offset


def f(name):
    return FOCUS[name][0]


KEYS = [
    # frame, camera position,                                          look at
    (0,   Vector((0.0, -4.2, 0.45)),                                       f("focus-0")),
    (50,  cam_from(f("focus-1"), FOCUS["focus-1"][1], 1.35, Vector((0.05, -0.2, 0.05))), f("focus-1")),
    (100, cam_from(f("focus-2"), FOCUS["focus-2"][1], 1.35, Vector((0.0, -0.2, 0.0))),   f("focus-2")),
    (150, cam_from(f("focus-3"), FOCUS["focus-3"][1], 1.35, Vector((-0.05, -0.2, 0.05))), f("focus-3")),
    (200, cam_from(f("focus-4"), FOCUS["focus-4"][1], 1.35, Vector((0.0, -0.2, 0.0))),   f("focus-4")),
    (250, Vector((0.7, -2.0, 1.7)),                                        f("focus-5")),
    (300, Vector((-0.5, -3.6, 0.7)),                                       f("focus-works")),
    (350, Vector((1.3, -3.4, 0.6)),                                        f("focus-works")),
]
prev_q = None
for frame, loc, target in KEYS:
    q = (target - loc).to_track_quat("-Z", "Y")
    if prev_q is not None and prev_q.dot(q) < 0:  # keep quaternions on one hemisphere
        q.negate()
    prev_q = q
    cam.location = loc
    cam.rotation_quaternion = q
    cam.keyframe_insert("location", frame=frame)
    cam.keyframe_insert("rotation_quaternion", frame=frame)
cam.animation_data.action.name = "CameraAction"

# A light so the .blend looks right when you open it (not exported to the website).
light = bpy.data.objects.new("Key light", bpy.data.lights.new("Key light", "AREA"))
light.location = (1.5, -2.5, 2.0)
light.data.energy = 300
scene.collection.objects.link(light)

scene.frame_set(0)
bpy.ops.wm.save_as_mainfile(filepath=BLEND_OUT)
os.makedirs(os.path.dirname(GLB_OUT), exist_ok=True)
bpy.ops.export_scene.gltf(
    filepath=GLB_OUT,
    export_format="GLB",
    export_cameras=True,
    export_lights=False,
    export_animations=True,
    export_yup=True,
    export_apply=True,
)
print("Saved", BLEND_OUT, "and", GLB_OUT)
