import bpy
from bpy.types import Operator
from bpy_extras.object_utils import object_data_add

import node_factory

import importlib

importlib.reload(node_factory)

from node_factory import create_node, BGI_Node

class AddGameBox(Operator):
    bl_idname = "mesh.game_box_add"
    bl_label = "Game Box"
    bl_description = "Add the Game Box object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = bpy.data.meshes.new("GameBox")
        object_data_add(context, mesh, operator=None)

        create_node(BGI_Node.GAME_BOX)

        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.0015
        bpy.context.object.modifiers["Solidify"].offset = 1
        bpy.context.object.modifiers["Solidify"].use_even_offset = True

        return {'FINISHED'}
    
class AddCardHolderHorizontal(Operator):
    bl_idname = "mesh.card_holder_horizontal_add"
    bl_label = "Card Holder Horizontal"
    bl_description = "Add the Card Holder Horizontal object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = bpy.data.meshes.new("CardHolderHorizontal")
        object_data_add(context, mesh, operator=None)
        parent = bpy.context.object
        
        create_node(BGI_Node.CARD_HOLDER_HORIZONTAL)
        cut_top_modifier = create_node(BGI_Node.CUT_TOP)

        bpy.ops.mesh.primitive_plane_add(size=0.5, 
                                enter_editmode=False, 
                                align='WORLD', 
                                location=(0, 0, 0.01),
                                scale=(1, 1, 1))

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        bpy.ops.mesh.flip_normals()
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        plane = bpy.context.object
        plane.name = 'CutPlane'
        plane.data.name = 'CutPlane'
        plane.display_type = 'WIRE'
        plane.parent = parent
        plane.hide_set(True)

        cut_top_modifier["Socket_2"] = plane

        return {'FINISHED'}