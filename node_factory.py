import bpy
from enum import Enum

import bgi_game_box

import importlib

importlib.reload(bgi_game_box)

class BGI_Node(Enum):
    GAME_BOX = 'BGI Game Box'

def create_node(node: BGI_Node):
    if node.value in bpy.data.node_groups:
        return bpy.data.node_groups[node.value]
        
    match node:
        case BGI_Node.GAME_BOX:
            new_node = bgi_game_box.bgi_game_box_node_group()
        case _:
            raise NameError("Node group doesn't exist: " + node.value)
        
    modifiers = bpy.context.object.modifiers.new(name = "GeometryNodes", type = 'NODES')
    modifiers.node_group = new_node