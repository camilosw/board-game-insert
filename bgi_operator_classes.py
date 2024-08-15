import bpy
from bpy.types import Operator
from bpy_extras.object_utils import object_data_add

from .node_factory import create_node, BGI_Node

class AddGameBox(Operator):
    bl_idname = "mesh.gbi_game_box_add"
    bl_label = "Game Box"
    bl_description = "Add the Game Box object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = bpy.data.meshes.new("GameBox")
        object_data_add(context, mesh, operator=None)
        bpy.context.object.show_wire = True

        create_node(BGI_Node.GAME_BOX)

        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = 0.0015
        bpy.context.object.modifiers["Solidify"].offset = 1
        bpy.context.object.modifiers["Solidify"].use_even_offset = True

        return {'FINISHED'}

class AddContainer(Operator):
    bl_idname = "mesh.gbi_container_add"
    bl_label = "Container"
    bl_description = "Add the Container object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = bpy.data.meshes.new("Container")
        object_data_add(context, mesh, operator=None)
        parent = bpy.context.object
        parent.show_wire = True
        
        create_node(BGI_Node.CONTAINER)
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
        plane.hide_render = True
        plane.hide_set(True)
        plane.parent = parent

        cut_top_modifier["Socket_2"] = plane

        bpy.ops.object.select_all(action='DESELECT')
        parent.select_set(True)
        bpy.context.view_layer.objects.active = parent

        return {'FINISHED'}

class AddCardHolderHorizontal(Operator):
    bl_idname = "mesh.gbi_card_holder_horizontal_add"
    bl_label = "Card Holder Horizontal"
    bl_description = "Add the Card Holder Horizontal object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mesh = bpy.data.meshes.new("CardHolderHorizontal")
        object_data_add(context, mesh, operator=None)
        parent = bpy.context.object
        parent.show_wire = True
        
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
        plane.hide_render = True
        plane.hide_set(True)
        plane.parent = parent

        cut_top_modifier["Socket_2"] = plane

        bpy.ops.object.select_all(action='DESELECT')
        parent.select_set(True)
        bpy.context.view_layer.objects.active = parent

        return {'FINISHED'}