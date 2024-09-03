import bpy

from .bgi_divisor import bgi_divisor_create

#initialize bgi_grid_container node group
def bgi_grid_container_node_group(bgi_divisor):
	bgi_grid_container = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Grid Container")

	bgi_grid_container.is_modifier = True
	
	#bgi_grid_container interface
	#Socket Geometry
	geometry_socket_1 = bgi_grid_container.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_1.attribute_domain = 'POINT'
	
	#Socket Inner Width
	inner_width_socket = bgi_grid_container.interface.new_socket(name = "Inner Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_width_socket.subtype = 'DISTANCE'
	inner_width_socket.default_value = 0.10000000149011612
	inner_width_socket.min_value = 0.0
	inner_width_socket.max_value = 3.4028234663852886e+38
	inner_width_socket.attribute_domain = 'POINT'
	inner_width_socket.force_non_field = True
	
	#Socket Inner Length
	inner_length_socket = bgi_grid_container.interface.new_socket(name = "Inner Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_length_socket.subtype = 'DISTANCE'
	inner_length_socket.default_value = 0.10000000149011612
	inner_length_socket.min_value = 0.0
	inner_length_socket.max_value = 3.4028234663852886e+38
	inner_length_socket.attribute_domain = 'POINT'
	inner_length_socket.force_non_field = True
	
	#Socket Inner Height
	inner_height_socket = bgi_grid_container.interface.new_socket(name = "Inner Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_height_socket.subtype = 'DISTANCE'
	inner_height_socket.default_value = 0.05000000074505806
	inner_height_socket.min_value = 0.0
	inner_height_socket.max_value = 3.4028234663852886e+38
	inner_height_socket.attribute_domain = 'POINT'
	inner_height_socket.force_non_field = True
	
	#Socket Tickness
	tickness_socket = bgi_grid_container.interface.new_socket(name = "Tickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	tickness_socket.subtype = 'DISTANCE'
	tickness_socket.default_value = 0.005000000353902578
	tickness_socket.min_value = 0.0
	tickness_socket.max_value = 3.4028234663852886e+38
	tickness_socket.attribute_domain = 'POINT'
	tickness_socket.force_non_field = True
	
	#Socket Count Width
	count_width_socket = bgi_grid_container.interface.new_socket(name = "Count Width", in_out='INPUT', socket_type = 'NodeSocketInt')
	count_width_socket.subtype = 'NONE'
	count_width_socket.default_value = 1
	count_width_socket.min_value = 1
	count_width_socket.max_value = 2147483647
	count_width_socket.attribute_domain = 'POINT'
	count_width_socket.force_non_field = True
	
	#Socket Count Length
	count_length_socket = bgi_grid_container.interface.new_socket(name = "Count Length", in_out='INPUT', socket_type = 'NodeSocketInt')
	count_length_socket.subtype = 'NONE'
	count_length_socket.default_value = 1
	count_length_socket.min_value = 1
	count_length_socket.max_value = 2147483647
	count_length_socket.attribute_domain = 'POINT'
	count_length_socket.force_non_field = True
	
	#Socket Cut Side 1
	cut_side_1_socket = bgi_grid_container.interface.new_socket(name = "Cut Side 1", in_out='INPUT', socket_type = 'NodeSocketBool')
	cut_side_1_socket.attribute_domain = 'POINT'
	cut_side_1_socket.force_non_field = True
	
	#Socket Cut Side 2
	cut_side_2_socket = bgi_grid_container.interface.new_socket(name = "Cut Side 2", in_out='INPUT', socket_type = 'NodeSocketBool')
	cut_side_2_socket.attribute_domain = 'POINT'
	cut_side_2_socket.force_non_field = True
	
	#Socket Cut inner
	cut_inner_socket = bgi_grid_container.interface.new_socket(name = "Cut inner", in_out='INPUT', socket_type = 'NodeSocketBool')
	cut_inner_socket.attribute_domain = 'POINT'
	cut_inner_socket.force_non_field = True
	
	#Socket Cut Size Top
	cut_size_top_socket = bgi_grid_container.interface.new_socket(name = "Cut Size Top", in_out='INPUT', socket_type = 'NodeSocketFloat')
	cut_size_top_socket.subtype = 'DISTANCE'
	cut_size_top_socket.default_value = 0.029999999329447746
	cut_size_top_socket.min_value = 0.0010000000474974513
	cut_size_top_socket.max_value = 3.4028234663852886e+38
	cut_size_top_socket.attribute_domain = 'POINT'
	cut_size_top_socket.force_non_field = True
	
	#Socket Cut Size Bottom
	cut_size_bottom_socket = bgi_grid_container.interface.new_socket(name = "Cut Size Bottom", in_out='INPUT', socket_type = 'NodeSocketFloat')
	cut_size_bottom_socket.subtype = 'DISTANCE'
	cut_size_bottom_socket.default_value = 0.019999999552965164
	cut_size_bottom_socket.min_value = 0.0
	cut_size_bottom_socket.max_value = 3.4028234663852886e+38
	cut_size_bottom_socket.attribute_domain = 'POINT'
	cut_size_bottom_socket.force_non_field = True
	
	
	#initialize bgi_grid_container nodes
	#node Frame.001
	frame_001_1 = bgi_grid_container.nodes.new("NodeFrame")
	frame_001_1.label = "Divisions location X direction"
	frame_001_1.name = "Frame.001"
	frame_001_1.label_size = 20
	frame_001_1.shrink = True
	
	#node Frame.002
	frame_002 = bgi_grid_container.nodes.new("NodeFrame")
	frame_002.label = "Containers division"
	frame_002.name = "Frame.002"
	frame_002.label_size = 20
	frame_002.shrink = True
	
	#node Frame.003
	frame_003_1 = bgi_grid_container.nodes.new("NodeFrame")
	frame_003_1.label = "Outside sides"
	frame_003_1.name = "Frame.003"
	frame_003_1.label_size = 20
	frame_003_1.shrink = True
	
	#node Frame.005
	frame_005 = bgi_grid_container.nodes.new("NodeFrame")
	frame_005.label = "Select cut sides"
	frame_005.name = "Frame.005"
	frame_005.label_size = 20
	frame_005.shrink = True
	
	#node Frame.006
	frame_006 = bgi_grid_container.nodes.new("NodeFrame")
	frame_006.label = "Position cut shapes"
	frame_006.name = "Frame.006"
	frame_006.label_size = 20
	frame_006.shrink = True
	
	#node Frame.004
	frame_004 = bgi_grid_container.nodes.new("NodeFrame")
	frame_004.label = "Sides cut shape"
	frame_004.name = "Frame.004"
	frame_004.label_size = 20
	frame_004.shrink = True
	
	#node Frame
	frame_1 = bgi_grid_container.nodes.new("NodeFrame")
	frame_1.label = "Base"
	frame_1.name = "Frame"
	frame_1.label_size = 20
	frame_1.shrink = True
	
	#node Reroute.008
	reroute_008 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_008.name = "Reroute.008"
	#node Math.017
	math_017 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_017.name = "Math.017"
	math_017.operation = 'MULTIPLY'
	math_017.use_clamp = False
	
	#node Math.018
	math_018 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_018.name = "Math.018"
	math_018.operation = 'MULTIPLY'
	math_018.use_clamp = False
	#Value_001
	math_018.inputs[1].default_value = -1.0
	
	#node Combine XYZ.003
	combine_xyz_003 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_003.name = "Combine XYZ.003"
	#Y
	combine_xyz_003.inputs[1].default_value = 0.0
	#Z
	combine_xyz_003.inputs[2].default_value = 0.0
	
	#node Group Input.003
	group_input_003_1 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_003_1.name = "Group Input.003"
	group_input_003_1.outputs[0].hide = True
	group_input_003_1.outputs[1].hide = True
	group_input_003_1.outputs[2].hide = True
	group_input_003_1.outputs[3].hide = True
	group_input_003_1.outputs[5].hide = True
	group_input_003_1.outputs[6].hide = True
	group_input_003_1.outputs[7].hide = True
	group_input_003_1.outputs[8].hide = True
	group_input_003_1.outputs[9].hide = True
	group_input_003_1.outputs[10].hide = True
	group_input_003_1.outputs[11].hide = True
	
	#node Mesh Line
	mesh_line = bgi_grid_container.nodes.new("GeometryNodeMeshLine")
	mesh_line.name = "Mesh Line"
	mesh_line.count_mode = 'TOTAL'
	mesh_line.mode = 'OFFSET'
	#Start Location
	mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Combine XYZ.002
	combine_xyz_002_1 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_002_1.name = "Combine XYZ.002"
	#Y
	combine_xyz_002_1.inputs[1].default_value = 0.0
	#Z
	combine_xyz_002_1.inputs[2].default_value = 0.0
	
	#node Math.007
	math_007 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_007.name = "Math.007"
	math_007.operation = 'DIVIDE'
	math_007.use_clamp = False
	#Value_001
	math_007.inputs[1].default_value = 2.0
	
	#node Math.014
	math_014 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_014.name = "Math.014"
	math_014.operation = 'ADD'
	math_014.use_clamp = False
	
	#node Math.009
	math_009_1 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_009_1.name = "Math.009"
	math_009_1.operation = 'ADD'
	math_009_1.use_clamp = False
	
	#node Math.008
	math_008 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_008.name = "Math.008"
	math_008.operation = 'ADD'
	math_008.use_clamp = False
	#Value_001
	math_008.inputs[1].default_value = 1.0
	
	#node Transform Geometry.001
	transform_geometry_001 = bgi_grid_container.nodes.new("GeometryNodeTransform")
	transform_geometry_001.name = "Transform Geometry.001"
	#Rotation
	transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Mesh to Points
	mesh_to_points = bgi_grid_container.nodes.new("GeometryNodeMeshToPoints")
	mesh_to_points.name = "Mesh to Points"
	mesh_to_points.mode = 'VERTICES'
	#Selection
	mesh_to_points.inputs[1].default_value = True
	#Position
	mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Radius
	mesh_to_points.inputs[3].default_value = 0.0020000000949949026
	
	#node Reroute.007
	reroute_007 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_007.name = "Reroute.007"
	#node Group
	group = bgi_grid_container.nodes.new("GeometryNodeGroup")
	group.name = "Group"
	group.node_tree = bgi_divisor
	#Input_3
	group.inputs[0].default_value = 0.0
	#Input_4
	group.inputs[4].default_value = False
	#Input_6
	group.inputs[5].default_value = True
	#Input_9
	group.inputs[6].default_value = 2
	
	#node Index
	index = bgi_grid_container.nodes.new("GeometryNodeInputIndex")
	index.name = "Index"
	
	#node Math.012
	math_012 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_012.name = "Math.012"
	math_012.operation = 'ADD'
	math_012.use_clamp = False
	#Value_001
	math_012.inputs[1].default_value = 1.0
	
	#node Math.011
	math_011 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_011.name = "Math.011"
	math_011.operation = 'MODULO'
	math_011.use_clamp = False
	#Value_001
	math_011.inputs[1].default_value = 2.0
	
	#node Instance on Points
	instance_on_points = bgi_grid_container.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points.name = "Instance on Points"
	#Pick Instance
	instance_on_points.inputs[3].default_value = False
	#Instance Index
	instance_on_points.inputs[4].default_value = 0
	#Rotation
	instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.004
	combine_xyz_004 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_004.name = "Combine XYZ.004"
	#X
	combine_xyz_004.inputs[0].default_value = 0.0
	#Z
	combine_xyz_004.inputs[2].default_value = 0.0
	
	#node Vector Math
	vector_math = bgi_grid_container.nodes.new("ShaderNodeVectorMath")
	vector_math.name = "Vector Math"
	vector_math.operation = 'MULTIPLY'
	#Vector_001
	vector_math.inputs[1].default_value = (1.0, -1.0, 1.0)
	
	#node Math.013
	math_013 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_013.name = "Math.013"
	math_013.operation = 'MODULO'
	math_013.use_clamp = False
	#Value_001
	math_013.inputs[1].default_value = 2.0
	
	#node Group.001
	group_001 = bgi_grid_container.nodes.new("GeometryNodeGroup")
	group_001.name = "Group.001"
	group_001.node_tree = bgi_divisor
	#Input_2
	group_001.inputs[1].default_value = 0.0
	#Input_4
	group_001.inputs[4].default_value = True
	#Input_6
	group_001.inputs[5].default_value = False
	#Input_9
	group_001.inputs[6].default_value = 2
	
	#node Index.001
	index_001 = bgi_grid_container.nodes.new("GeometryNodeInputIndex")
	index_001.name = "Index.001"
	
	#node Instance on Points.001
	instance_on_points_001 = bgi_grid_container.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points_001.name = "Instance on Points.001"
	#Pick Instance
	instance_on_points_001.inputs[3].default_value = False
	#Instance Index
	instance_on_points_001.inputs[4].default_value = 0
	#Rotation
	instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Transform Geometry.002
	transform_geometry_002 = bgi_grid_container.nodes.new("GeometryNodeTransform")
	transform_geometry_002.name = "Transform Geometry.002"
	#Rotation
	transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Transform Geometry.003
	transform_geometry_003_1 = bgi_grid_container.nodes.new("GeometryNodeTransform")
	transform_geometry_003_1.name = "Transform Geometry.003"
	#Rotation
	transform_geometry_003_1.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_003_1.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Reroute.006
	reroute_006 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_006.name = "Reroute.006"
	#node Reroute.010
	reroute_010 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_010.name = "Reroute.010"
	#node Mesh Boolean
	mesh_boolean = bgi_grid_container.nodes.new("GeometryNodeMeshBoolean")
	mesh_boolean.name = "Mesh Boolean"
	mesh_boolean.operation = 'DIFFERENCE'
	if bpy.app.version >= (4, 2, 0):
		mesh_boolean.solver = 'EXACT'
	#Self Intersection
	mesh_boolean.inputs[2].default_value = False
	#Hole Tolerant
	mesh_boolean.inputs[3].default_value = False
	
	#node Mesh Boolean.001
	mesh_boolean_001 = bgi_grid_container.nodes.new("GeometryNodeMeshBoolean")
	mesh_boolean_001.name = "Mesh Boolean.001"
	mesh_boolean_001.operation = 'DIFFERENCE'
	if bpy.app.version >= (4, 2, 0):
		mesh_boolean_001.solver = 'EXACT'
	#Self Intersection
	mesh_boolean_001.inputs[2].default_value = False
	#Hole Tolerant
	mesh_boolean_001.inputs[3].default_value = False
	
	#node Switch.001
	switch_001 = bgi_grid_container.nodes.new("GeometryNodeSwitch")
	switch_001.name = "Switch.001"
	switch_001.input_type = 'GEOMETRY'
	
	#node Group Input.009
	group_input_009 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_009.name = "Group Input.009"
	group_input_009.outputs[0].hide = True
	group_input_009.outputs[1].hide = True
	group_input_009.outputs[2].hide = True
	group_input_009.outputs[3].hide = True
	group_input_009.outputs[4].hide = True
	group_input_009.outputs[5].hide = True
	group_input_009.outputs[6].hide = True
	group_input_009.outputs[8].hide = True
	group_input_009.outputs[9].hide = True
	group_input_009.outputs[10].hide = True
	group_input_009.outputs[11].hide = True
	
	#node Group Input.008
	group_input_008 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_008.name = "Group Input.008"
	group_input_008.outputs[0].hide = True
	group_input_008.outputs[1].hide = True
	group_input_008.outputs[2].hide = True
	group_input_008.outputs[3].hide = True
	group_input_008.outputs[4].hide = True
	group_input_008.outputs[5].hide = True
	group_input_008.outputs[7].hide = True
	group_input_008.outputs[8].hide = True
	group_input_008.outputs[9].hide = True
	group_input_008.outputs[10].hide = True
	group_input_008.outputs[11].hide = True
	
	#node Realize Instances.001
	realize_instances_001 = bgi_grid_container.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_001.name = "Realize Instances.001"
	
	#node Realize Instances.002
	realize_instances_002 = bgi_grid_container.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_002.name = "Realize Instances.002"
	
	#node Realize Instances
	realize_instances = bgi_grid_container.nodes.new("GeometryNodeRealizeInstances")
	realize_instances.name = "Realize Instances"
	
	#node Math.019
	math_019 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_019.name = "Math.019"
	math_019.operation = 'MODULO'
	math_019.use_clamp = False
	#Value_001
	math_019.inputs[1].default_value = 2.0
	
	#node Group Input.007
	group_input_007 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_007.name = "Group Input.007"
	group_input_007.outputs[0].hide = True
	group_input_007.outputs[1].hide = True
	group_input_007.outputs[4].hide = True
	group_input_007.outputs[6].hide = True
	group_input_007.outputs[7].hide = True
	group_input_007.outputs[9].hide = True
	group_input_007.outputs[10].hide = True
	group_input_007.outputs[11].hide = True
	
	#node Transform Geometry.004
	transform_geometry_004 = bgi_grid_container.nodes.new("GeometryNodeTransform")
	transform_geometry_004.name = "Transform Geometry.004"
	#Rotation
	transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.006
	combine_xyz_006 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_006.name = "Combine XYZ.006"
	#X
	combine_xyz_006.inputs[0].default_value = 0.0
	#Y
	combine_xyz_006.inputs[1].default_value = 0.0
	
	#node Instance on Points.002
	instance_on_points_002 = bgi_grid_container.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points_002.name = "Instance on Points.002"
	#Pick Instance
	instance_on_points_002.inputs[3].default_value = False
	#Instance Index
	instance_on_points_002.inputs[4].default_value = 0
	#Rotation
	instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Math.023
	math_023 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_023.name = "Math.023"
	math_023.operation = 'ADD'
	math_023.use_clamp = False
	
	#node Math.022
	math_022 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_022.name = "Math.022"
	math_022.operation = 'DIVIDE'
	math_022.use_clamp = False
	#Value_001
	math_022.inputs[1].default_value = 2.0
	
	#node Index.002
	index_002 = bgi_grid_container.nodes.new("GeometryNodeInputIndex")
	index_002.name = "Index.002"
	
	#node Scale Elements
	scale_elements = bgi_grid_container.nodes.new("GeometryNodeScaleElements")
	scale_elements.name = "Scale Elements"
	scale_elements.domain = 'FACE'
	scale_elements.scale_mode = 'SINGLE_AXIS'
	#Center
	scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
	#Axis
	scale_elements.inputs[4].default_value = (1.0, 0.0, 0.0)
	
	#node Math.027
	math_027 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_027.name = "Math.027"
	math_027.operation = 'DIVIDE'
	math_027.use_clamp = False
	
	#node Compare
	compare = bgi_grid_container.nodes.new("FunctionNodeCompare")
	compare.name = "Compare"
	compare.data_type = 'FLOAT'
	compare.mode = 'ELEMENT'
	compare.operation = 'GREATER_THAN'
	#B
	compare.inputs[1].default_value = 0.0
	
	#node Separate XYZ
	separate_xyz = bgi_grid_container.nodes.new("ShaderNodeSeparateXYZ")
	separate_xyz.name = "Separate XYZ"
	
	#node Position
	position = bgi_grid_container.nodes.new("GeometryNodeInputPosition")
	position.name = "Position"
	
	#node Cube.001
	cube_001_1 = bgi_grid_container.nodes.new("GeometryNodeMeshCube")
	cube_001_1.name = "Cube.001"
	#Vertices X
	cube_001_1.inputs[1].default_value = 2
	#Vertices Y
	cube_001_1.inputs[2].default_value = 2
	#Vertices Z
	cube_001_1.inputs[3].default_value = 2
	
	#node Combine XYZ.005
	combine_xyz_005 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_005.name = "Combine XYZ.005"
	
	#node Math.020
	math_020 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_020.name = "Math.020"
	math_020.operation = 'ADD'
	math_020.use_clamp = False
	
	#node Math.021
	math_021 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_021.name = "Math.021"
	math_021.operation = 'MULTIPLY'
	math_021.use_clamp = False
	#Value_001
	math_021.inputs[1].default_value = 3.0
	
	#node Group Input.006
	group_input_006 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_006.name = "Group Input.006"
	group_input_006.outputs[0].hide = True
	group_input_006.outputs[2].hide = True
	group_input_006.outputs[4].hide = True
	group_input_006.outputs[6].hide = True
	group_input_006.outputs[7].hide = True
	group_input_006.outputs[9].hide = True
	group_input_006.outputs[10].hide = True
	group_input_006.outputs[11].hide = True
	
	#node Group Input.010
	group_input_010 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_010.name = "Group Input.010"
	group_input_010.outputs[0].hide = True
	group_input_010.outputs[1].hide = True
	group_input_010.outputs[3].hide = True
	group_input_010.outputs[4].hide = True
	group_input_010.outputs[6].hide = True
	group_input_010.outputs[7].hide = True
	group_input_010.outputs[11].hide = True
	
	#node Group Input.001
	group_input_001_1 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_001_1.name = "Group Input.001"
	group_input_001_1.outputs[1].hide = True
	group_input_001_1.outputs[2].hide = True
	group_input_001_1.outputs[5].hide = True
	group_input_001_1.outputs[6].hide = True
	group_input_001_1.outputs[7].hide = True
	group_input_001_1.outputs[8].hide = True
	group_input_001_1.outputs[9].hide = True
	group_input_001_1.outputs[10].hide = True
	group_input_001_1.outputs[11].hide = True
	
	#node Group Input.002
	group_input_002_1 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_002_1.name = "Group Input.002"
	group_input_002_1.outputs[0].hide = True
	group_input_002_1.outputs[2].hide = True
	group_input_002_1.outputs[4].hide = True
	group_input_002_1.outputs[6].hide = True
	group_input_002_1.outputs[7].hide = True
	group_input_002_1.outputs[8].hide = True
	group_input_002_1.outputs[9].hide = True
	group_input_002_1.outputs[10].hide = True
	group_input_002_1.outputs[11].hide = True
	
	#node Group Input.004
	group_input_004_1 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_004_1.name = "Group Input.004"
	group_input_004_1.outputs[1].hide = True
	group_input_004_1.outputs[4].hide = True
	group_input_004_1.outputs[5].hide = True
	group_input_004_1.outputs[6].hide = True
	group_input_004_1.outputs[7].hide = True
	group_input_004_1.outputs[8].hide = True
	group_input_004_1.outputs[9].hide = True
	group_input_004_1.outputs[10].hide = True
	group_input_004_1.outputs[11].hide = True
	
	#node Group Input.005
	group_input_005 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_005.name = "Group Input.005"
	group_input_005.outputs[0].hide = True
	group_input_005.outputs[1].hide = True
	group_input_005.outputs[2].hide = True
	group_input_005.outputs[3].hide = True
	group_input_005.outputs[4].hide = True
	group_input_005.outputs[6].hide = True
	group_input_005.outputs[7].hide = True
	group_input_005.outputs[8].hide = True
	group_input_005.outputs[9].hide = True
	group_input_005.outputs[10].hide = True
	group_input_005.outputs[11].hide = True
	
	#node Combine XYZ.001
	combine_xyz_001 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_001.name = "Combine XYZ.001"
	#X
	combine_xyz_001.inputs[0].default_value = 0.0
	#Y
	combine_xyz_001.inputs[1].default_value = 0.0
	
	#node Combine XYZ
	combine_xyz_1 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_1.name = "Combine XYZ"
	
	#node Math
	math = bgi_grid_container.nodes.new("ShaderNodeMath")
	math.name = "Math"
	math.operation = 'DIVIDE'
	math.use_clamp = False
	#Value_001
	math.inputs[1].default_value = 2.0
	
	#node Math.003
	math_003 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_003.name = "Math.003"
	math_003.operation = 'ADD'
	math_003.use_clamp = False
	
	#node Transform Geometry
	transform_geometry = bgi_grid_container.nodes.new("GeometryNodeTransform")
	transform_geometry.name = "Transform Geometry"
	#Rotation
	transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Math.004
	math_004_1 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_004_1.name = "Math.004"
	math_004_1.operation = 'MULTIPLY'
	math_004_1.use_clamp = False
	
	#node Math.002
	math_002 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_002.name = "Math.002"
	math_002.operation = 'ADD'
	math_002.use_clamp = False
	
	#node Math.006
	math_006 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_006.name = "Math.006"
	math_006.operation = 'MULTIPLY'
	math_006.use_clamp = False
	
	#node Math.001
	math_001 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_001.name = "Math.001"
	math_001.operation = 'MULTIPLY'
	math_001.use_clamp = False
	
	#node Cube
	cube = bgi_grid_container.nodes.new("GeometryNodeMeshCube")
	cube.name = "Cube"
	#Vertices X
	cube.inputs[1].default_value = 2
	#Vertices Y
	cube.inputs[2].default_value = 2
	#Vertices Z
	cube.inputs[3].default_value = 2
	
	#node Group Input.011
	group_input_011 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_011.name = "Group Input.011"
	group_input_011.outputs[0].hide = True
	group_input_011.outputs[2].hide = True
	group_input_011.outputs[4].hide = True
	group_input_011.outputs[6].hide = True
	group_input_011.outputs[7].hide = True
	group_input_011.outputs[9].hide = True
	group_input_011.outputs[10].hide = True
	group_input_011.outputs[11].hide = True
	
	#node Math.005
	math_005_1 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_005_1.name = "Math.005"
	math_005_1.operation = 'ADD'
	math_005_1.use_clamp = False
	#Value_001
	math_005_1.inputs[1].default_value = 1.0
	
	#node Group Input
	group_input_1 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_1.name = "Group Input"
	group_input_1.outputs[1].hide = True
	group_input_1.outputs[2].hide = True
	group_input_1.outputs[5].hide = True
	group_input_1.outputs[6].hide = True
	group_input_1.outputs[7].hide = True
	group_input_1.outputs[8].hide = True
	group_input_1.outputs[9].hide = True
	group_input_1.outputs[10].hide = True
	group_input_1.outputs[11].hide = True
	
	#node Join Geometry
	join_geometry = bgi_grid_container.nodes.new("GeometryNodeJoinGeometry")
	join_geometry.name = "Join Geometry"
	
	#node Realize Instances.003
	realize_instances_003 = bgi_grid_container.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_003.name = "Realize Instances.003"
	
	#node Group Output
	group_output_1 = bgi_grid_container.nodes.new("NodeGroupOutput")
	group_output_1.name = "Group Output"
	group_output_1.is_active_output = True
	
	#node Switch
	switch_1 = bgi_grid_container.nodes.new("GeometryNodeSwitch")
	switch_1.name = "Switch"
	switch_1.input_type = 'GEOMETRY'
	
	#node Group Input.012
	group_input_012 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_012.name = "Group Input.012"
	group_input_012.outputs[0].hide = True
	group_input_012.outputs[2].hide = True
	group_input_012.outputs[4].hide = True
	group_input_012.outputs[6].hide = True
	group_input_012.outputs[7].hide = True
	group_input_012.outputs[8].hide = True
	group_input_012.outputs[9].hide = True
	group_input_012.outputs[10].hide = True
	group_input_012.outputs[11].hide = True
	
	#node Math.024
	math_024 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_024.name = "Math.024"
	math_024.operation = 'MULTIPLY'
	math_024.use_clamp = False
	
	#node Math.025
	math_025 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_025.name = "Math.025"
	math_025.operation = 'ADD'
	math_025.use_clamp = False
	#Value_001
	math_025.inputs[1].default_value = 1.0
	
	#node Math.026
	math_026 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_026.name = "Math.026"
	math_026.operation = 'MULTIPLY'
	math_026.use_clamp = False
	
	#node Math.028
	math_028 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_028.name = "Math.028"
	math_028.operation = 'SUBTRACT'
	math_028.use_clamp = False
	#Value_001
	math_028.inputs[1].default_value = 1.0
	
	#node Math.029
	math_029 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_029.name = "Math.029"
	math_029.operation = 'ADD'
	math_029.use_clamp = False
	
	#node Math.030
	math_030 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_030.name = "Math.030"
	math_030.operation = 'MULTIPLY'
	math_030.use_clamp = False
	
	#node Group Input.013
	group_input_013 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_013.name = "Group Input.013"
	group_input_013.outputs[0].hide = True
	group_input_013.outputs[1].hide = True
	group_input_013.outputs[4].hide = True
	group_input_013.outputs[5].hide = True
	group_input_013.outputs[6].hide = True
	group_input_013.outputs[7].hide = True
	group_input_013.outputs[8].hide = True
	group_input_013.outputs[9].hide = True
	group_input_013.outputs[10].hide = True
	group_input_013.outputs[11].hide = True
	
	#node Math.015
	math_015 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_015.name = "Math.015"
	math_015.operation = 'MULTIPLY_ADD'
	math_015.use_clamp = False
	
	#node Math.010
	math_010_1 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_010_1.name = "Math.010"
	math_010_1.operation = 'ADD'
	math_010_1.use_clamp = False
	#Value_001
	math_010_1.inputs[1].default_value = 1.0
	
	#node Math.016
	math_016 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_016.name = "Math.016"
	math_016.operation = 'MULTIPLY'
	math_016.use_clamp = False
	
	#node Math.031
	math_031 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_031.name = "Math.031"
	math_031.operation = 'DIVIDE'
	math_031.use_clamp = False
	#Value_001
	math_031.inputs[1].default_value = 2.0
	
	#node Group Input.014
	group_input_014 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_014.name = "Group Input.014"
	group_input_014.outputs[0].hide = True
	group_input_014.outputs[2].hide = True
	group_input_014.outputs[4].hide = True
	group_input_014.outputs[6].hide = True
	group_input_014.outputs[7].hide = True
	group_input_014.outputs[8].hide = True
	group_input_014.outputs[9].hide = True
	group_input_014.outputs[10].hide = True
	group_input_014.outputs[11].hide = True
	
	#node Math.032
	math_032 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_032.name = "Math.032"
	math_032.operation = 'SUBTRACT'
	math_032.use_clamp = False
	
	#node Group Input.015
	group_input_015 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_015.name = "Group Input.015"
	group_input_015.outputs[0].hide = True
	group_input_015.outputs[2].hide = True
	group_input_015.outputs[4].hide = True
	group_input_015.outputs[6].hide = True
	group_input_015.outputs[7].hide = True
	group_input_015.outputs[8].hide = True
	group_input_015.outputs[9].hide = True
	group_input_015.outputs[10].hide = True
	group_input_015.outputs[11].hide = True
	
	#node Math.033
	math_033 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_033.name = "Math.033"
	math_033.operation = 'DIVIDE'
	math_033.use_clamp = False
	#Value_001
	math_033.inputs[1].default_value = 2.0
	
	#node Math.034
	math_034 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_034.name = "Math.034"
	math_034.operation = 'MULTIPLY'
	math_034.use_clamp = False
	
	#node Frame.007
	frame_007 = bgi_grid_container.nodes.new("NodeFrame")
	frame_007.label = "Divisions location Y direction"
	frame_007.name = "Frame.007"
	frame_007.label_size = 20
	frame_007.shrink = True
	
	#node Mesh Line.001
	mesh_line_001 = bgi_grid_container.nodes.new("GeometryNodeMeshLine")
	mesh_line_001.name = "Mesh Line.001"
	mesh_line_001.count_mode = 'TOTAL'
	mesh_line_001.mode = 'OFFSET'
	
	#node Mesh to Points.001
	mesh_to_points_001 = bgi_grid_container.nodes.new("GeometryNodeMeshToPoints")
	mesh_to_points_001.name = "Mesh to Points.001"
	mesh_to_points_001.mode = 'VERTICES'
	#Selection
	mesh_to_points_001.inputs[1].default_value = True
	#Position
	mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Radius
	mesh_to_points_001.inputs[3].default_value = 0.0020000000949949026
	
	#node Group Input.017
	group_input_017 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_017.name = "Group Input.017"
	group_input_017.outputs[0].hide = True
	group_input_017.outputs[2].hide = True
	group_input_017.outputs[4].hide = True
	group_input_017.outputs[6].hide = True
	group_input_017.outputs[7].hide = True
	group_input_017.outputs[8].hide = True
	group_input_017.outputs[9].hide = True
	group_input_017.outputs[10].hide = True
	group_input_017.outputs[11].hide = True
	
	#node Reroute
	reroute_1 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_1.name = "Reroute"
	#node Frame.008
	frame_008 = bgi_grid_container.nodes.new("NodeFrame")
	frame_008.label = "Side divisor"
	frame_008.name = "Frame.008"
	frame_008.label_size = 20
	frame_008.shrink = True
	
	#node Reroute.001
	reroute_001 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_001.name = "Reroute.001"
	#node Combine XYZ.009
	combine_xyz_009 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_009.name = "Combine XYZ.009"
	#X
	combine_xyz_009.inputs[0].default_value = 0.0
	#Z
	combine_xyz_009.inputs[2].default_value = 0.0
	
	#node Combine XYZ.010
	combine_xyz_010 = bgi_grid_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_010.name = "Combine XYZ.010"
	#X
	combine_xyz_010.inputs[0].default_value = 0.0
	#Z
	combine_xyz_010.inputs[2].default_value = 0.0
	
	#node Math.035
	math_035 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_035.name = "Math.035"
	math_035.operation = 'ADD'
	math_035.use_clamp = False
	
	#node Math.041
	math_041 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_041.name = "Math.041"
	math_041.operation = 'SUBTRACT'
	math_041.use_clamp = False
	#Value_001
	math_041.inputs[1].default_value = 1.0
	
	#node Group Input.019
	group_input_019 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_019.name = "Group Input.019"
	group_input_019.outputs[0].hide = True
	group_input_019.outputs[1].hide = True
	group_input_019.outputs[2].hide = True
	group_input_019.outputs[3].hide = True
	group_input_019.outputs[4].hide = True
	group_input_019.outputs[6].hide = True
	group_input_019.outputs[7].hide = True
	group_input_019.outputs[8].hide = True
	group_input_019.outputs[9].hide = True
	group_input_019.outputs[10].hide = True
	group_input_019.outputs[11].hide = True
	
	#node Instance on Points.003
	instance_on_points_003 = bgi_grid_container.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points_003.name = "Instance on Points.003"
	#Selection
	instance_on_points_003.inputs[1].default_value = True
	#Pick Instance
	instance_on_points_003.inputs[3].default_value = False
	#Instance Index
	instance_on_points_003.inputs[4].default_value = 0
	#Rotation
	instance_on_points_003.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points_003.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Math.036
	math_036 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_036.name = "Math.036"
	math_036.operation = 'DIVIDE'
	math_036.use_clamp = False
	#Value_001
	math_036.inputs[1].default_value = -2.0
	
	#node Math.037
	math_037 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_037.name = "Math.037"
	math_037.operation = 'MULTIPLY'
	math_037.use_clamp = False
	
	#node Math.038
	math_038 = bgi_grid_container.nodes.new("ShaderNodeMath")
	math_038.name = "Math.038"
	math_038.operation = 'SUBTRACT'
	math_038.use_clamp = False
	#Value_001
	math_038.inputs[1].default_value = 2.0
	
	#node Reroute.003
	reroute_003 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_003.name = "Reroute.003"
	#node Realize Instances.004
	realize_instances_004 = bgi_grid_container.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_004.name = "Realize Instances.004"
	
	#node Group Input.016
	group_input_016 = bgi_grid_container.nodes.new("NodeGroupInput")
	group_input_016.name = "Group Input.016"
	group_input_016.outputs[0].hide = True
	group_input_016.outputs[1].hide = True
	group_input_016.outputs[2].hide = True
	group_input_016.outputs[3].hide = True
	group_input_016.outputs[4].hide = True
	group_input_016.outputs[5].hide = True
	group_input_016.outputs[6].hide = True
	group_input_016.outputs[7].hide = True
	group_input_016.outputs[9].hide = True
	group_input_016.outputs[10].hide = True
	group_input_016.outputs[11].hide = True
	
	#node Switch.002
	switch_002_1 = bgi_grid_container.nodes.new("GeometryNodeSwitch")
	switch_002_1.name = "Switch.002"
	switch_002_1.input_type = 'GEOMETRY'
	
	#node Mesh Boolean.002
	mesh_boolean_002 = bgi_grid_container.nodes.new("GeometryNodeMeshBoolean")
	mesh_boolean_002.name = "Mesh Boolean.002"
	mesh_boolean_002.operation = 'DIFFERENCE'
	if bpy.app.version >= (4, 2, 0):
		mesh_boolean_002.solver = 'EXACT'
	#Self Intersection
	mesh_boolean_002.inputs[2].default_value = False
	#Hole Tolerant
	mesh_boolean_002.inputs[3].default_value = False
	
	#node Reroute.002
	reroute_002 = bgi_grid_container.nodes.new("NodeReroute")
	reroute_002.name = "Reroute.002"
	#node Domain Size
	domain_size = bgi_grid_container.nodes.new("GeometryNodeAttributeDomainSize")
	domain_size.name = "Domain Size"
	domain_size.component = 'MESH'
	
	#node Compare.001
	compare_001 = bgi_grid_container.nodes.new("FunctionNodeCompare")
	compare_001.name = "Compare.001"
	compare_001.data_type = 'INT'
	compare_001.mode = 'ELEMENT'
	compare_001.operation = 'GREATER_THAN'
	#B_INT
	compare_001.inputs[3].default_value = 0
	
	#node Switch.003
	switch_003 = bgi_grid_container.nodes.new("GeometryNodeSwitch")
	switch_003.name = "Switch.003"
	switch_003.input_type = 'GEOMETRY'
	
	
	
	#Set parents
	math_017.parent = frame_001_1
	math_018.parent = frame_001_1
	combine_xyz_003.parent = frame_001_1
	group_input_003_1.parent = frame_001_1
	mesh_line.parent = frame_001_1
	combine_xyz_002_1.parent = frame_001_1
	math_007.parent = frame_001_1
	math_014.parent = frame_001_1
	math_009_1.parent = frame_001_1
	math_008.parent = frame_001_1
	transform_geometry_001.parent = frame_001_1
	mesh_to_points.parent = frame_001_1
	group.parent = frame_002
	index.parent = frame_002
	math_012.parent = frame_002
	math_011.parent = frame_002
	instance_on_points.parent = frame_002
	combine_xyz_004.parent = frame_003_1
	vector_math.parent = frame_003_1
	math_013.parent = frame_008
	group_001.parent = frame_008
	index_001.parent = frame_008
	instance_on_points_001.parent = frame_008
	transform_geometry_002.parent = frame_003_1
	transform_geometry_003_1.parent = frame_003_1
	mesh_boolean.parent = frame_005
	mesh_boolean_001.parent = frame_005
	switch_001.parent = frame_005
	group_input_009.parent = frame_005
	group_input_008.parent = frame_005
	realize_instances_001.parent = frame_005
	realize_instances_002.parent = frame_005
	realize_instances.parent = frame_005
	math_019.parent = frame_006
	group_input_007.parent = frame_006
	transform_geometry_004.parent = frame_006
	combine_xyz_006.parent = frame_006
	instance_on_points_002.parent = frame_006
	math_023.parent = frame_006
	math_022.parent = frame_006
	index_002.parent = frame_006
	scale_elements.parent = frame_004
	math_027.parent = frame_004
	compare.parent = frame_004
	separate_xyz.parent = frame_004
	position.parent = frame_004
	cube_001_1.parent = frame_004
	combine_xyz_005.parent = frame_004
	math_020.parent = frame_004
	math_021.parent = frame_004
	group_input_006.parent = frame_004
	group_input_010.parent = frame_004
	group_input_001_1.parent = frame_001_1
	group_input_002_1.parent = frame_002
	group_input_004_1.parent = frame_008
	group_input_005.parent = frame_003_1
	combine_xyz_001.parent = frame_1
	combine_xyz_1.parent = frame_1
	math.parent = frame_1
	math_003.parent = frame_1
	transform_geometry.parent = frame_1
	math_004_1.parent = frame_1
	math_002.parent = frame_1
	math_006.parent = frame_1
	math_001.parent = frame_1
	cube.parent = frame_1
	group_input_011.parent = frame_1
	math_005_1.parent = frame_1
	group_input_1.parent = frame_1
	switch_1.parent = frame_005
	group_input_012.parent = frame_1
	math_024.parent = frame_1
	math_025.parent = frame_1
	math_026.parent = frame_002
	math_028.parent = frame_002
	math_029.parent = frame_002
	math_030.parent = frame_002
	group_input_013.parent = frame_002
	math_015.parent = frame_003_1
	math_010_1.parent = frame_003_1
	math_016.parent = frame_003_1
	math_031.parent = frame_003_1
	group_input_014.parent = frame_003_1
	math_032.parent = frame_003_1
	group_input_015.parent = frame_003_1
	math_033.parent = frame_003_1
	math_034.parent = frame_004
	mesh_line_001.parent = frame_007
	mesh_to_points_001.parent = frame_007
	group_input_017.parent = frame_007
	reroute_001.parent = frame_003_1
	combine_xyz_009.parent = frame_007
	combine_xyz_010.parent = frame_007
	math_035.parent = frame_007
	math_041.parent = frame_007
	group_input_019.parent = frame_007
	instance_on_points_003.parent = frame_007
	math_036.parent = frame_007
	math_037.parent = frame_007
	math_038.parent = frame_007
	realize_instances_004.parent = frame_005
	group_input_016.parent = frame_005
	switch_002_1.parent = frame_005
	mesh_boolean_002.parent = frame_005
	domain_size.parent = frame_005
	compare_001.parent = frame_005
	switch_003.parent = frame_005
	
	#Set locations
	frame_001_1.location = (-930.0, -532.0)
	frame_002.location = (1149.0, 549.0)
	frame_003_1.location = (-21.0, -470.0)
	frame_005.location = (-22.0, -247.0)
	frame_006.location = (40.0, -370.0)
	frame_004.location = (-50.0, -337.0)
	frame_1.location = (71.0, 816.0)
	reroute_008.location = (80.0, 240.0)
	math_017.location = (-2366.17626953125, -281.3491516113281)
	math_018.location = (-2175.85302734375, -283.416015625)
	combine_xyz_003.location = (-2006.16455078125, -283.5311279296875)
	group_input_003_1.location = (-2556.25048828125, -378.7306823730469)
	mesh_line.location = (-2173.522705078125, -1.201385498046875)
	combine_xyz_002_1.location = (-2368.73876953125, -141.16993713378906)
	math_007.location = (-2556.07763671875, -181.12489318847656)
	math_014.location = (-2737.598876953125, -179.7510986328125)
	math_009_1.location = (-2361.89599609375, 38.087032318115234)
	math_008.location = (-2558.85791015625, 92.7177505493164)
	transform_geometry_001.location = (-1803.961181640625, -103.16421508789062)
	mesh_to_points.location = (-1610.0, -168.0)
	reroute_007.location = (-900.0, 240.0)
	group.location = (-1200.0, -529.0)
	index.location = (-1560.0, -429.0)
	math_012.location = (-1380.0, -369.0)
	math_011.location = (-1200.0, -369.0)
	instance_on_points.location = (-1000.0, -389.0)
	combine_xyz_004.location = (-250.0, -890.0)
	vector_math.location = (-50.0, -910.0)
	math_013.location = (-2060.0, -460.0)
	group_001.location = (-2060.0, -640.0)
	index_001.location = (-2280.0, -540.0)
	instance_on_points_001.location = (-1869.0, -461.0)
	transform_geometry_002.location = (190.0, -629.0)
	transform_geometry_003_1.location = (190.0, -929.0)
	reroute_006.location = (-2300.0, -740.0)
	reroute_010.location = (-2120.0, -1700.0)
	mesh_boolean.location = (1022.0, -413.0)
	mesh_boolean_001.location = (1022.0, -653.0)
	switch_001.location = (642.0, -793.0)
	group_input_009.location = (442.0, -853.0)
	group_input_008.location = (442.0, -613.0)
	realize_instances_001.location = (442.0, -493.0)
	realize_instances_002.location = (442.0, -733.0)
	realize_instances.location = (442.0, -953.0)
	math_019.location = (-452.6567687988281, -1389.5614013671875)
	group_input_007.location = (-580.5625610351562, -1884.75146484375)
	transform_geometry_004.location = (126.0401840209961, -1449.48876953125)
	combine_xyz_006.location = (-63.425174713134766, -1801.0885009765625)
	instance_on_points_002.location = (-70.86670684814453, -1451.0360107421875)
	math_023.location = (-237.2020263671875, -1807.8134765625)
	math_022.location = (-409.1944580078125, -1776.7532958984375)
	index_002.location = (-651.0845336914062, -1465.4306640625)
	scale_elements.location = (-800.6685180664062, -1548.0284423828125)
	math_027.location = (-1210.8466796875, -1730.6495361328125)
	compare.location = (-1023.304443359375, -1775.6810302734375)
	separate_xyz.location = (-1215.808837890625, -1908.0040283203125)
	position.location = (-1397.4140625, -1971.1334228515625)
	cube_001_1.location = (-1021.1686401367188, -1546.0616455078125)
	combine_xyz_005.location = (-1208.7972412109375, -1589.10009765625)
	math_020.location = (-1680.6632080078125, -1562.1470947265625)
	math_021.location = (-1860.6632080078125, -1502.1470947265625)
	group_input_006.location = (-2060.6630859375, -1662.1470947265625)
	group_input_010.location = (-1680.6632080078125, -1742.1470947265625)
	group_input_001_1.location = (-2981.425048828125, -17.6748046875)
	group_input_002_1.location = (-1920.0, -649.0)
	group_input_004_1.location = (-2280.0, -680.0)
	group_input_005.location = (-1370.0, -1090.0)
	combine_xyz_001.location = (-142.0, -236.0)
	combine_xyz_1.location = (-322.0, -56.0)
	math.location = (-322.0, -196.0)
	math_003.location = (-562.0, -116.0)
	transform_geometry.location = (78.0, -56.0)
	math_004_1.location = (-762.0, -116.0)
	math_002.location = (-562.0, 204.0)
	math_006.location = (-762.0, 44.0)
	math_001.location = (-762.0, 204.0)
	cube.location = (-142.0, -56.0)
	group_input_011.location = (-562.0, -276.0)
	math_005_1.location = (-982.0, 204.0)
	group_input_1.location = (-1182.0, 4.0)
	join_geometry.location = (1280.0001220703125, -120.0)
	realize_instances_003.location = (1460.0001220703125, -120.0)
	group_output_1.location = (1640.0001220703125, -120.0)
	switch_1.location = (642.0, -553.0)
	group_input_012.location = (-1182.0, -196.0)
	math_024.location = (-762.0, -276.0)
	math_025.location = (-982.0, -376.0)
	math_026.location = (-1560.0, -689.0)
	math_028.location = (-1740.0, -489.0)
	math_029.location = (-1380.0, -529.0)
	math_030.location = (-1560.0, -529.0)
	group_input_013.location = (-1380.0, -689.0)
	math_015.location = (-810.0, -870.0)
	math_010_1.location = (-1190.0, -1010.0)
	math_016.location = (-990.0, -1010.0)
	math_031.location = (-630.0, -870.0)
	group_input_014.location = (-1190.0, -890.0)
	math_032.location = (-450.0, -890.0)
	group_input_015.location = (-810.0, -1070.0)
	math_033.location = (-630.0, -1030.0)
	math_034.location = (-1500.6632080078125, -1562.1470947265625)
	frame_007.location = (1557.0, -512.0)
	mesh_line_001.location = (-1848.0, 32.0)
	mesh_to_points_001.location = (-1659.0, 32.0)
	group_input_017.location = (-2848.0, -168.0)
	reroute_1.location = (-1720.0, -740.0)
	frame_008.location = (229.0, -499.0)
	reroute_001.location = (10.0, -690.0)
	combine_xyz_009.location = (-2068.0, -68.0)
	combine_xyz_010.location = (-2068.0, -208.0)
	math_035.location = (-2628.0, -248.0)
	math_041.location = (-2068.0, 92.0)
	group_input_019.location = (-2248.0, 32.0)
	instance_on_points_003.location = (-1397.0, 32.0)
	math_036.location = (-2248.0, -68.0)
	math_037.location = (-2428.0, -68.0)
	math_038.location = (-2628.0, -68.0)
	reroute_003.location = (-120.0, -1000.0)
	realize_instances_004.location = (442.0, -233.0)
	group_input_016.location = (442.0, -353.0)
	switch_002_1.location = (642.0, -293.0)
	mesh_boolean_002.location = (862.0, -173.0)
	reroute_002.location = (-60.0, -1700.0)
	domain_size.location = (642.0, -53.0)
	compare_001.location = (862.0, -13.0)
	switch_003.location = (1042.0, -33.0)
	
	#Set dimensions
	frame_001_1.width, frame_001_1.height = 1569.333251953125, 589.1666259765625
	frame_002.width, frame_002.height = 1118.6666259765625, 529.8333740234375
	frame_003_1.width, frame_003_1.height = 1758.666748046875, 618.5
	frame_005.width, frame_005.height = 798.0, 1080.5
	frame_006.width, frame_006.height = 975.3333129882812, 675.1666259765625
	frame_004.width, frame_004.height = 1458.0, 587.8333740234375
	frame_1.width, frame_1.height = 1458.666748046875, 791.1666259765625
	reroute_008.width, reroute_008.height = 16.0, 100.0
	math_017.width, math_017.height = 140.0, 100.0
	math_018.width, math_018.height = 140.0, 100.0
	combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
	group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
	mesh_line.width, mesh_line.height = 140.0, 100.0
	combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
	math_007.width, math_007.height = 140.0, 100.0
	math_014.width, math_014.height = 140.0, 100.0
	math_009_1.width, math_009_1.height = 140.0, 100.0
	math_008.width, math_008.height = 140.0, 100.0
	transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
	mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
	reroute_007.width, reroute_007.height = 16.0, 100.0
	group.width, group.height = 140.0, 100.0
	index.width, index.height = 140.0, 100.0
	math_012.width, math_012.height = 140.0, 100.0
	math_011.width, math_011.height = 140.0, 100.0
	instance_on_points.width, instance_on_points.height = 140.0, 100.0
	combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
	vector_math.width, vector_math.height = 140.0, 100.0
	math_013.width, math_013.height = 140.0, 100.0
	group_001.width, group_001.height = 140.0, 100.0
	index_001.width, index_001.height = 140.0, 100.0
	instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
	transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
	transform_geometry_003_1.width, transform_geometry_003_1.height = 140.0, 100.0
	reroute_006.width, reroute_006.height = 16.0, 100.0
	reroute_010.width, reroute_010.height = 16.0, 100.0
	mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
	mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
	switch_001.width, switch_001.height = 140.0, 100.0
	group_input_009.width, group_input_009.height = 140.0, 100.0
	group_input_008.width, group_input_008.height = 140.0, 100.0
	realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
	realize_instances_002.width, realize_instances_002.height = 140.0, 100.0
	realize_instances.width, realize_instances.height = 140.0, 100.0
	math_019.width, math_019.height = 140.0, 100.0
	group_input_007.width, group_input_007.height = 140.0, 100.0
	transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
	combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
	instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
	math_023.width, math_023.height = 140.0, 100.0
	math_022.width, math_022.height = 140.0, 100.0
	index_002.width, index_002.height = 140.0, 100.0
	scale_elements.width, scale_elements.height = 140.0, 100.0
	math_027.width, math_027.height = 140.0, 100.0
	compare.width, compare.height = 140.0, 100.0
	separate_xyz.width, separate_xyz.height = 140.0, 100.0
	position.width, position.height = 140.0, 100.0
	cube_001_1.width, cube_001_1.height = 140.0, 100.0
	combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
	math_020.width, math_020.height = 140.0, 100.0
	math_021.width, math_021.height = 140.0, 100.0
	group_input_006.width, group_input_006.height = 140.0, 100.0
	group_input_010.width, group_input_010.height = 140.0, 100.0
	group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
	group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
	group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
	group_input_005.width, group_input_005.height = 140.0, 100.0
	combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
	combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
	math.width, math.height = 140.0, 100.0
	math_003.width, math_003.height = 140.0, 100.0
	transform_geometry.width, transform_geometry.height = 140.0, 100.0
	math_004_1.width, math_004_1.height = 140.0, 100.0
	math_002.width, math_002.height = 140.0, 100.0
	math_006.width, math_006.height = 140.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	cube.width, cube.height = 140.0, 100.0
	group_input_011.width, group_input_011.height = 140.0, 100.0
	math_005_1.width, math_005_1.height = 140.0, 100.0
	group_input_1.width, group_input_1.height = 140.0, 100.0
	join_geometry.width, join_geometry.height = 140.0, 100.0
	realize_instances_003.width, realize_instances_003.height = 140.0, 100.0
	group_output_1.width, group_output_1.height = 140.0, 100.0
	switch_1.width, switch_1.height = 140.0, 100.0
	group_input_012.width, group_input_012.height = 140.0, 100.0
	math_024.width, math_024.height = 140.0, 100.0
	math_025.width, math_025.height = 140.0, 100.0
	math_026.width, math_026.height = 140.0, 100.0
	math_028.width, math_028.height = 140.0, 100.0
	math_029.width, math_029.height = 140.0, 100.0
	math_030.width, math_030.height = 140.0, 100.0
	group_input_013.width, group_input_013.height = 140.0, 100.0
	math_015.width, math_015.height = 140.0, 100.0
	math_010_1.width, math_010_1.height = 140.0, 100.0
	math_016.width, math_016.height = 140.0, 100.0
	math_031.width, math_031.height = 140.0, 100.0
	group_input_014.width, group_input_014.height = 140.0, 100.0
	math_032.width, math_032.height = 140.0, 100.0
	group_input_015.width, group_input_015.height = 140.0, 100.0
	math_033.width, math_033.height = 140.0, 100.0
	math_034.width, math_034.height = 140.0, 100.0
	frame_007.width, frame_007.height = 1649.33349609375, 549.8333129882812
	mesh_line_001.width, mesh_line_001.height = 140.0, 100.0
	mesh_to_points_001.width, mesh_to_points_001.height = 140.0, 100.0
	group_input_017.width, group_input_017.height = 140.0, 100.0
	reroute_1.width, reroute_1.height = 16.0, 100.0
	frame_008.width, frame_008.height = 609.333251953125, 465.16668701171875
	reroute_001.width, reroute_001.height = 16.0, 100.0
	combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
	combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
	math_035.width, math_035.height = 140.0, 100.0
	math_041.width, math_041.height = 140.0, 100.0
	group_input_019.width, group_input_019.height = 140.0, 100.0
	instance_on_points_003.width, instance_on_points_003.height = 140.0, 100.0
	math_036.width, math_036.height = 140.0, 100.0
	math_037.width, math_037.height = 140.0, 100.0
	math_038.width, math_038.height = 140.0, 100.0
	reroute_003.width, reroute_003.height = 16.0, 100.0
	realize_instances_004.width, realize_instances_004.height = 140.0, 100.0
	group_input_016.width, group_input_016.height = 140.0, 100.0
	switch_002_1.width, switch_002_1.height = 140.0, 100.0
	mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
	reroute_002.width, reroute_002.height = 16.0, 100.0
	domain_size.width, domain_size.height = 140.0, 100.0
	compare_001.width, compare_001.height = 140.0, 100.0
	switch_003.width, switch_003.height = 140.0, 100.0
	
	#initialize bgi_grid_container links
	#combine_xyz_1.Vector -> cube.Size
	bgi_grid_container.links.new(combine_xyz_1.outputs[0], cube.inputs[0])
	#cube.Mesh -> transform_geometry.Geometry
	bgi_grid_container.links.new(cube.outputs[0], transform_geometry.inputs[0])
	#group_input_011.Tickness -> math.Value
	bgi_grid_container.links.new(group_input_011.outputs[3], math.inputs[0])
	#combine_xyz_001.Vector -> transform_geometry.Translation
	bgi_grid_container.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
	#math.Value -> combine_xyz_001.Z
	bgi_grid_container.links.new(math.outputs[0], combine_xyz_001.inputs[2])
	#math_001.Value -> math_002.Value
	bgi_grid_container.links.new(math_001.outputs[0], math_002.inputs[0])
	#math_002.Value -> combine_xyz_1.X
	bgi_grid_container.links.new(math_002.outputs[0], combine_xyz_1.inputs[0])
	#math_003.Value -> combine_xyz_1.Y
	bgi_grid_container.links.new(math_003.outputs[0], combine_xyz_1.inputs[1])
	#group_input_011.Tickness -> combine_xyz_1.Z
	bgi_grid_container.links.new(group_input_011.outputs[3], combine_xyz_1.inputs[2])
	#math_006.Value -> math_002.Value
	bgi_grid_container.links.new(math_006.outputs[0], math_002.inputs[1])
	#math_004_1.Value -> math_003.Value
	bgi_grid_container.links.new(math_004_1.outputs[0], math_003.inputs[0])
	#group_input_1.Count Width -> math_005_1.Value
	bgi_grid_container.links.new(group_input_1.outputs[4], math_005_1.inputs[0])
	#group_input_1.Inner Width -> math_006.Value
	bgi_grid_container.links.new(group_input_1.outputs[0], math_006.inputs[0])
	#group_input_1.Count Width -> math_006.Value
	bgi_grid_container.links.new(group_input_1.outputs[4], math_006.inputs[1])
	#group_input_1.Tickness -> math_001.Value
	bgi_grid_container.links.new(group_input_1.outputs[3], math_001.inputs[1])
	#math_005_1.Value -> math_001.Value
	bgi_grid_container.links.new(math_005_1.outputs[0], math_001.inputs[0])
	#combine_xyz_002_1.Vector -> mesh_line.Offset
	bgi_grid_container.links.new(combine_xyz_002_1.outputs[0], mesh_line.inputs[3])
	#math_007.Value -> combine_xyz_002_1.X
	bgi_grid_container.links.new(math_007.outputs[0], combine_xyz_002_1.inputs[0])
	#group_input_001_1.Count Width -> math_008.Value
	bgi_grid_container.links.new(group_input_001_1.outputs[4], math_008.inputs[0])
	#math_008.Value -> math_009_1.Value
	bgi_grid_container.links.new(math_008.outputs[0], math_009_1.inputs[0])
	#group_input_001_1.Count Width -> math_009_1.Value
	bgi_grid_container.links.new(group_input_001_1.outputs[4], math_009_1.inputs[1])
	#math_009_1.Value -> mesh_line.Count
	bgi_grid_container.links.new(math_009_1.outputs[0], mesh_line.inputs[0])
	#mesh_line.Mesh -> transform_geometry_001.Geometry
	bgi_grid_container.links.new(mesh_line.outputs[0], transform_geometry_001.inputs[0])
	#combine_xyz_003.Vector -> transform_geometry_001.Translation
	bgi_grid_container.links.new(combine_xyz_003.outputs[0], transform_geometry_001.inputs[1])
	#transform_geometry_001.Geometry -> mesh_to_points.Mesh
	bgi_grid_container.links.new(transform_geometry_001.outputs[0], mesh_to_points.inputs[0])
	#reroute_008.Output -> instance_on_points.Points
	bgi_grid_container.links.new(reroute_008.outputs[0], instance_on_points.inputs[0])
	#group.Geometry -> instance_on_points.Instance
	bgi_grid_container.links.new(group.outputs[0], instance_on_points.inputs[2])
	#math_011.Value -> instance_on_points.Selection
	bgi_grid_container.links.new(math_011.outputs[0], instance_on_points.inputs[1])
	#index.Index -> math_012.Value
	bgi_grid_container.links.new(index.outputs[0], math_012.inputs[0])
	#math_012.Value -> math_011.Value
	bgi_grid_container.links.new(math_012.outputs[0], math_011.inputs[0])
	#group_input_001_1.Tickness -> math_014.Value
	bgi_grid_container.links.new(group_input_001_1.outputs[3], math_014.inputs[1])
	#group_input_001_1.Inner Width -> math_014.Value
	bgi_grid_container.links.new(group_input_001_1.outputs[0], math_014.inputs[0])
	#math_014.Value -> math_007.Value
	bgi_grid_container.links.new(math_014.outputs[0], math_007.inputs[0])
	#math_007.Value -> math_017.Value
	bgi_grid_container.links.new(math_007.outputs[0], math_017.inputs[0])
	#math_018.Value -> combine_xyz_003.X
	bgi_grid_container.links.new(math_018.outputs[0], combine_xyz_003.inputs[0])
	#math_017.Value -> math_018.Value
	bgi_grid_container.links.new(math_017.outputs[0], math_018.inputs[0])
	#group_input_003_1.Count Width -> math_017.Value
	bgi_grid_container.links.new(group_input_003_1.outputs[4], math_017.inputs[1])
	#group_input_004_1.Tickness -> group_001.Thickness
	bgi_grid_container.links.new(group_input_004_1.outputs[3], group_001.inputs[3])
	#group_input_004_1.Inner Height -> group_001.Height
	bgi_grid_container.links.new(group_input_004_1.outputs[2], group_001.inputs[2])
	#group_001.Geometry -> instance_on_points_001.Instance
	bgi_grid_container.links.new(group_001.outputs[0], instance_on_points_001.inputs[2])
	#math_013.Value -> instance_on_points_001.Selection
	bgi_grid_container.links.new(math_013.outputs[0], instance_on_points_001.inputs[1])
	#index_001.Index -> math_013.Value
	bgi_grid_container.links.new(index_001.outputs[0], math_013.inputs[0])
	#reroute_1.Output -> instance_on_points_001.Points
	bgi_grid_container.links.new(reroute_1.outputs[0], instance_on_points_001.inputs[0])
	#group_input_004_1.Inner Width -> group_001.Width
	bgi_grid_container.links.new(group_input_004_1.outputs[0], group_001.inputs[0])
	#reroute_001.Output -> transform_geometry_002.Geometry
	bgi_grid_container.links.new(reroute_001.outputs[0], transform_geometry_002.inputs[0])
	#combine_xyz_004.Vector -> transform_geometry_002.Translation
	bgi_grid_container.links.new(combine_xyz_004.outputs[0], transform_geometry_002.inputs[1])
	#combine_xyz_004.Vector -> vector_math.Vector
	bgi_grid_container.links.new(combine_xyz_004.outputs[0], vector_math.inputs[0])
	#vector_math.Vector -> transform_geometry_003_1.Translation
	bgi_grid_container.links.new(vector_math.outputs[0], transform_geometry_003_1.inputs[1])
	#mesh_to_points.Points -> reroute_006.Input
	bgi_grid_container.links.new(mesh_to_points.outputs[0], reroute_006.inputs[0])
	#reroute_006.Output -> reroute_007.Input
	bgi_grid_container.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
	#reroute_007.Output -> reroute_008.Input
	bgi_grid_container.links.new(reroute_007.outputs[0], reroute_008.inputs[0])
	#reroute_002.Output -> instance_on_points_002.Points
	bgi_grid_container.links.new(reroute_002.outputs[0], instance_on_points_002.inputs[0])
	#math_019.Value -> instance_on_points_002.Selection
	bgi_grid_container.links.new(math_019.outputs[0], instance_on_points_002.inputs[1])
	#index_002.Index -> math_019.Value
	bgi_grid_container.links.new(index_002.outputs[0], math_019.inputs[0])
	#combine_xyz_005.Vector -> cube_001_1.Size
	bgi_grid_container.links.new(combine_xyz_005.outputs[0], cube_001_1.inputs[0])
	#instance_on_points_002.Instances -> transform_geometry_004.Geometry
	bgi_grid_container.links.new(instance_on_points_002.outputs[0], transform_geometry_004.inputs[0])
	#math_034.Value -> combine_xyz_005.Y
	bgi_grid_container.links.new(math_034.outputs[0], combine_xyz_005.inputs[1])
	#group_input_006.Tickness -> math_021.Value
	bgi_grid_container.links.new(group_input_006.outputs[3], math_021.inputs[0])
	#combine_xyz_006.Vector -> transform_geometry_004.Translation
	bgi_grid_container.links.new(combine_xyz_006.outputs[0], transform_geometry_004.inputs[1])
	#math_023.Value -> combine_xyz_006.Z
	bgi_grid_container.links.new(math_023.outputs[0], combine_xyz_006.inputs[2])
	#math_022.Value -> math_023.Value
	bgi_grid_container.links.new(math_022.outputs[0], math_023.inputs[0])
	#cube_001_1.Mesh -> scale_elements.Geometry
	bgi_grid_container.links.new(cube_001_1.outputs[0], scale_elements.inputs[0])
	#position.Position -> separate_xyz.Vector
	bgi_grid_container.links.new(position.outputs[0], separate_xyz.inputs[0])
	#separate_xyz.Z -> compare.A
	bgi_grid_container.links.new(separate_xyz.outputs[2], compare.inputs[2])
	#separate_xyz.Z -> compare.A
	bgi_grid_container.links.new(separate_xyz.outputs[2], compare.inputs[0])
	#compare.Result -> scale_elements.Selection
	bgi_grid_container.links.new(compare.outputs[0], scale_elements.inputs[1])
	#transform_geometry_004.Geometry -> realize_instances.Geometry
	bgi_grid_container.links.new(transform_geometry_004.outputs[0], realize_instances.inputs[0])
	#transform_geometry_002.Geometry -> realize_instances_001.Geometry
	bgi_grid_container.links.new(transform_geometry_002.outputs[0], realize_instances_001.inputs[0])
	#group_input_007.Inner Height -> math_022.Value
	bgi_grid_container.links.new(group_input_007.outputs[2], math_022.inputs[0])
	#group_input_007.Tickness -> math_023.Value
	bgi_grid_container.links.new(group_input_007.outputs[3], math_023.inputs[1])
	#realize_instances_001.Geometry -> mesh_boolean.Mesh 1
	bgi_grid_container.links.new(realize_instances_001.outputs[0], mesh_boolean.inputs[0])
	#scale_elements.Geometry -> instance_on_points_002.Instance
	bgi_grid_container.links.new(scale_elements.outputs[0], instance_on_points_002.inputs[2])
	#math_027.Value -> scale_elements.Scale
	bgi_grid_container.links.new(math_027.outputs[0], scale_elements.inputs[2])
	#transform_geometry_003_1.Geometry -> realize_instances_002.Geometry
	bgi_grid_container.links.new(transform_geometry_003_1.outputs[0], realize_instances_002.inputs[0])
	#realize_instances_002.Geometry -> mesh_boolean_001.Mesh 1
	bgi_grid_container.links.new(realize_instances_002.outputs[0], mesh_boolean_001.inputs[0])
	#switch_001.Output -> mesh_boolean_001.Mesh 2
	bgi_grid_container.links.new(switch_001.outputs[0], mesh_boolean_001.inputs[1])
	#switch_1.Output -> mesh_boolean.Mesh 2
	bgi_grid_container.links.new(switch_1.outputs[0], mesh_boolean.inputs[1])
	#group_input_008.Cut Side 1 -> switch_1.Switch
	bgi_grid_container.links.new(group_input_008.outputs[6], switch_1.inputs[0])
	#realize_instances.Geometry -> switch_1.True
	bgi_grid_container.links.new(realize_instances.outputs[0], switch_1.inputs[2])
	#group_input_009.Cut Side 2 -> switch_001.Switch
	bgi_grid_container.links.new(group_input_009.outputs[7], switch_001.inputs[0])
	#realize_instances.Geometry -> switch_001.True
	bgi_grid_container.links.new(realize_instances.outputs[0], switch_001.inputs[2])
	#math_021.Value -> math_020.Value
	bgi_grid_container.links.new(math_021.outputs[0], math_020.inputs[0])
	#group_input_006.Inner Length -> math_020.Value
	bgi_grid_container.links.new(group_input_006.outputs[1], math_020.inputs[1])
	#group_input_010.Cut Size Top -> math_027.Value
	bgi_grid_container.links.new(group_input_010.outputs[9], math_027.inputs[0])
	#group_input_010.Cut Size Bottom -> math_027.Value
	bgi_grid_container.links.new(group_input_010.outputs[10], math_027.inputs[1])
	#group_input_010.Inner Height -> combine_xyz_005.Z
	bgi_grid_container.links.new(group_input_010.outputs[2], combine_xyz_005.inputs[2])
	#group_input_010.Cut Size Bottom -> combine_xyz_005.X
	bgi_grid_container.links.new(group_input_010.outputs[10], combine_xyz_005.inputs[0])
	#reroute_006.Output -> reroute_010.Input
	bgi_grid_container.links.new(reroute_006.outputs[0], reroute_010.inputs[0])
	#join_geometry.Geometry -> realize_instances_003.Geometry
	bgi_grid_container.links.new(join_geometry.outputs[0], realize_instances_003.inputs[0])
	#realize_instances_003.Geometry -> group_output_1.Geometry
	bgi_grid_container.links.new(realize_instances_003.outputs[0], group_output_1.inputs[0])
	#math_024.Value -> math_003.Value
	bgi_grid_container.links.new(math_024.outputs[0], math_003.inputs[1])
	#math_025.Value -> math_024.Value
	bgi_grid_container.links.new(math_025.outputs[0], math_024.inputs[1])
	#group_input_012.Count Length -> math_004_1.Value
	bgi_grid_container.links.new(group_input_012.outputs[5], math_004_1.inputs[1])
	#group_input_012.Count Length -> math_025.Value
	bgi_grid_container.links.new(group_input_012.outputs[5], math_025.inputs[0])
	#group_input_012.Tickness -> math_024.Value
	bgi_grid_container.links.new(group_input_012.outputs[3], math_024.inputs[0])
	#group_input_012.Inner Length -> math_004_1.Value
	bgi_grid_container.links.new(group_input_012.outputs[1], math_004_1.inputs[0])
	#group_input_002_1.Count Length -> math_026.Value
	bgi_grid_container.links.new(group_input_002_1.outputs[5], math_026.inputs[1])
	#group_input_002_1.Inner Length -> math_026.Value
	bgi_grid_container.links.new(group_input_002_1.outputs[1], math_026.inputs[0])
	#group_input_002_1.Count Length -> math_028.Value
	bgi_grid_container.links.new(group_input_002_1.outputs[5], math_028.inputs[0])
	#math_026.Value -> math_029.Value
	bgi_grid_container.links.new(math_026.outputs[0], math_029.inputs[1])
	#math_029.Value -> group.Length
	bgi_grid_container.links.new(math_029.outputs[0], group.inputs[1])
	#math_028.Value -> math_030.Value
	bgi_grid_container.links.new(math_028.outputs[0], math_030.inputs[0])
	#group_input_002_1.Tickness -> math_030.Value
	bgi_grid_container.links.new(group_input_002_1.outputs[3], math_030.inputs[1])
	#math_030.Value -> math_029.Value
	bgi_grid_container.links.new(math_030.outputs[0], math_029.inputs[0])
	#mesh_boolean_001.Mesh -> join_geometry.Geometry
	bgi_grid_container.links.new(mesh_boolean_001.outputs[0], join_geometry.inputs[0])
	#group_input_013.Inner Height -> group.Height
	bgi_grid_container.links.new(group_input_013.outputs[2], group.inputs[2])
	#group_input_013.Tickness -> group.Thickness
	bgi_grid_container.links.new(group_input_013.outputs[3], group.inputs[3])
	#group_input_005.Count Length -> math_010_1.Value
	bgi_grid_container.links.new(group_input_005.outputs[5], math_010_1.inputs[0])
	#math_016.Value -> math_015.Value
	bgi_grid_container.links.new(math_016.outputs[0], math_015.inputs[2])
	#math_015.Value -> math_031.Value
	bgi_grid_container.links.new(math_015.outputs[0], math_031.inputs[0])
	#math_032.Value -> combine_xyz_004.Y
	bgi_grid_container.links.new(math_032.outputs[0], combine_xyz_004.inputs[1])
	#group_input_014.Inner Length -> math_015.Value
	bgi_grid_container.links.new(group_input_014.outputs[1], math_015.inputs[0])
	#group_input_014.Count Length -> math_015.Value
	bgi_grid_container.links.new(group_input_014.outputs[5], math_015.inputs[1])
	#math_010_1.Value -> math_016.Value
	bgi_grid_container.links.new(math_010_1.outputs[0], math_016.inputs[1])
	#group_input_014.Tickness -> math_016.Value
	bgi_grid_container.links.new(group_input_014.outputs[3], math_016.inputs[0])
	#math_031.Value -> math_032.Value
	bgi_grid_container.links.new(math_031.outputs[0], math_032.inputs[0])
	#math_033.Value -> math_032.Value
	bgi_grid_container.links.new(math_033.outputs[0], math_032.inputs[1])
	#group_input_015.Tickness -> math_033.Value
	bgi_grid_container.links.new(group_input_015.outputs[3], math_033.inputs[0])
	#math_020.Value -> math_034.Value
	bgi_grid_container.links.new(math_020.outputs[0], math_034.inputs[0])
	#group_input_010.Count Length -> math_034.Value
	bgi_grid_container.links.new(group_input_010.outputs[5], math_034.inputs[1])
	#reroute_006.Output -> reroute_1.Input
	bgi_grid_container.links.new(reroute_006.outputs[0], reroute_1.inputs[0])
	#reroute_003.Output -> reroute_001.Input
	bgi_grid_container.links.new(reroute_003.outputs[0], reroute_001.inputs[0])
	#reroute_001.Output -> transform_geometry_003_1.Geometry
	bgi_grid_container.links.new(reroute_001.outputs[0], transform_geometry_003_1.inputs[0])
	#combine_xyz_010.Vector -> mesh_line_001.Offset
	bgi_grid_container.links.new(combine_xyz_010.outputs[0], mesh_line_001.inputs[3])
	#math_035.Value -> combine_xyz_010.Y
	bgi_grid_container.links.new(math_035.outputs[0], combine_xyz_010.inputs[1])
	#group_input_019.Count Length -> math_041.Value
	bgi_grid_container.links.new(group_input_019.outputs[5], math_041.inputs[0])
	#math_041.Value -> mesh_line_001.Count
	bgi_grid_container.links.new(math_041.outputs[0], mesh_line_001.inputs[0])
	#group_input_017.Inner Length -> math_035.Value
	bgi_grid_container.links.new(group_input_017.outputs[1], math_035.inputs[0])
	#group_input_017.Tickness -> math_035.Value
	bgi_grid_container.links.new(group_input_017.outputs[3], math_035.inputs[1])
	#mesh_to_points_001.Points -> instance_on_points_003.Points
	bgi_grid_container.links.new(mesh_to_points_001.outputs[0], instance_on_points_003.inputs[0])
	#mesh_line_001.Mesh -> mesh_to_points_001.Mesh
	bgi_grid_container.links.new(mesh_line_001.outputs[0], mesh_to_points_001.inputs[0])
	#combine_xyz_009.Vector -> mesh_line_001.Start Location
	bgi_grid_container.links.new(combine_xyz_009.outputs[0], mesh_line_001.inputs[2])
	#math_036.Value -> combine_xyz_009.Y
	bgi_grid_container.links.new(math_036.outputs[0], combine_xyz_009.inputs[1])
	#group_input_017.Count Length -> math_038.Value
	bgi_grid_container.links.new(group_input_017.outputs[5], math_038.inputs[0])
	#math_038.Value -> math_037.Value
	bgi_grid_container.links.new(math_038.outputs[0], math_037.inputs[0])
	#math_035.Value -> math_037.Value
	bgi_grid_container.links.new(math_035.outputs[0], math_037.inputs[1])
	#math_037.Value -> math_036.Value
	bgi_grid_container.links.new(math_037.outputs[0], math_036.inputs[0])
	#instance_on_points_001.Instances -> reroute_003.Input
	bgi_grid_container.links.new(instance_on_points_001.outputs[0], reroute_003.inputs[0])
	#reroute_003.Output -> instance_on_points_003.Instance
	bgi_grid_container.links.new(reroute_003.outputs[0], instance_on_points_003.inputs[2])
	#instance_on_points_003.Instances -> realize_instances_004.Geometry
	bgi_grid_container.links.new(instance_on_points_003.outputs[0], realize_instances_004.inputs[0])
	#realize_instances_004.Geometry -> mesh_boolean_002.Mesh 1
	bgi_grid_container.links.new(realize_instances_004.outputs[0], mesh_boolean_002.inputs[0])
	#switch_002_1.Output -> mesh_boolean_002.Mesh 2
	bgi_grid_container.links.new(switch_002_1.outputs[0], mesh_boolean_002.inputs[1])
	#group_input_016.Cut inner -> switch_002_1.Switch
	bgi_grid_container.links.new(group_input_016.outputs[8], switch_002_1.inputs[0])
	#realize_instances.Geometry -> switch_002_1.True
	bgi_grid_container.links.new(realize_instances.outputs[0], switch_002_1.inputs[2])
	#reroute_010.Output -> reroute_002.Input
	bgi_grid_container.links.new(reroute_010.outputs[0], reroute_002.inputs[0])
	#realize_instances_004.Geometry -> domain_size.Geometry
	bgi_grid_container.links.new(realize_instances_004.outputs[0], domain_size.inputs[0])
	#compare_001.Result -> switch_003.Switch
	bgi_grid_container.links.new(compare_001.outputs[0], switch_003.inputs[0])
	#domain_size.Edge Count -> compare_001.A
	bgi_grid_container.links.new(domain_size.outputs[1], compare_001.inputs[2])
	#mesh_boolean_002.Mesh -> switch_003.True
	bgi_grid_container.links.new(mesh_boolean_002.outputs[0], switch_003.inputs[2])
	#mesh_boolean.Mesh -> join_geometry.Geometry
	bgi_grid_container.links.new(mesh_boolean.outputs[0], join_geometry.inputs[0])
	#switch_003.Output -> join_geometry.Geometry
	bgi_grid_container.links.new(switch_003.outputs[0], join_geometry.inputs[0])
	#instance_on_points.Instances -> join_geometry.Geometry
	bgi_grid_container.links.new(instance_on_points.outputs[0], join_geometry.inputs[0])
	#transform_geometry.Geometry -> join_geometry.Geometry
	bgi_grid_container.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
	return bgi_grid_container

def bgi_grid_container_create():
	bgi_divisor = bgi_divisor_create()

	return bgi_grid_container_node_group(bgi_divisor)