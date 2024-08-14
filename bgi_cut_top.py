import bpy

#initialize bgi_cut_top node group
def bgi_cut_top_node_group():
    bgi_cut_top = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Cut Top")

    bgi_cut_top.is_modifier = True
    
    #initialize bgi_cut_top nodes
    #bgi_cut_top interface
    #Socket Geometry
    geometry_socket = bgi_cut_top.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    
    #Socket Geometry
    geometry_socket_1 = bgi_cut_top.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    
    #Socket Cut Object
    cut_object_socket = bgi_cut_top.interface.new_socket(name = "Cut Object", in_out='INPUT', socket_type = 'NodeSocketObject')
    cut_object_socket.attribute_domain = 'POINT'
    
    #Socket Enable
    enable_socket = bgi_cut_top.interface.new_socket(name = "Enable", in_out='INPUT', socket_type = 'NodeSocketBool')
    enable_socket.attribute_domain = 'POINT'
    
    
    #node Mesh Boolean
    mesh_boolean = bgi_cut_top.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    #Self Intersection
    mesh_boolean.inputs[2].default_value = True
    #Hole Tolerant
    mesh_boolean.inputs[3].default_value = False
    
    #node Switch
    switch = bgi_cut_top.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'
    
    #node Group Output
    group_output = bgi_cut_top.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    #node Group Input.001
    group_input_001 = bgi_cut_top.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[1].hide = True
    group_input_001.outputs[3].hide = True
    
    #node Realize Instances
    realize_instances = bgi_cut_top.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    
    #node Object Info
    object_info = bgi_cut_top.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'RELATIVE'
    #As Instance
    object_info.inputs[1].default_value = False
    
    #node Group Input
    group_input = bgi_cut_top.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    
    #Set locations
    mesh_boolean.location = (0.0, 77.33333587646484)
    switch.location = (212.6666717529297, 0.0)
    group_output.location = (386.6666564941406, 0.0)
    group_input_001.location = (0.0, -135.3333282470703)
    realize_instances.location = (-193.3333282470703, 77.33333587646484)
    object_info.location = (-193.3333282470703, -19.33333396911621)
    group_input.location = (-406.0, 0.0)
    
    #Set dimensions
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    
    #initialize bgi_cut_top links
    #realize_instances.Geometry -> mesh_boolean.Mesh 1
    bgi_cut_top.links.new(realize_instances.outputs[0], mesh_boolean.inputs[0])
    #object_info.Geometry -> mesh_boolean.Mesh 2
    bgi_cut_top.links.new(object_info.outputs[3], mesh_boolean.inputs[1])
    #switch.Output -> group_output.Geometry
    bgi_cut_top.links.new(switch.outputs[0], group_output.inputs[0])
    #group_input.Geometry -> realize_instances.Geometry
    bgi_cut_top.links.new(group_input.outputs[0], realize_instances.inputs[0])
    #group_input.Cut Object -> object_info.Object
    bgi_cut_top.links.new(group_input.outputs[1], object_info.inputs[0])
    #mesh_boolean.Mesh -> switch.True
    bgi_cut_top.links.new(mesh_boolean.outputs[0], switch.inputs[2])
    #group_input_001.Enable -> switch.Switch
    bgi_cut_top.links.new(group_input_001.outputs[2], switch.inputs[0])
    #group_input_001.Geometry -> switch.False
    bgi_cut_top.links.new(group_input_001.outputs[0], switch.inputs[1])
    return bgi_cut_top

