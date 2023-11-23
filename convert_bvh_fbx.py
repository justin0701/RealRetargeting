<<<<<<< HEAD
##Convert bvh to fbx Code
=======
>>>>>>> 966c7c33f42ca0325c1486fa86446279ff2a7323
import bpy
import argparse


parser = argparse.ArgumentParser()
<<<<<<< HEAD
parser.add_argument('--bvh_path',type=str,default="./.bvh") #Your bvh 
=======
parser.add_argument('--bvh_path',type=str,default="./.bvh") #Your bvh
>>>>>>> 966c7c33f42ca0325c1486fa86446279ff2a7323
parser.add_argument('--fbx_path',type=str,default="./.fbx") #Export fbx

args = parser.parse_args()

# 씬 셋팅
bpy.ops.wm.read_factory_settings(use_empty=True)

# Bvh file
bpy.ops.import_anim.bvh(filepath=args.bvh_path)

# Export to FBX
bpy.ops.export_scene.fbx(filepath=args.fbx_path, use_selection=True)

scene = bpy.context.scene
for obj in scene.objects:
    if obj.type == 'ARMATURE':
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='DESELECT')
        bpy.ops.armature.select_all(action='SELECT')
        bpy.ops.armature.delete(type='PREVIOUS')
        bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.wm.link_remove(1) 


