import bpy
from enum import Enum

import bgi_game_box
import bgi_cut_top
import bgi_card_holder_horizontal

import importlib

importlib.reload(bgi_game_box)
importlib.reload(bgi_cut_top)
importlib.reload(bgi_card_holder_horizontal)

from bgi_game_box import bgi_game_box_node_group
from bgi_cut_top import bgi_cut_top_node_group
from bgi_card_holder_horizontal import bgi_card_holder_horizontal

class BGI_Node(Enum):
    GAME_BOX = 'BGI Game Box'
    CUT_TOP = 'BGI Cut Top'
    CARD_HOLDER_HORIZONTAL = 'BGI Card Holder Horizontal'

def create_node(node: BGI_Node):
    if node.value in bpy.data.node_groups:
        node_group = bpy.data.node_groups[node.value]
    else:
        match node:
            case BGI_Node.GAME_BOX:
                node_group = bgi_game_box_node_group()
            case BGI_Node.CUT_TOP:
                node_group = bgi_cut_top_node_group()
            case BGI_Node.CARD_HOLDER_HORIZONTAL:
                node_group = bgi_card_holder_horizontal()
            case _:
                raise NameError("Node group doesn't exist: " + node.value)
        
    modifier = bpy.context.object.modifiers.new(name = "GeometryNodes", type = 'NODES')
    modifier.node_group = node_group

    return modifier