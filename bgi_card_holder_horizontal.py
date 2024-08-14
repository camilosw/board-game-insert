import bpy

import bgi_divisor

import importlib

importlib.reload(bgi_divisor)

from bgi_divisor import bgi_divisor_create

#initialize bgi_card_holder_horizontal node group
def bgi_card_holder_horizontal_node_group(bgi_divisor):
	bgi_card_holder_horizontal = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Card Holder Horizontal")

	bgi_card_holder_horizontal.is_modifier = True
	
	#initialize bgi_card_holder_horizontal nodes
	#bgi_card_holder_horizontal interface
	#Socket Geometry
	geometry_socket_1 = bgi_card_holder_horizontal.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_1.attribute_domain = 'POINT'
	
	#Socket Inner Width
	inner_width_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Inner Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_width_socket.subtype = 'DISTANCE'
	inner_width_socket.default_value = 0.10000000149011612
	inner_width_socket.min_value = 0.0
	inner_width_socket.max_value = 3.4028234663852886e+38
	inner_width_socket.attribute_domain = 'POINT'
	
	#Socket Inner Length
	inner_length_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Inner Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_length_socket.subtype = 'DISTANCE'
	inner_length_socket.default_value = 0.10000000149011612
	inner_length_socket.min_value = 0.0
	inner_length_socket.max_value = 3.4028234663852886e+38
	inner_length_socket.attribute_domain = 'POINT'
	
	#Socket Inner Height
	inner_height_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Inner Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_height_socket.subtype = 'DISTANCE'
	inner_height_socket.default_value = 0.05000000074505806
	inner_height_socket.min_value = 0.0
	inner_height_socket.max_value = 3.4028234663852886e+38
	inner_height_socket.attribute_domain = 'POINT'
	
	#Socket Tickness
	tickness_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Tickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	tickness_socket.subtype = 'DISTANCE'
	tickness_socket.default_value = 0.005000000353902578
	tickness_socket.min_value = 0.0
	tickness_socket.max_value = 3.4028234663852886e+38
	tickness_socket.attribute_domain = 'POINT'
	
	#Socket Count
	count_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
	count_socket.subtype = 'NONE'
	count_socket.default_value = 1
	count_socket.min_value = 1
	count_socket.max_value = 2147483647
	count_socket.attribute_domain = 'POINT'
	
	#Socket Cut Side 1
	cut_side_1_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Cut Side 1", in_out='INPUT', socket_type = 'NodeSocketBool')
	cut_side_1_socket.attribute_domain = 'POINT'
	
	#Socket Cut Side 2
	cut_side_2_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Cut Side 2", in_out='INPUT', socket_type = 'NodeSocketBool')
	cut_side_2_socket.attribute_domain = 'POINT'
	
	#Socket Cut Size Top
	cut_size_top_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Cut Size Top", in_out='INPUT', socket_type = 'NodeSocketFloat')
	cut_size_top_socket.subtype = 'DISTANCE'
	cut_size_top_socket.default_value = 0.029999999329447746
	cut_size_top_socket.min_value = 0.0010000000474974513
	cut_size_top_socket.max_value = 3.4028234663852886e+38
	cut_size_top_socket.attribute_domain = 'POINT'
	
	#Socket Cut Size Bottom
	cut_size_bottom_socket = bgi_card_holder_horizontal.interface.new_socket(name = "Cut Size Bottom", in_out='INPUT', socket_type = 'NodeSocketFloat')
	cut_size_bottom_socket.subtype = 'DISTANCE'
	cut_size_bottom_socket.default_value = 0.019999999552965164
	cut_size_bottom_socket.min_value = 0.0
	cut_size_bottom_socket.max_value = 3.4028234663852886e+38
	cut_size_bottom_socket.attribute_domain = 'POINT'
	
	
	#node Frame.001
	frame_001_1 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_001_1.label = "Divisions location"
	frame_001_1.name = "Frame.001"
	frame_001_1.label_size = 20
	frame_001_1.shrink = True
	
	#node Frame.002
	frame_002 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_002.label = "Containers division"
	frame_002.name = "Frame.002"
	frame_002.label_size = 20
	frame_002.shrink = True
	
	#node Frame.003
	frame_003_1 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_003_1.label = "Sides"
	frame_003_1.name = "Frame.003"
	frame_003_1.label_size = 20
	frame_003_1.shrink = True
	
	#node Frame.005
	frame_005 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_005.label = "Select cut sides"
	frame_005.name = "Frame.005"
	frame_005.label_size = 20
	frame_005.shrink = True
	
	#node Frame.006
	frame_006 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_006.label = "Position cut shapes"
	frame_006.name = "Frame.006"
	frame_006.label_size = 20
	frame_006.shrink = True
	
	#node Frame.004
	frame_004 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_004.label = "Sides cut shape"
	frame_004.name = "Frame.004"
	frame_004.label_size = 20
	frame_004.shrink = True
	
	#node Frame
	frame_1 = bgi_card_holder_horizontal.nodes.new("NodeFrame")
	frame_1.label = "Base"
	frame_1.name = "Frame"
	frame_1.label_size = 20
	frame_1.shrink = True
	
	#node Reroute.008
	reroute_008 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_008.name = "Reroute.008"
	#node Math.017
	math_017 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_017.name = "Math.017"
	math_017.operation = 'MULTIPLY'
	math_017.use_clamp = False
	#Value_002
	math_017.inputs[2].default_value = 0.5
	
	#node Math.018
	math_018 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_018.name = "Math.018"
	math_018.operation = 'MULTIPLY'
	math_018.use_clamp = False
	#Value_001
	math_018.inputs[1].default_value = -1.0
	#Value_002
	math_018.inputs[2].default_value = 0.5
	
	#node Combine XYZ.003
	combine_xyz_003 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_003.name = "Combine XYZ.003"
	#Y
	combine_xyz_003.inputs[1].default_value = 0.0
	#Z
	combine_xyz_003.inputs[2].default_value = 0.0
	
	#node Group Input.003
	group_input_003_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_003_1.name = "Group Input.003"
	group_input_003_1.outputs[0].hide = True
	group_input_003_1.outputs[1].hide = True
	group_input_003_1.outputs[2].hide = True
	group_input_003_1.outputs[3].hide = True
	group_input_003_1.outputs[9].hide = True
	
	#node Mesh Line
	mesh_line = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshLine")
	mesh_line.name = "Mesh Line"
	mesh_line.count_mode = 'TOTAL'
	mesh_line.mode = 'OFFSET'
	#Resolution
	mesh_line.inputs[1].default_value = 1.0
	#Start Location
	mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Combine XYZ.002
	combine_xyz_002_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_002_1.name = "Combine XYZ.002"
	#Y
	combine_xyz_002_1.inputs[1].default_value = 0.0
	#Z
	combine_xyz_002_1.inputs[2].default_value = 0.0
	
	#node Math.007
	math_007 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_007.name = "Math.007"
	math_007.operation = 'DIVIDE'
	math_007.use_clamp = False
	#Value_001
	math_007.inputs[1].default_value = 2.0
	#Value_002
	math_007.inputs[2].default_value = 0.5
	
	#node Math.014
	math_014 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_014.name = "Math.014"
	math_014.operation = 'ADD'
	math_014.use_clamp = False
	#Value_002
	math_014.inputs[2].default_value = 0.5
	
	#node Math.009
	math_009_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_009_1.name = "Math.009"
	math_009_1.operation = 'ADD'
	math_009_1.use_clamp = False
	#Value_002
	math_009_1.inputs[2].default_value = 0.5
	
	#node Math.008
	math_008 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_008.name = "Math.008"
	math_008.operation = 'ADD'
	math_008.use_clamp = False
	#Value_001
	math_008.inputs[1].default_value = 1.0
	#Value_002
	math_008.inputs[2].default_value = 0.5
	
	#node Transform Geometry.001
	transform_geometry_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeTransform")
	transform_geometry_001.name = "Transform Geometry.001"
	#Rotation
	transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Mesh to Points
	mesh_to_points = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshToPoints")
	mesh_to_points.name = "Mesh to Points"
	mesh_to_points.mode = 'VERTICES'
	#Selection
	mesh_to_points.inputs[1].default_value = True
	#Position
	mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Radius
	mesh_to_points.inputs[3].default_value = 0.0020000000949949026
	
	#node Reroute.007
	reroute_007 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_007.name = "Reroute.007"
	#node Group
	group = bgi_card_holder_horizontal.nodes.new("GeometryNodeGroup")
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
	index = bgi_card_holder_horizontal.nodes.new("GeometryNodeInputIndex")
	index.name = "Index"
	
	#node Math.012
	math_012 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_012.name = "Math.012"
	math_012.operation = 'ADD'
	math_012.use_clamp = False
	#Value_001
	math_012.inputs[1].default_value = 1.0
	#Value_002
	math_012.inputs[2].default_value = 0.5
	
	#node Math.011
	math_011 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_011.name = "Math.011"
	math_011.operation = 'MODULO'
	math_011.use_clamp = False
	#Value_001
	math_011.inputs[1].default_value = 2.0
	#Value_002
	math_011.inputs[2].default_value = 0.5
	
	#node Instance on Points
	instance_on_points = bgi_card_holder_horizontal.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points.name = "Instance on Points"
	#Pick Instance
	instance_on_points.inputs[3].default_value = False
	#Instance Index
	instance_on_points.inputs[4].default_value = 0
	#Rotation
	instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Math.010
	math_010_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_010_1.name = "Math.010"
	math_010_1.operation = 'DIVIDE'
	math_010_1.use_clamp = False
	#Value_001
	math_010_1.inputs[1].default_value = 2.0
	#Value_002
	math_010_1.inputs[2].default_value = 0.5
	
	#node Math.016
	math_016 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_016.name = "Math.016"
	math_016.operation = 'DIVIDE'
	math_016.use_clamp = False
	#Value_001
	math_016.inputs[1].default_value = 2.0
	#Value_002
	math_016.inputs[2].default_value = 0.5
	
	#node Combine XYZ.004
	combine_xyz_004 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_004.name = "Combine XYZ.004"
	#X
	combine_xyz_004.inputs[0].default_value = 0.0
	#Z
	combine_xyz_004.inputs[2].default_value = 0.0
	
	#node Vector Math
	vector_math = bgi_card_holder_horizontal.nodes.new("ShaderNodeVectorMath")
	vector_math.name = "Vector Math"
	vector_math.operation = 'MULTIPLY'
	#Vector_001
	vector_math.inputs[1].default_value = (1.0, -1.0, 1.0)
	#Vector_002
	vector_math.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	vector_math.inputs[3].default_value = 1.0
	
	#node Math.013
	math_013 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_013.name = "Math.013"
	math_013.operation = 'MODULO'
	math_013.use_clamp = False
	#Value_001
	math_013.inputs[1].default_value = 2.0
	#Value_002
	math_013.inputs[2].default_value = 0.5
	
	#node Group.001
	group_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeGroup")
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
	index_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeInputIndex")
	index_001.name = "Index.001"
	
	#node Math.015
	math_015 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_015.name = "Math.015"
	math_015.operation = 'ADD'
	math_015.use_clamp = False
	#Value_002
	math_015.inputs[2].default_value = 0.5
	
	#node Instance on Points.001
	instance_on_points_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeInstanceOnPoints")
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
	transform_geometry_002 = bgi_card_holder_horizontal.nodes.new("GeometryNodeTransform")
	transform_geometry_002.name = "Transform Geometry.002"
	#Rotation
	transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Transform Geometry.003
	transform_geometry_003_1 = bgi_card_holder_horizontal.nodes.new("GeometryNodeTransform")
	transform_geometry_003_1.name = "Transform Geometry.003"
	#Rotation
	transform_geometry_003_1.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_003_1.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Reroute.009
	reroute_009 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_009.name = "Reroute.009"
	#node Reroute.005
	reroute_005 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_005.name = "Reroute.005"
	#node Reroute.006
	reroute_006 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_006.name = "Reroute.006"
	#node Reroute.010
	reroute_010 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_010.name = "Reroute.010"
	#node Mesh Boolean
	mesh_boolean = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshBoolean")
	mesh_boolean.name = "Mesh Boolean"
	mesh_boolean.operation = 'DIFFERENCE'
	#Self Intersection
	mesh_boolean.inputs[2].default_value = False
	#Hole Tolerant
	mesh_boolean.inputs[3].default_value = False
	
	#node Mesh Boolean.001
	mesh_boolean_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshBoolean")
	mesh_boolean_001.name = "Mesh Boolean.001"
	mesh_boolean_001.operation = 'DIFFERENCE'
	#Self Intersection
	mesh_boolean_001.inputs[2].default_value = False
	#Hole Tolerant
	mesh_boolean_001.inputs[3].default_value = False
	
	#node Switch.001
	switch_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeSwitch")
	switch_001.name = "Switch.001"
	switch_001.input_type = 'GEOMETRY'
	
	#node Group Input.009
	group_input_009 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_009.name = "Group Input.009"
	group_input_009.outputs[0].hide = True
	group_input_009.outputs[1].hide = True
	group_input_009.outputs[2].hide = True
	group_input_009.outputs[3].hide = True
	group_input_009.outputs[4].hide = True
	group_input_009.outputs[5].hide = True
	group_input_009.outputs[7].hide = True
	group_input_009.outputs[8].hide = True
	group_input_009.outputs[9].hide = True
	
	#node Group Input.008
	group_input_008 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_008.name = "Group Input.008"
	group_input_008.outputs[0].hide = True
	group_input_008.outputs[1].hide = True
	group_input_008.outputs[2].hide = True
	group_input_008.outputs[3].hide = True
	group_input_008.outputs[4].hide = True
	group_input_008.outputs[6].hide = True
	group_input_008.outputs[7].hide = True
	group_input_008.outputs[8].hide = True
	group_input_008.outputs[9].hide = True
	
	#node Realize Instances.001
	realize_instances_001 = bgi_card_holder_horizontal.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_001.name = "Realize Instances.001"
	
	#node Realize Instances.002
	realize_instances_002 = bgi_card_holder_horizontal.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_002.name = "Realize Instances.002"
	
	#node Realize Instances
	realize_instances = bgi_card_holder_horizontal.nodes.new("GeometryNodeRealizeInstances")
	realize_instances.name = "Realize Instances"
	
	#node Math.019
	math_019 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_019.name = "Math.019"
	math_019.operation = 'MODULO'
	math_019.use_clamp = False
	#Value_001
	math_019.inputs[1].default_value = 2.0
	#Value_002
	math_019.inputs[2].default_value = 0.5
	
	#node Group Input.007
	group_input_007 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_007.name = "Group Input.007"
	group_input_007.outputs[0].hide = True
	group_input_007.outputs[1].hide = True
	group_input_007.outputs[4].hide = True
	group_input_007.outputs[5].hide = True
	group_input_007.outputs[6].hide = True
	group_input_007.outputs[7].hide = True
	group_input_007.outputs[8].hide = True
	group_input_007.outputs[9].hide = True
	
	#node Transform Geometry.004
	transform_geometry_004 = bgi_card_holder_horizontal.nodes.new("GeometryNodeTransform")
	transform_geometry_004.name = "Transform Geometry.004"
	#Rotation
	transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.006
	combine_xyz_006 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_006.name = "Combine XYZ.006"
	#X
	combine_xyz_006.inputs[0].default_value = 0.0
	#Y
	combine_xyz_006.inputs[1].default_value = 0.0
	
	#node Instance on Points.002
	instance_on_points_002 = bgi_card_holder_horizontal.nodes.new("GeometryNodeInstanceOnPoints")
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
	math_023 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_023.name = "Math.023"
	math_023.operation = 'ADD'
	math_023.use_clamp = False
	#Value_002
	math_023.inputs[2].default_value = 0.5
	
	#node Math.022
	math_022 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_022.name = "Math.022"
	math_022.operation = 'DIVIDE'
	math_022.use_clamp = False
	#Value_001
	math_022.inputs[1].default_value = 2.0
	#Value_002
	math_022.inputs[2].default_value = 0.5
	
	#node Index.002
	index_002 = bgi_card_holder_horizontal.nodes.new("GeometryNodeInputIndex")
	index_002.name = "Index.002"
	
	#node Scale Elements
	scale_elements = bgi_card_holder_horizontal.nodes.new("GeometryNodeScaleElements")
	scale_elements.name = "Scale Elements"
	scale_elements.domain = 'FACE'
	scale_elements.scale_mode = 'SINGLE_AXIS'
	#Center
	scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
	#Axis
	scale_elements.inputs[4].default_value = (1.0, 0.0, 0.0)
	
	#node Math.027
	math_027 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_027.name = "Math.027"
	math_027.operation = 'DIVIDE'
	math_027.use_clamp = False
	#Value_002
	math_027.inputs[2].default_value = 0.5
	
	#node Compare
	compare = bgi_card_holder_horizontal.nodes.new("FunctionNodeCompare")
	compare.name = "Compare"
	compare.data_type = 'FLOAT'
	compare.mode = 'ELEMENT'
	compare.operation = 'GREATER_THAN'
	#B
	compare.inputs[1].default_value = 0.0
	#B_INT
	compare.inputs[3].default_value = 1
	#A_VEC3
	compare.inputs[4].default_value = (0.0, 0.0, 0.0)
	#B_VEC3
	compare.inputs[5].default_value = (0.0, 0.0, 0.0)
	#A_COL
	compare.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
	#B_COL
	compare.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
	#A_STR
	compare.inputs[8].default_value = ""
	#B_STR
	compare.inputs[9].default_value = ""
	#C
	compare.inputs[10].default_value = 0.8999999761581421
	#Angle
	compare.inputs[11].default_value = 0.08726649731397629
	#Epsilon
	compare.inputs[12].default_value = 0.0010000000474974513
	
	#node Separate XYZ
	separate_xyz = bgi_card_holder_horizontal.nodes.new("ShaderNodeSeparateXYZ")
	separate_xyz.name = "Separate XYZ"
	
	#node Position
	position = bgi_card_holder_horizontal.nodes.new("GeometryNodeInputPosition")
	position.name = "Position"
	
	#node Cube.001
	cube_001_1 = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshCube")
	cube_001_1.name = "Cube.001"
	#Vertices X
	cube_001_1.inputs[1].default_value = 2
	#Vertices Y
	cube_001_1.inputs[2].default_value = 2
	#Vertices Z
	cube_001_1.inputs[3].default_value = 2
	
	#node Combine XYZ.005
	combine_xyz_005 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_005.name = "Combine XYZ.005"
	
	#node Math.020
	math_020 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_020.name = "Math.020"
	math_020.operation = 'ADD'
	math_020.use_clamp = False
	#Value_002
	math_020.inputs[2].default_value = 0.5
	
	#node Math.021
	math_021 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_021.name = "Math.021"
	math_021.operation = 'MULTIPLY'
	math_021.use_clamp = False
	#Value_001
	math_021.inputs[1].default_value = 3.0
	#Value_002
	math_021.inputs[2].default_value = 0.5
	
	#node Group Input.006
	group_input_006 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_006.name = "Group Input.006"
	group_input_006.outputs[0].hide = True
	group_input_006.outputs[2].hide = True
	group_input_006.outputs[4].hide = True
	group_input_006.outputs[5].hide = True
	group_input_006.outputs[6].hide = True
	group_input_006.outputs[7].hide = True
	group_input_006.outputs[8].hide = True
	group_input_006.outputs[9].hide = True
	
	#node Group Input.010
	group_input_010 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_010.name = "Group Input.010"
	group_input_010.outputs[0].hide = True
	group_input_010.outputs[1].hide = True
	group_input_010.outputs[3].hide = True
	group_input_010.outputs[4].hide = True
	group_input_010.outputs[5].hide = True
	group_input_010.outputs[6].hide = True
	group_input_010.outputs[9].hide = True
	
	#node Reroute.011
	reroute_011 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_011.name = "Reroute.011"
	#node Group Input.001
	group_input_001_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_001_1.name = "Group Input.001"
	group_input_001_1.outputs[1].hide = True
	group_input_001_1.outputs[2].hide = True
	group_input_001_1.outputs[5].hide = True
	group_input_001_1.outputs[6].hide = True
	group_input_001_1.outputs[7].hide = True
	group_input_001_1.outputs[8].hide = True
	group_input_001_1.outputs[9].hide = True
	
	#node Group Input.002
	group_input_002_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_002_1.name = "Group Input.002"
	group_input_002_1.outputs[0].hide = True
	group_input_002_1.outputs[4].hide = True
	group_input_002_1.outputs[5].hide = True
	group_input_002_1.outputs[6].hide = True
	group_input_002_1.outputs[7].hide = True
	group_input_002_1.outputs[8].hide = True
	group_input_002_1.outputs[9].hide = True
	
	#node Group Input.004
	group_input_004_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_004_1.name = "Group Input.004"
	group_input_004_1.outputs[1].hide = True
	group_input_004_1.outputs[4].hide = True
	group_input_004_1.outputs[5].hide = True
	group_input_004_1.outputs[6].hide = True
	group_input_004_1.outputs[7].hide = True
	group_input_004_1.outputs[8].hide = True
	group_input_004_1.outputs[9].hide = True
	
	#node Group Input.005
	group_input_005 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_005.name = "Group Input.005"
	group_input_005.outputs[0].hide = True
	group_input_005.outputs[2].hide = True
	group_input_005.outputs[4].hide = True
	group_input_005.outputs[5].hide = True
	group_input_005.outputs[6].hide = True
	group_input_005.outputs[7].hide = True
	group_input_005.outputs[8].hide = True
	group_input_005.outputs[9].hide = True
	
	#node Combine XYZ.001
	combine_xyz_001 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_001.name = "Combine XYZ.001"
	#X
	combine_xyz_001.inputs[0].default_value = 0.0
	#Y
	combine_xyz_001.inputs[1].default_value = 0.0
	
	#node Combine XYZ
	combine_xyz_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_1.name = "Combine XYZ"
	
	#node Math
	math = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math.name = "Math"
	math.operation = 'DIVIDE'
	math.use_clamp = False
	#Value_001
	math.inputs[1].default_value = 2.0
	#Value_002
	math.inputs[2].default_value = 0.5
	
	#node Math.003
	math_003 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_003.name = "Math.003"
	math_003.operation = 'ADD'
	math_003.use_clamp = False
	#Value_002
	math_003.inputs[2].default_value = 0.5
	
	#node Transform Geometry
	transform_geometry = bgi_card_holder_horizontal.nodes.new("GeometryNodeTransform")
	transform_geometry.name = "Transform Geometry"
	#Rotation
	transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Math.004
	math_004_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_004_1.name = "Math.004"
	math_004_1.operation = 'MULTIPLY'
	math_004_1.use_clamp = False
	#Value_001
	math_004_1.inputs[1].default_value = 2.0
	#Value_002
	math_004_1.inputs[2].default_value = 0.5
	
	#node Math.002
	math_002 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_002.name = "Math.002"
	math_002.operation = 'ADD'
	math_002.use_clamp = False
	#Value_002
	math_002.inputs[2].default_value = 0.5
	
	#node Math.006
	math_006 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_006.name = "Math.006"
	math_006.operation = 'MULTIPLY'
	math_006.use_clamp = False
	#Value_002
	math_006.inputs[2].default_value = 0.5
	
	#node Math.001
	math_001 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_001.name = "Math.001"
	math_001.operation = 'MULTIPLY'
	math_001.use_clamp = False
	#Value_002
	math_001.inputs[2].default_value = 0.5
	
	#node Reroute.001
	reroute_001 = bgi_card_holder_horizontal.nodes.new("NodeReroute")
	reroute_001.name = "Reroute.001"
	#node Cube
	cube = bgi_card_holder_horizontal.nodes.new("GeometryNodeMeshCube")
	cube.name = "Cube"
	#Vertices X
	cube.inputs[1].default_value = 2
	#Vertices Y
	cube.inputs[2].default_value = 2
	#Vertices Z
	cube.inputs[3].default_value = 2
	
	#node Group Input.011
	group_input_011 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_011.name = "Group Input.011"
	group_input_011.outputs[0].hide = True
	group_input_011.outputs[2].hide = True
	group_input_011.outputs[4].hide = True
	group_input_011.outputs[5].hide = True
	group_input_011.outputs[6].hide = True
	group_input_011.outputs[7].hide = True
	group_input_011.outputs[8].hide = True
	group_input_011.outputs[9].hide = True
	
	#node Math.005
	math_005_1 = bgi_card_holder_horizontal.nodes.new("ShaderNodeMath")
	math_005_1.name = "Math.005"
	math_005_1.operation = 'ADD'
	math_005_1.use_clamp = False
	#Value_001
	math_005_1.inputs[1].default_value = 1.0
	#Value_002
	math_005_1.inputs[2].default_value = 0.5
	
	#node Group Input
	group_input_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupInput")
	group_input_1.name = "Group Input"
	group_input_1.outputs[1].hide = True
	group_input_1.outputs[2].hide = True
	group_input_1.outputs[5].hide = True
	group_input_1.outputs[6].hide = True
	group_input_1.outputs[7].hide = True
	group_input_1.outputs[8].hide = True
	group_input_1.outputs[9].hide = True
	
	#node Join Geometry
	join_geometry = bgi_card_holder_horizontal.nodes.new("GeometryNodeJoinGeometry")
	join_geometry.name = "Join Geometry"
	
	#node Realize Instances.003
	realize_instances_003 = bgi_card_holder_horizontal.nodes.new("GeometryNodeRealizeInstances")
	realize_instances_003.name = "Realize Instances.003"
	
	#node Group Output
	group_output_1 = bgi_card_holder_horizontal.nodes.new("NodeGroupOutput")
	group_output_1.name = "Group Output"
	group_output_1.is_active_output = True
	
	#node Switch
	switch_1 = bgi_card_holder_horizontal.nodes.new("GeometryNodeSwitch")
	switch_1.name = "Switch"
	switch_1.input_type = 'GEOMETRY'
	
	
	
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
	math_010_1.parent = frame_003_1
	math_016.parent = frame_003_1
	combine_xyz_004.parent = frame_003_1
	vector_math.parent = frame_003_1
	math_013.parent = frame_003_1
	group_001.parent = frame_003_1
	index_001.parent = frame_003_1
	math_015.parent = frame_003_1
	instance_on_points_001.parent = frame_003_1
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
	group_input_004_1.parent = frame_003_1
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
	reroute_001.parent = frame_1
	cube.parent = frame_1
	group_input_011.parent = frame_1
	math_005_1.parent = frame_1
	group_input_1.parent = frame_1
	switch_1.parent = frame_005
	
	#Set locations
	frame_001_1.location = (231.2939453125, -145.5316619873047)
	frame_002.location = (1018.2619018554688, 300.1052551269531)
	frame_003_1.location = (-107.77703857421875, 7.07269287109375)
	frame_005.location = (-110.5693359375, -157.72409057617188)
	frame_006.location = (-2.04754638671875, -50.1927490234375)
	frame_004.location = (-79.3367919921875, -17.8529052734375)
	frame_1.location = (-53.088623046875, 427.8203125)
	reroute_008.location = (-83.36905670166016, -1.4661725759506226)
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
	mesh_to_points.location = (-1628.218017578125, -188.933837890625)
	reroute_007.location = (-753.443359375, 0.0192413330078125)
	group.location = (-1356.1849365234375, -553.2692260742188)
	index.location = (-1681.7843017578125, -396.807373046875)
	math_012.location = (-1508.6417236328125, -378.8019714355469)
	math_011.location = (-1343.5811767578125, -367.1869201660156)
	instance_on_points.location = (-999.4872436523438, -383.5027770996094)
	math_010_1.location = (-610.96142578125, -1004.830810546875)
	math_016.location = (-608.8296508789062, -1181.7269287109375)
	combine_xyz_004.location = (-251.85081481933594, -1044.5400390625)
	vector_math.location = (-66.30834197998047, -1084.801513671875)
	math_013.location = (-593.50732421875, -598.6879272460938)
	group_001.location = (-602.20166015625, -776.6127319335938)
	index_001.location = (-805.9782104492188, -674.4490966796875)
	math_015.location = (-429.5523376464844, -1065.012451171875)
	instance_on_points_001.location = (-246.10621643066406, -701.3245239257812)
	transform_geometry_002.location = (130.9606170654297, -617.521484375)
	transform_geometry_003_1.location = (130.15040588378906, -886.720458984375)
	reroute_009.location = (-475.2469482421875, -522.6355590820312)
	reroute_005.location = (-883.7420043945312, -519.886962890625)
	reroute_006.location = (-1094.986083984375, -367.6512451171875)
	reroute_010.location = (-279.7698059082031, -1374.5543212890625)
	mesh_boolean.location = (848.8390502929688, -370.0494689941406)
	mesh_boolean_001.location = (859.90673828125, -616.9750366210938)
	switch_001.location = (637.9524536132812, -759.4254760742188)
	group_input_009.location = (419.7576599121094, -811.6616821289062)
	group_input_008.location = (424.8758850097656, -569.9468994140625)
	realize_instances_001.location = (423.8089904785156, -445.6916198730469)
	realize_instances_002.location = (421.0419006347656, -690.4024047851562)
	realize_instances.location = (425.85577392578125, -897.3543701171875)
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
	math_020.location = (-1420.873046875, -1555.11181640625)
	math_021.location = (-1602.955078125, -1503.0804443359375)
	group_input_006.location = (-1796.353759765625, -1651.0413818359375)
	group_input_010.location = (-1417.956787109375, -1739.4085693359375)
	reroute_011.location = (-969.4357299804688, -1377.138671875)
	group_input_001_1.location = (-2981.425048828125, -17.6748046875)
	group_input_002_1.location = (-1545.310302734375, -626.6314697265625)
	group_input_004_1.location = (-815.0081176757812, -827.990966796875)
	group_input_005.location = (-807.5728149414062, -1145.40625)
	combine_xyz_001.location = (-149.05105590820312, -226.1741943359375)
	combine_xyz_1.location = (-325.9454040527344, -50.780948638916016)
	math.location = (-329.0421447753906, -197.6778106689453)
	math_003.location = (-568.05908203125, -136.11904907226562)
	transform_geometry.location = (70.38475799560547, -40.947845458984375)
	math_004_1.location = (-769.612548828125, -124.79510498046875)
	math_002.location = (-553.548095703125, 53.7738037109375)
	math_006.location = (-763.4810791015625, 40.877532958984375)
	math_001.location = (-759.9774169921875, 204.79714965820312)
	reroute_001.location = (-382.6703796386719, -308.0303955078125)
	cube.location = (-146.71456909179688, -45.32170486450195)
	group_input_011.location = (-766.5849609375, -292.05438232421875)
	math_005_1.location = (-977.35986328125, 200.3018798828125)
	group_input_1.location = (-1192.7413330078125, -27.695465087890625)
	join_geometry.location = (1160.5408935546875, -54.734619140625)
	realize_instances_003.location = (1334.0, -58.0)
	group_output_1.location = (1508.0, -58.0)
	switch_1.location = (628.6666259765625, -515.6619262695312)
	
	#Set dimensions
	frame_001_1.width, frame_001_1.height = 1551.3333740234375, 671.8333129882812
	frame_002.width, frame_002.height = 880.0, 471.1666259765625
	frame_003_1.width, frame_003_1.height = 1144.0, 793.166748046875
	frame_005.width, frame_005.height = 637.9998779296875, 667.8333740234375
	frame_006.width, frame_006.height = 975.3333129882812, 633.1666259765625
	frame_004.width, frame_004.height = 1194.0, 587.166748046875
	frame_1.width, frame_1.height = 1461.3333740234375, 636.5
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
	math_010_1.width, math_010_1.height = 140.0, 100.0
	math_016.width, math_016.height = 140.0, 100.0
	combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
	vector_math.width, vector_math.height = 140.0, 100.0
	math_013.width, math_013.height = 140.0, 100.0
	group_001.width, group_001.height = 140.0, 100.0
	index_001.width, index_001.height = 140.0, 100.0
	math_015.width, math_015.height = 140.0, 100.0
	instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
	transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
	transform_geometry_003_1.width, transform_geometry_003_1.height = 140.0, 100.0
	reroute_009.width, reroute_009.height = 16.0, 100.0
	reroute_005.width, reroute_005.height = 16.0, 100.0
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
	reroute_011.width, reroute_011.height = 16.0, 100.0
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
	reroute_001.width, reroute_001.height = 16.0, 100.0
	cube.width, cube.height = 140.0, 100.0
	group_input_011.width, group_input_011.height = 140.0, 100.0
	math_005_1.width, math_005_1.height = 140.0, 100.0
	group_input_1.width, group_input_1.height = 140.0, 100.0
	join_geometry.width, join_geometry.height = 140.0, 100.0
	realize_instances_003.width, realize_instances_003.height = 140.0, 100.0
	group_output_1.width, group_output_1.height = 140.0, 100.0
	switch_1.width, switch_1.height = 140.0, 100.0
	
	#initialize bgi_card_holder_horizontal links
	#combine_xyz_1.Vector -> cube.Size
	bgi_card_holder_horizontal.links.new(combine_xyz_1.outputs[0], cube.inputs[0])
	#cube.Mesh -> transform_geometry.Geometry
	bgi_card_holder_horizontal.links.new(cube.outputs[0], transform_geometry.inputs[0])
	#reroute_001.Output -> math.Value
	bgi_card_holder_horizontal.links.new(reroute_001.outputs[0], math.inputs[0])
	#combine_xyz_001.Vector -> transform_geometry.Translation
	bgi_card_holder_horizontal.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
	#math.Value -> combine_xyz_001.Z
	bgi_card_holder_horizontal.links.new(math.outputs[0], combine_xyz_001.inputs[2])
	#math_001.Value -> math_002.Value
	bgi_card_holder_horizontal.links.new(math_001.outputs[0], math_002.inputs[0])
	#math_002.Value -> combine_xyz_1.X
	bgi_card_holder_horizontal.links.new(math_002.outputs[0], combine_xyz_1.inputs[0])
	#math_003.Value -> combine_xyz_1.Y
	bgi_card_holder_horizontal.links.new(math_003.outputs[0], combine_xyz_1.inputs[1])
	#reroute_001.Output -> combine_xyz_1.Z
	bgi_card_holder_horizontal.links.new(reroute_001.outputs[0], combine_xyz_1.inputs[2])
	#math_006.Value -> math_002.Value
	bgi_card_holder_horizontal.links.new(math_006.outputs[0], math_002.inputs[1])
	#math_004_1.Value -> math_003.Value
	bgi_card_holder_horizontal.links.new(math_004_1.outputs[0], math_003.inputs[0])
	#group_input_1.Count -> math_005_1.Value
	bgi_card_holder_horizontal.links.new(group_input_1.outputs[4], math_005_1.inputs[0])
	#group_input_1.Inner Width -> math_006.Value
	bgi_card_holder_horizontal.links.new(group_input_1.outputs[0], math_006.inputs[0])
	#group_input_1.Count -> math_006.Value
	bgi_card_holder_horizontal.links.new(group_input_1.outputs[4], math_006.inputs[1])
	#group_input_1.Tickness -> math_004_1.Value
	bgi_card_holder_horizontal.links.new(group_input_1.outputs[3], math_004_1.inputs[0])
	#group_input_1.Tickness -> math_001.Value
	bgi_card_holder_horizontal.links.new(group_input_1.outputs[3], math_001.inputs[1])
	#math_005_1.Value -> math_001.Value
	bgi_card_holder_horizontal.links.new(math_005_1.outputs[0], math_001.inputs[0])
	#combine_xyz_002_1.Vector -> mesh_line.Offset
	bgi_card_holder_horizontal.links.new(combine_xyz_002_1.outputs[0], mesh_line.inputs[3])
	#math_007.Value -> combine_xyz_002_1.X
	bgi_card_holder_horizontal.links.new(math_007.outputs[0], combine_xyz_002_1.inputs[0])
	#group_input_001_1.Count -> math_008.Value
	bgi_card_holder_horizontal.links.new(group_input_001_1.outputs[4], math_008.inputs[0])
	#math_008.Value -> math_009_1.Value
	bgi_card_holder_horizontal.links.new(math_008.outputs[0], math_009_1.inputs[0])
	#group_input_001_1.Count -> math_009_1.Value
	bgi_card_holder_horizontal.links.new(group_input_001_1.outputs[4], math_009_1.inputs[1])
	#math_009_1.Value -> mesh_line.Count
	bgi_card_holder_horizontal.links.new(math_009_1.outputs[0], mesh_line.inputs[0])
	#mesh_line.Mesh -> transform_geometry_001.Geometry
	bgi_card_holder_horizontal.links.new(mesh_line.outputs[0], transform_geometry_001.inputs[0])
	#combine_xyz_003.Vector -> transform_geometry_001.Translation
	bgi_card_holder_horizontal.links.new(combine_xyz_003.outputs[0], transform_geometry_001.inputs[1])
	#group_input_002_1.Tickness -> group.Thickness
	bgi_card_holder_horizontal.links.new(group_input_002_1.outputs[3], group.inputs[3])
	#group_input_002_1.Inner Height -> group.Height
	bgi_card_holder_horizontal.links.new(group_input_002_1.outputs[2], group.inputs[2])
	#group_input_002_1.Inner Length -> group.Length
	bgi_card_holder_horizontal.links.new(group_input_002_1.outputs[1], group.inputs[1])
	#transform_geometry_001.Geometry -> mesh_to_points.Mesh
	bgi_card_holder_horizontal.links.new(transform_geometry_001.outputs[0], mesh_to_points.inputs[0])
	#reroute_008.Output -> instance_on_points.Points
	bgi_card_holder_horizontal.links.new(reroute_008.outputs[0], instance_on_points.inputs[0])
	#group.Geometry -> instance_on_points.Instance
	bgi_card_holder_horizontal.links.new(group.outputs[0], instance_on_points.inputs[2])
	#math_011.Value -> instance_on_points.Selection
	bgi_card_holder_horizontal.links.new(math_011.outputs[0], instance_on_points.inputs[1])
	#index.Index -> math_012.Value
	bgi_card_holder_horizontal.links.new(index.outputs[0], math_012.inputs[0])
	#math_012.Value -> math_011.Value
	bgi_card_holder_horizontal.links.new(math_012.outputs[0], math_011.inputs[0])
	#group_input_001_1.Tickness -> math_014.Value
	bgi_card_holder_horizontal.links.new(group_input_001_1.outputs[3], math_014.inputs[1])
	#group_input_001_1.Inner Width -> math_014.Value
	bgi_card_holder_horizontal.links.new(group_input_001_1.outputs[0], math_014.inputs[0])
	#math_014.Value -> math_007.Value
	bgi_card_holder_horizontal.links.new(math_014.outputs[0], math_007.inputs[0])
	#math_007.Value -> math_017.Value
	bgi_card_holder_horizontal.links.new(math_007.outputs[0], math_017.inputs[0])
	#math_018.Value -> combine_xyz_003.X
	bgi_card_holder_horizontal.links.new(math_018.outputs[0], combine_xyz_003.inputs[0])
	#math_017.Value -> math_018.Value
	bgi_card_holder_horizontal.links.new(math_017.outputs[0], math_018.inputs[0])
	#group_input_003_1.Count -> math_017.Value
	bgi_card_holder_horizontal.links.new(group_input_003_1.outputs[4], math_017.inputs[1])
	#group_input_004_1.Tickness -> group_001.Thickness
	bgi_card_holder_horizontal.links.new(group_input_004_1.outputs[3], group_001.inputs[3])
	#group_input_004_1.Inner Height -> group_001.Height
	bgi_card_holder_horizontal.links.new(group_input_004_1.outputs[2], group_001.inputs[2])
	#group_001.Geometry -> instance_on_points_001.Instance
	bgi_card_holder_horizontal.links.new(group_001.outputs[0], instance_on_points_001.inputs[2])
	#math_013.Value -> instance_on_points_001.Selection
	bgi_card_holder_horizontal.links.new(math_013.outputs[0], instance_on_points_001.inputs[1])
	#index_001.Index -> math_013.Value
	bgi_card_holder_horizontal.links.new(index_001.outputs[0], math_013.inputs[0])
	#reroute_009.Output -> instance_on_points_001.Points
	bgi_card_holder_horizontal.links.new(reroute_009.outputs[0], instance_on_points_001.inputs[0])
	#group_input_004_1.Inner Width -> group_001.Width
	bgi_card_holder_horizontal.links.new(group_input_004_1.outputs[0], group_001.inputs[0])
	#instance_on_points_001.Instances -> transform_geometry_002.Geometry
	bgi_card_holder_horizontal.links.new(instance_on_points_001.outputs[0], transform_geometry_002.inputs[0])
	#combine_xyz_004.Vector -> transform_geometry_002.Translation
	bgi_card_holder_horizontal.links.new(combine_xyz_004.outputs[0], transform_geometry_002.inputs[1])
	#mesh_boolean.Mesh -> join_geometry.Geometry
	bgi_card_holder_horizontal.links.new(mesh_boolean.outputs[0], join_geometry.inputs[0])
	#group_input_005.Inner Length -> math_010_1.Value
	bgi_card_holder_horizontal.links.new(group_input_005.outputs[1], math_010_1.inputs[0])
	#math_010_1.Value -> math_015.Value
	bgi_card_holder_horizontal.links.new(math_010_1.outputs[0], math_015.inputs[0])
	#math_015.Value -> combine_xyz_004.Y
	bgi_card_holder_horizontal.links.new(math_015.outputs[0], combine_xyz_004.inputs[1])
	#group_input_005.Tickness -> math_016.Value
	bgi_card_holder_horizontal.links.new(group_input_005.outputs[3], math_016.inputs[0])
	#math_016.Value -> math_015.Value
	bgi_card_holder_horizontal.links.new(math_016.outputs[0], math_015.inputs[1])
	#combine_xyz_004.Vector -> vector_math.Vector
	bgi_card_holder_horizontal.links.new(combine_xyz_004.outputs[0], vector_math.inputs[0])
	#vector_math.Vector -> transform_geometry_003_1.Translation
	bgi_card_holder_horizontal.links.new(vector_math.outputs[0], transform_geometry_003_1.inputs[1])
	#instance_on_points_001.Instances -> transform_geometry_003_1.Geometry
	bgi_card_holder_horizontal.links.new(instance_on_points_001.outputs[0], transform_geometry_003_1.inputs[0])
	#mesh_to_points.Points -> reroute_006.Input
	bgi_card_holder_horizontal.links.new(mesh_to_points.outputs[0], reroute_006.inputs[0])
	#reroute_006.Output -> reroute_007.Input
	bgi_card_holder_horizontal.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
	#reroute_007.Output -> reroute_008.Input
	bgi_card_holder_horizontal.links.new(reroute_007.outputs[0], reroute_008.inputs[0])
	#reroute_006.Output -> reroute_005.Input
	bgi_card_holder_horizontal.links.new(reroute_006.outputs[0], reroute_005.inputs[0])
	#reroute_005.Output -> reroute_009.Input
	bgi_card_holder_horizontal.links.new(reroute_005.outputs[0], reroute_009.inputs[0])
	#reroute_010.Output -> instance_on_points_002.Points
	bgi_card_holder_horizontal.links.new(reroute_010.outputs[0], instance_on_points_002.inputs[0])
	#math_019.Value -> instance_on_points_002.Selection
	bgi_card_holder_horizontal.links.new(math_019.outputs[0], instance_on_points_002.inputs[1])
	#index_002.Index -> math_019.Value
	bgi_card_holder_horizontal.links.new(index_002.outputs[0], math_019.inputs[0])
	#combine_xyz_005.Vector -> cube_001_1.Size
	bgi_card_holder_horizontal.links.new(combine_xyz_005.outputs[0], cube_001_1.inputs[0])
	#instance_on_points_002.Instances -> transform_geometry_004.Geometry
	bgi_card_holder_horizontal.links.new(instance_on_points_002.outputs[0], transform_geometry_004.inputs[0])
	#math_020.Value -> combine_xyz_005.Y
	bgi_card_holder_horizontal.links.new(math_020.outputs[0], combine_xyz_005.inputs[1])
	#group_input_006.Tickness -> math_021.Value
	bgi_card_holder_horizontal.links.new(group_input_006.outputs[3], math_021.inputs[0])
	#combine_xyz_006.Vector -> transform_geometry_004.Translation
	bgi_card_holder_horizontal.links.new(combine_xyz_006.outputs[0], transform_geometry_004.inputs[1])
	#math_023.Value -> combine_xyz_006.Z
	bgi_card_holder_horizontal.links.new(math_023.outputs[0], combine_xyz_006.inputs[2])
	#math_022.Value -> math_023.Value
	bgi_card_holder_horizontal.links.new(math_022.outputs[0], math_023.inputs[0])
	#cube_001_1.Mesh -> scale_elements.Geometry
	bgi_card_holder_horizontal.links.new(cube_001_1.outputs[0], scale_elements.inputs[0])
	#position.Position -> separate_xyz.Vector
	bgi_card_holder_horizontal.links.new(position.outputs[0], separate_xyz.inputs[0])
	#separate_xyz.Z -> compare.A
	bgi_card_holder_horizontal.links.new(separate_xyz.outputs[2], compare.inputs[2])
	#separate_xyz.Z -> compare.A
	bgi_card_holder_horizontal.links.new(separate_xyz.outputs[2], compare.inputs[0])
	#compare.Result -> scale_elements.Selection
	bgi_card_holder_horizontal.links.new(compare.outputs[0], scale_elements.inputs[1])
	#transform_geometry_004.Geometry -> realize_instances.Geometry
	bgi_card_holder_horizontal.links.new(transform_geometry_004.outputs[0], realize_instances.inputs[0])
	#transform_geometry_002.Geometry -> realize_instances_001.Geometry
	bgi_card_holder_horizontal.links.new(transform_geometry_002.outputs[0], realize_instances_001.inputs[0])
	#group_input_007.Inner Height -> math_022.Value
	bgi_card_holder_horizontal.links.new(group_input_007.outputs[2], math_022.inputs[0])
	#group_input_007.Tickness -> math_023.Value
	bgi_card_holder_horizontal.links.new(group_input_007.outputs[3], math_023.inputs[1])
	#realize_instances_001.Geometry -> mesh_boolean.Mesh 1
	bgi_card_holder_horizontal.links.new(realize_instances_001.outputs[0], mesh_boolean.inputs[0])
	#scale_elements.Geometry -> instance_on_points_002.Instance
	bgi_card_holder_horizontal.links.new(scale_elements.outputs[0], instance_on_points_002.inputs[2])
	#math_027.Value -> scale_elements.Scale
	bgi_card_holder_horizontal.links.new(math_027.outputs[0], scale_elements.inputs[2])
	#transform_geometry_003_1.Geometry -> realize_instances_002.Geometry
	bgi_card_holder_horizontal.links.new(transform_geometry_003_1.outputs[0], realize_instances_002.inputs[0])
	#realize_instances_002.Geometry -> mesh_boolean_001.Mesh 1
	bgi_card_holder_horizontal.links.new(realize_instances_002.outputs[0], mesh_boolean_001.inputs[0])
	#switch_001.Output -> mesh_boolean_001.Mesh 2
	bgi_card_holder_horizontal.links.new(switch_001.outputs[0], mesh_boolean_001.inputs[1])
	#switch_1.Output -> mesh_boolean.Mesh 2
	bgi_card_holder_horizontal.links.new(switch_1.outputs[0], mesh_boolean.inputs[1])
	#group_input_008.Cut Side 1 -> switch_1.Switch
	bgi_card_holder_horizontal.links.new(group_input_008.outputs[5], switch_1.inputs[0])
	#realize_instances.Geometry -> switch_1.True
	bgi_card_holder_horizontal.links.new(realize_instances.outputs[0], switch_1.inputs[2])
	#group_input_009.Cut Side 2 -> switch_001.Switch
	bgi_card_holder_horizontal.links.new(group_input_009.outputs[6], switch_001.inputs[0])
	#realize_instances.Geometry -> switch_001.True
	bgi_card_holder_horizontal.links.new(realize_instances.outputs[0], switch_001.inputs[2])
	#math_021.Value -> math_020.Value
	bgi_card_holder_horizontal.links.new(math_021.outputs[0], math_020.inputs[0])
	#group_input_006.Inner Length -> math_020.Value
	bgi_card_holder_horizontal.links.new(group_input_006.outputs[1], math_020.inputs[1])
	#group_input_010.Cut Size Top -> math_027.Value
	bgi_card_holder_horizontal.links.new(group_input_010.outputs[7], math_027.inputs[0])
	#group_input_010.Cut Size Bottom -> math_027.Value
	bgi_card_holder_horizontal.links.new(group_input_010.outputs[8], math_027.inputs[1])
	#group_input_010.Inner Height -> combine_xyz_005.Z
	bgi_card_holder_horizontal.links.new(group_input_010.outputs[2], combine_xyz_005.inputs[2])
	#group_input_010.Cut Size Bottom -> combine_xyz_005.X
	bgi_card_holder_horizontal.links.new(group_input_010.outputs[8], combine_xyz_005.inputs[0])
	#reroute_011.Output -> reroute_010.Input
	bgi_card_holder_horizontal.links.new(reroute_011.outputs[0], reroute_010.inputs[0])
	#reroute_006.Output -> reroute_011.Input
	bgi_card_holder_horizontal.links.new(reroute_006.outputs[0], reroute_011.inputs[0])
	#group_input_011.Tickness -> reroute_001.Input
	bgi_card_holder_horizontal.links.new(group_input_011.outputs[3], reroute_001.inputs[0])
	#group_input_011.Inner Length -> math_003.Value
	bgi_card_holder_horizontal.links.new(group_input_011.outputs[1], math_003.inputs[1])
	#join_geometry.Geometry -> realize_instances_003.Geometry
	bgi_card_holder_horizontal.links.new(join_geometry.outputs[0], realize_instances_003.inputs[0])
	#realize_instances_003.Geometry -> group_output_1.Geometry
	bgi_card_holder_horizontal.links.new(realize_instances_003.outputs[0], group_output_1.inputs[0])
	#mesh_boolean_001.Mesh -> join_geometry.Geometry
	bgi_card_holder_horizontal.links.new(mesh_boolean_001.outputs[0], join_geometry.inputs[0])
	#instance_on_points.Instances -> join_geometry.Geometry
	bgi_card_holder_horizontal.links.new(instance_on_points.outputs[0], join_geometry.inputs[0])
	#transform_geometry.Geometry -> join_geometry.Geometry
	bgi_card_holder_horizontal.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
	return bgi_card_holder_horizontal

def bgi_card_holder_horizontal_create():
	bgi_divisor = bgi_divisor_create()

	return bgi_card_holder_horizontal_node_group(bgi_divisor)