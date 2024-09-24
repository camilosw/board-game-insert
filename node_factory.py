import bpy
from enum import Enum

from .bgi_game_box import bgi_game_box_node_group
from .bgi_cut_top import bgi_cut_top_node_group
from .bgi_container import bgi_container_create
from .bgi_grid_container import bgi_grid_container_create
from .bgi_card_holder import bgi_card_holder_create

class BGI_Node(Enum):
    GAME_BOX = 'BGI Game Box'
    CUT_TOP = 'BGI Cut Top'
    CONTAINER = 'BGI Container'
    GRID_CONTAINER = 'BGI Grid Container'
    CARD_HOLDER = 'BGI Card Holder'

def create_node(node: BGI_Node):
    if node.value in bpy.data.node_groups:
        node_group = bpy.data.node_groups[node.value]
    else:
        match node:
            case BGI_Node.GAME_BOX:
                node_group = bgi_game_box_node_group()
            case BGI_Node.CUT_TOP:
                node_group = bgi_cut_top_node_group()
            case BGI_Node.CONTAINER:
                node_group = bgi_container_create()
            case BGI_Node.GRID_CONTAINER:
                node_group = bgi_grid_container_create()
            case BGI_Node.CARD_HOLDER:
                node_group = bgi_card_holder_create()
            case _:
                raise NameError("Node group doesn't exist: " + node.value)
        
    modifier = bpy.context.object.modifiers.new(name = "GeometryNodes", type = 'NODES')
    modifier.node_group = node_group

    return modifier