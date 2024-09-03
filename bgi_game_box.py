import bpy

#initialize bgi_game_box node group
def bgi_game_box_node_group():
    bgi_game_box = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Game Box")

    bgi_game_box.is_modifier = True
    
    #bgi_game_box interface
    #Socket Geometry
    geometry_socket = bgi_game_box.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    
    #Socket Geometry
    geometry_socket_1 = bgi_game_box.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    
    #Socket Width
    width_socket = bgi_game_box.interface.new_socket(name = "Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
    width_socket.subtype = 'DISTANCE'
    width_socket.default_value = 0.30000001192092896
    width_socket.min_value = 0.0
    width_socket.max_value = 3.4028234663852886e+38
    width_socket.attribute_domain = 'POINT'
    
    #Socket Height
    height_socket = bgi_game_box.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    height_socket.subtype = 'DISTANCE'
    height_socket.default_value = 0.30000001192092896
    height_socket.min_value = 0.0
    height_socket.max_value = 3.4028234663852886e+38
    height_socket.attribute_domain = 'POINT'
    
    #Socket Depth
    depth_socket = bgi_game_box.interface.new_socket(name = "Depth", in_out='INPUT', socket_type = 'NodeSocketFloat')
    depth_socket.subtype = 'DISTANCE'
    depth_socket.default_value = 0.07000000029802322
    depth_socket.min_value = 0.0
    depth_socket.max_value = 3.4028234663852886e+38
    depth_socket.attribute_domain = 'POINT'
    
    
    #initialize bgi_game_box nodes
    #node Compare
    compare = bgi_game_box.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_THAN'
    #B
    compare.inputs[1].default_value = 0.0
    
    #node Combine XYZ
    combine_xyz = bgi_game_box.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    
    #node Cube
    cube = bgi_game_box.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    #Vertices X
    cube.inputs[1].default_value = 2
    #Vertices Y
    cube.inputs[2].default_value = 2
    #Vertices Z
    cube.inputs[3].default_value = 2
    
    #node Attribute Statistic
    attribute_statistic = bgi_game_box.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'POINT'
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.inputs[2].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[3].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[5].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    #Selection
    attribute_statistic.inputs[1].default_value = True
    #Attribute
    attribute_statistic.inputs[2].default_value = (0.0, 0.0, 0.0)
    
    #node Math
    math = bgi_game_box.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 2.0
    
    #node Combine XYZ.001
    combine_xyz_001 = bgi_game_box.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #X
    combine_xyz_001.inputs[0].default_value = 0.0
    #Y
    combine_xyz_001.inputs[1].default_value = 0.0
    
    #node Vector Math
    vector_math = bgi_game_box.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ADD'
    
    #node Delete Geometry
    delete_geometry = bgi_game_box.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'
    
    #node Set Position
    set_position = bgi_game_box.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True
    #Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
    
    #node Group Output
    group_output = bgi_game_box.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    #node Group Input
    group_input = bgi_game_box.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    
    #node Normal
    normal = bgi_game_box.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    
    #node Vector Math.001
    vector_math_001 = bgi_game_box.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'DOT_PRODUCT'
    #Vector_001
    vector_math_001.inputs[1].default_value = (0.0, 0.0, 1.0)
    
    
    
    
    #Set locations
    compare.location = (38.66666793823242, 367.3333435058594)
    combine_xyz.location = (-135.3333282470703, 154.6666717529297)
    cube.location = (38.66666793823242, 174.0)
    attribute_statistic.location = (-135.3333282470703, -19.33333396911621)
    math.location = (-135.3333282470703, -174.0)
    combine_xyz_001.location = (38.66666793823242, -174.0)
    vector_math.location = (232.0, -19.33333396911621)
    delete_geometry.location = (232.0, 309.3333435058594)
    set_position.location = (440.0, 140.0)
    group_output.location = (620.0, 140.0)
    group_input.location = (-367.3333435058594, 58.0)
    normal.location = (-367.3333435058594, 367.3333435058594)
    vector_math_001.location = (-135.3333282470703, 367.3333435058594)
    
    #Set dimensions
    compare.width, compare.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    
    #initialize bgi_game_box links
    #combine_xyz.Vector -> cube.Size
    bgi_game_box.links.new(combine_xyz.outputs[0], cube.inputs[0])
    #group_input.Width -> combine_xyz.X
    bgi_game_box.links.new(group_input.outputs[1], combine_xyz.inputs[0])
    #group_input.Height -> combine_xyz.Y
    bgi_game_box.links.new(group_input.outputs[2], combine_xyz.inputs[1])
    #group_input.Depth -> combine_xyz.Z
    bgi_game_box.links.new(group_input.outputs[3], combine_xyz.inputs[2])
    #group_input.Depth -> math.Value
    bgi_game_box.links.new(group_input.outputs[3], math.inputs[0])
    #set_position.Geometry -> group_output.Geometry
    bgi_game_box.links.new(set_position.outputs[0], group_output.inputs[0])
    #vector_math.Vector -> set_position.Offset
    bgi_game_box.links.new(vector_math.outputs[0], set_position.inputs[3])
    #math.Value -> combine_xyz_001.Z
    bgi_game_box.links.new(math.outputs[0], combine_xyz_001.inputs[2])
    #group_input.Geometry -> attribute_statistic.Geometry
    bgi_game_box.links.new(group_input.outputs[0], attribute_statistic.inputs[0])
    #combine_xyz_001.Vector -> vector_math.Vector
    bgi_game_box.links.new(combine_xyz_001.outputs[0], vector_math.inputs[1])
    #attribute_statistic.Median -> vector_math.Vector
    bgi_game_box.links.new(attribute_statistic.outputs[1], vector_math.inputs[0])
    #cube.Mesh -> delete_geometry.Geometry
    bgi_game_box.links.new(cube.outputs[0], delete_geometry.inputs[0])
    #delete_geometry.Geometry -> set_position.Geometry
    bgi_game_box.links.new(delete_geometry.outputs[0], set_position.inputs[0])
    #normal.Normal -> vector_math_001.Vector
    bgi_game_box.links.new(normal.outputs[0], vector_math_001.inputs[0])
    #vector_math_001.Value -> compare.A
    bgi_game_box.links.new(vector_math_001.outputs[1], compare.inputs[0])
    #compare.Result -> delete_geometry.Selection
    bgi_game_box.links.new(compare.outputs[0], delete_geometry.inputs[1])
    return bgi_game_box
