bl_info = {
    "name": "Board Game Insert",
    "author": "Camilo Mejia",
    "version": (1, 0),
    "blender": (3, 60, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds objects to create board game inserts",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

from . import bgi_operator_classes

import bpy
from bpy.types import Menu

class VIEW3D_MT_board_game_insert_add(Menu):
    bl_idname = "VIEW3D_MT_board_game_insert_add"
    bl_label = "Board Game Insert"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        layout.operator("mesh.gbi_game_box_add",
                        text="Game Box")
        layout.operator("mesh.gbi_container_add",
                        text="Container")
        layout.operator("mesh.gbi_card_holder_horizontal_add",
                        text="Card Holder Horizontal")

def menu_func(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'

    layout.separator()
    layout.menu("VIEW3D_MT_board_game_insert_add",
                text="Board Game Insert", icon="DECORATE")

classes = [
    bgi_operator_classes.AddGameBox,
    bgi_operator_classes.AddContainer,
    bgi_operator_classes.AddCardHolderHorizontal,
    VIEW3D_MT_board_game_insert_add
]

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()