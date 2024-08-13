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