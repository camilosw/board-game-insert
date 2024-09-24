import bpy

from .bgi_divisor import bgi_divisor_create
from .bgi_select_indexes import bgi_select_indexes_create

#initialize bgi_card_holder node group
def bgi_card_holder_node_group(bgi_divisor, bgi_select_indexes):
	bgi_card_holder = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Card Holder")

	bgi_card_holder.is_modifier = True
	
	#bgi_card_holder interface
	#Socket Geometry
	geometry_socket_1 = bgi_card_holder.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_1.attribute_domain = 'POINT'
	
	#Socket Inner Width
	inner_width_socket = bgi_card_holder.interface.new_socket(name = "Inner Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_width_socket.subtype = 'DISTANCE'
	inner_width_socket.default_value = 0.05000000074505806
	inner_width_socket.min_value = 0.0
	inner_width_socket.max_value = 3.4028234663852886e+38
	inner_width_socket.attribute_domain = 'POINT'
	
	#Socket Inner Length
	inner_length_socket = bgi_card_holder.interface.new_socket(name = "Inner Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_length_socket.subtype = 'DISTANCE'
	inner_length_socket.default_value = 0.07000000029802322
	inner_length_socket.min_value = 0.0
	inner_length_socket.max_value = 3.4028234663852886e+38
	inner_length_socket.attribute_domain = 'POINT'
	
	#Socket Inner Height
	inner_height_socket = bgi_card_holder.interface.new_socket(name = "Inner Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_height_socket.subtype = 'DISTANCE'
	inner_height_socket.default_value = 0.05000000074505806
	inner_height_socket.min_value = 0.0
	inner_height_socket.max_value = 3.4028234663852886e+38
	inner_height_socket.attribute_domain = 'POINT'
	
	#Socket Tickness
	tickness_socket = bgi_card_holder.interface.new_socket(name = "Tickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	tickness_socket.subtype = 'DISTANCE'
	tickness_socket.default_value = 0.005000000353902578
	tickness_socket.min_value = 0.0
	tickness_socket.max_value = 3.4028234663852886e+38
	tickness_socket.attribute_domain = 'POINT'
	
	#Socket Count
	count_socket = bgi_card_holder.interface.new_socket(name = "Count", in_out='INPUT', socket_type = 'NodeSocketInt')
	count_socket.subtype = 'NONE'
	count_socket.default_value = 3
	count_socket.min_value = 1
	count_socket.max_value = 2147483647
	count_socket.attribute_domain = 'POINT'
	
	#Socket Angle
	angle_socket = bgi_card_holder.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
	angle_socket.subtype = 'ANGLE'
	angle_socket.default_value = 0.523599
	angle_socket.min_value = 0.0
	angle_socket.max_value = 0.785398006439209
	angle_socket.attribute_domain = 'POINT'
	
	
	#initialize bgi_card_holder nodes
	#node Frame.001
	frame_001_1 = bgi_card_holder.nodes.new("NodeFrame")
	frame_001_1.label = "Divisions location"
	frame_001_1.name = "Frame.001"
	frame_001_1.label_size = 20
	frame_001_1.shrink = True
	
	#node Frame.002
	frame_002 = bgi_card_holder.nodes.new("NodeFrame")
	frame_002.label = "Containers division"
	frame_002.name = "Frame.002"
	frame_002.label_size = 20
	frame_002.shrink = True
	
	#node Frame
	frame_1 = bgi_card_holder.nodes.new("NodeFrame")
	frame_1.label = "Base"
	frame_1.name = "Frame"
	frame_1.label_size = 20
	frame_1.shrink = True
	
	#node Frame.010
	frame_010 = bgi_card_holder.nodes.new("NodeFrame")
	frame_010.label = "Move to the sides"
	frame_010.name = "Frame.010"
	frame_010.label_size = 20
	frame_010.shrink = True
	
	#node Math.017
	math_017 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_017.name = "Math.017"
	math_017.operation = 'MULTIPLY'
	math_017.use_clamp = False
	
	#node Math.018
	math_018 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_018.name = "Math.018"
	math_018.operation = 'MULTIPLY'
	math_018.use_clamp = False
	#Value_001
	math_018.inputs[1].default_value = -1.0
	
	#node Combine XYZ.003
	combine_xyz_003 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_003.name = "Combine XYZ.003"
	#Y
	combine_xyz_003.inputs[1].default_value = 0.0
	#Z
	combine_xyz_003.inputs[2].default_value = 0.0
	
	#node Group Input.003
	group_input_003_1 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_003_1.name = "Group Input.003"
	group_input_003_1.outputs[0].hide = True
	group_input_003_1.outputs[1].hide = True
	group_input_003_1.outputs[2].hide = True
	group_input_003_1.outputs[3].hide = True
	group_input_003_1.outputs[5].hide = True
	group_input_003_1.outputs[6].hide = True
	
	#node Mesh Line
	mesh_line = bgi_card_holder.nodes.new("GeometryNodeMeshLine")
	mesh_line.name = "Mesh Line"
	mesh_line.count_mode = 'TOTAL'
	mesh_line.mode = 'OFFSET'
	#Start Location
	mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Combine XYZ.002
	combine_xyz_002_1 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_002_1.name = "Combine XYZ.002"
	#Y
	combine_xyz_002_1.inputs[1].default_value = 0.0
	#Z
	combine_xyz_002_1.inputs[2].default_value = 0.0
	
	#node Math.014
	math_014 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_014.name = "Math.014"
	math_014.operation = 'ADD'
	math_014.use_clamp = False
	
	#node Transform Geometry.001
	transform_geometry_001 = bgi_card_holder.nodes.new("GeometryNodeTransform")
	transform_geometry_001.name = "Transform Geometry.001"
	#Rotation
	transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Group Input.001
	group_input_001_1 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_001_1.name = "Group Input.001"
	group_input_001_1.outputs[1].hide = True
	group_input_001_1.outputs[2].hide = True
	group_input_001_1.outputs[6].hide = True
	
	#node Math.007
	math_007 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_007.name = "Math.007"
	math_007.operation = 'DIVIDE'
	math_007.use_clamp = False
	#Value_001
	math_007.inputs[1].default_value = 2.0
	
	#node Math.008
	math_008 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_008.name = "Math.008"
	math_008.operation = 'ADD'
	math_008.use_clamp = False
	#Value_001
	math_008.inputs[1].default_value = 1.0
	
	#node Mesh to Points
	mesh_to_points = bgi_card_holder.nodes.new("GeometryNodeMeshToPoints")
	mesh_to_points.name = "Mesh to Points"
	mesh_to_points.mode = 'VERTICES'
	#Selection
	mesh_to_points.inputs[1].default_value = True
	#Position
	mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Radius
	mesh_to_points.inputs[3].default_value = 0.0020000000949949026
	
	#node Grid
	grid = bgi_card_holder.nodes.new("GeometryNodeMeshGrid")
	grid.name = "Grid"
	#Vertices X
	grid.inputs[2].default_value = 2
	#Vertices Y
	grid.inputs[3].default_value = 2
	
	#node Combine XYZ.008
	combine_xyz_008 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_008.name = "Combine XYZ.008"
	#X
	combine_xyz_008.inputs[0].default_value = 0.0
	#Y
	combine_xyz_008.inputs[1].default_value = 0.0
	
	#node Set Position.004
	set_position_004 = bgi_card_holder.nodes.new("GeometryNodeSetPosition")
	set_position_004.name = "Set Position.004"
	#Selection
	set_position_004.inputs[1].default_value = True
	#Position
	set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Math.038
	math_038 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_038.name = "Math.038"
	math_038.operation = 'MULTIPLY'
	math_038.use_clamp = False
	
	#node Math.037
	math_037 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_037.name = "Math.037"
	math_037.operation = 'ADD'
	math_037.use_clamp = False
	
	#node Math.036
	math_036 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_036.name = "Math.036"
	math_036.operation = 'MULTIPLY'
	math_036.use_clamp = False
	
	#node Math.039
	math_039 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_039.name = "Math.039"
	math_039.operation = 'ADD'
	math_039.use_clamp = False
	#Value_001
	math_039.inputs[1].default_value = 1.0
	
	#node Group Input.014
	group_input_014 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_014.name = "Group Input.014"
	group_input_014.outputs[0].hide = True
	group_input_014.outputs[1].hide = True
	group_input_014.outputs[2].hide = True
	group_input_014.outputs[4].hide = True
	group_input_014.outputs[5].hide = True
	group_input_014.outputs[6].hide = True
	
	#node Group Input.012
	group_input_012 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_012.name = "Group Input.012"
	group_input_012.outputs[1].hide = True
	group_input_012.outputs[2].hide = True
	group_input_012.outputs[5].hide = True
	group_input_012.outputs[6].hide = True
	
	#node Position
	position = bgi_card_holder.nodes.new("GeometryNodeInputPosition")
	position.name = "Position"
	
	#node Group
	group = bgi_card_holder.nodes.new("GeometryNodeGroup")
	group.name = "Group"
	group.node_tree = bgi_divisor
	#Input_3
	group.inputs[0].default_value = 0.0
	#Input_4
	group.inputs[4].default_value = False
	#Input_6
	group.inputs[5].default_value = False
	#Input_9
	group.inputs[6].default_value = 2
	
	#node Group Input.006
	group_input_006 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_006.name = "Group Input.006"
	group_input_006.outputs[0].hide = True
	group_input_006.outputs[1].hide = True
	group_input_006.outputs[2].hide = True
	group_input_006.outputs[3].hide = True
	group_input_006.outputs[4].hide = True
	group_input_006.outputs[6].hide = True
	
	#node Math.020
	math_020 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_020.name = "Math.020"
	math_020.operation = 'COSINE'
	math_020.use_clamp = False
	
	#node Math.019
	math_019 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_019.name = "Math.019"
	math_019.operation = 'DIVIDE'
	math_019.use_clamp = False
	
	#node Group Input.002
	group_input_002_1 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_002_1.name = "Group Input.002"
	group_input_002_1.outputs[0].hide = True
	group_input_002_1.outputs[4].hide = True
	group_input_002_1.outputs[6].hide = True
	
	#node Math.021
	math_021 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_021.name = "Math.021"
	math_021.operation = 'TANGENT'
	math_021.use_clamp = False
	
	#node Math.022
	math_022 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_022.name = "Math.022"
	math_022.operation = 'MULTIPLY'
	math_022.use_clamp = False
	
	#node Math.023
	math_023 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_023.name = "Math.023"
	math_023.operation = 'SUBTRACT'
	math_023.use_clamp = False
	
	#node Math.012
	math_012 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_012.name = "Math.012"
	math_012.operation = 'ADD'
	math_012.use_clamp = False
	#Value_001
	math_012.inputs[1].default_value = 1.0
	
	#node Index
	index = bgi_card_holder.nodes.new("GeometryNodeInputIndex")
	index.name = "Index"
	
	#node Set Position
	set_position = bgi_card_holder.nodes.new("GeometryNodeSetPosition")
	set_position.name = "Set Position"
	#Selection
	set_position.inputs[1].default_value = True
	#Offset
	set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
	
	#node Vector Rotate
	vector_rotate = bgi_card_holder.nodes.new("ShaderNodeVectorRotate")
	vector_rotate.name = "Vector Rotate"
	vector_rotate.invert = False
	vector_rotate.rotation_type = 'AXIS_ANGLE'
	#Center
	vector_rotate.inputs[1].default_value = (0.0024999999441206455, 0.0, 0.004999999888241291)
	#Axis
	vector_rotate.inputs[2].default_value = (0.0, 1.0, 0.0)
	
	#node Instance on Points
	instance_on_points = bgi_card_holder.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points.name = "Instance on Points"
	#Pick Instance
	instance_on_points.inputs[3].default_value = False
	#Instance Index
	instance_on_points.inputs[4].default_value = 0
	#Rotation
	instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
	#Scale
	instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.001
	combine_xyz_001 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_001.name = "Combine XYZ.001"
	#X
	combine_xyz_001.inputs[0].default_value = 0.0
	#Y
	combine_xyz_001.inputs[1].default_value = 0.0
	
	#node Combine XYZ
	combine_xyz_1 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_1.name = "Combine XYZ"
	
	#node Math
	math = bgi_card_holder.nodes.new("ShaderNodeMath")
	math.name = "Math"
	math.operation = 'DIVIDE'
	math.use_clamp = False
	#Value_001
	math.inputs[1].default_value = 2.0
	
	#node Math.003
	math_003 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_003.name = "Math.003"
	math_003.operation = 'ADD'
	math_003.use_clamp = False
	
	#node Math.004
	math_004_1 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_004_1.name = "Math.004"
	math_004_1.operation = 'MULTIPLY'
	math_004_1.use_clamp = False
	#Value_001
	math_004_1.inputs[1].default_value = 2.0
	
	#node Math.002
	math_002 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_002.name = "Math.002"
	math_002.operation = 'ADD'
	math_002.use_clamp = False
	
	#node Math.006
	math_006 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_006.name = "Math.006"
	math_006.operation = 'MULTIPLY'
	math_006.use_clamp = False
	
	#node Math.001
	math_001 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_001.name = "Math.001"
	math_001.operation = 'MULTIPLY'
	math_001.use_clamp = False
	
	#node Reroute.001
	reroute_001 = bgi_card_holder.nodes.new("NodeReroute")
	reroute_001.name = "Reroute.001"
	#node Cube
	cube = bgi_card_holder.nodes.new("GeometryNodeMeshCube")
	cube.name = "Cube"
	#Vertices X
	cube.inputs[1].default_value = 2
	#Vertices Y
	cube.inputs[2].default_value = 2
	#Vertices Z
	cube.inputs[3].default_value = 2
	
	#node Group Input.011
	group_input_011 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_011.name = "Group Input.011"
	group_input_011.outputs[0].hide = True
	group_input_011.outputs[2].hide = True
	group_input_011.outputs[4].hide = True
	group_input_011.outputs[6].hide = True
	
	#node Math.005
	math_005_1 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_005_1.name = "Math.005"
	math_005_1.operation = 'ADD'
	math_005_1.use_clamp = False
	#Value_001
	math_005_1.inputs[1].default_value = 1.0
	
	#node Group Input
	group_input_2 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_2.name = "Group Input"
	group_input_2.outputs[1].hide = True
	group_input_2.outputs[2].hide = True
	group_input_2.outputs[6].hide = True
	
	#node Transform Geometry
	transform_geometry = bgi_card_holder.nodes.new("GeometryNodeTransform")
	transform_geometry.name = "Transform Geometry"
	#Rotation
	transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.009
	combine_xyz_009 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_009.name = "Combine XYZ.009"
	#Y
	combine_xyz_009.inputs[1].default_value = 0.0
	#Z
	combine_xyz_009.inputs[2].default_value = 0.0
	
	#node Math.042
	math_042 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_042.name = "Math.042"
	math_042.operation = 'TANGENT'
	math_042.use_clamp = False
	
	#node Math.043
	math_043 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_043.name = "Math.043"
	math_043.operation = 'MULTIPLY'
	math_043.use_clamp = False
	
	#node Extrude Mesh
	extrude_mesh = bgi_card_holder.nodes.new("GeometryNodeExtrudeMesh")
	extrude_mesh.name = "Extrude Mesh"
	extrude_mesh.mode = 'FACES'
	#Selection
	extrude_mesh.inputs[1].default_value = True
	#Offset
	extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Individual
	extrude_mesh.inputs[4].default_value = True
	
	#node Set Position.005
	set_position_005 = bgi_card_holder.nodes.new("GeometryNodeSetPosition")
	set_position_005.name = "Set Position.005"
	#Position
	set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Math.045
	math_045 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_045.name = "Math.045"
	math_045.operation = 'MULTIPLY'
	math_045.use_clamp = False
	#Value_001
	math_045.inputs[1].default_value = 2.0
	
	#node Group Input.013
	group_input_013 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_013.name = "Group Input.013"
	group_input_013.outputs[0].hide = True
	group_input_013.outputs[1].hide = True
	group_input_013.outputs[2].hide = True
	group_input_013.outputs[4].hide = True
	group_input_013.outputs[5].hide = True
	group_input_013.outputs[6].hide = True
	
	#node Math.040
	math_040 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_040.name = "Math.040"
	math_040.operation = 'SINE'
	math_040.use_clamp = False
	
	#node Math.041
	math_041 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_041.name = "Math.041"
	math_041.operation = 'MULTIPLY'
	math_041.use_clamp = False
	
	#node Group Input.015
	group_input_015 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_015.name = "Group Input.015"
	group_input_015.outputs[0].hide = True
	group_input_015.outputs[1].hide = True
	group_input_015.outputs[2].hide = True
	group_input_015.outputs[3].hide = True
	group_input_015.outputs[4].hide = True
	group_input_015.outputs[6].hide = True
	
	#node Math.044
	math_044 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_044.name = "Math.044"
	math_044.operation = 'SUBTRACT'
	math_044.use_clamp = False
	
	#node Extrude Mesh.001
	extrude_mesh_001 = bgi_card_holder.nodes.new("GeometryNodeExtrudeMesh")
	extrude_mesh_001.name = "Extrude Mesh.001"
	extrude_mesh_001.mode = 'FACES'
	#Offset
	extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Individual
	extrude_mesh_001.inputs[4].default_value = True
	
	#node Group Input.017
	group_input_017 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_017.name = "Group Input.017"
	group_input_017.outputs[0].hide = True
	group_input_017.outputs[1].hide = True
	group_input_017.outputs[3].hide = True
	group_input_017.outputs[4].hide = True
	group_input_017.outputs[6].hide = True
	
	#node Math.046
	math_046 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_046.name = "Math.046"
	math_046.operation = 'TANGENT'
	math_046.use_clamp = False
	
	#node Math.047
	math_047 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_047.name = "Math.047"
	math_047.operation = 'MULTIPLY'
	math_047.use_clamp = False
	
	#node Extrude Mesh.002
	extrude_mesh_002 = bgi_card_holder.nodes.new("GeometryNodeExtrudeMesh")
	extrude_mesh_002.name = "Extrude Mesh.002"
	extrude_mesh_002.mode = 'FACES'
	#Offset
	extrude_mesh_002.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Individual
	extrude_mesh_002.inputs[4].default_value = True
	
	#node Set Position.006
	set_position_006 = bgi_card_holder.nodes.new("GeometryNodeSetPosition")
	set_position_006.name = "Set Position.006"
	#Position
	set_position_006.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Select indexes
	select_indexes_1 = bgi_card_holder.nodes.new("GeometryNodeGroup")
	select_indexes_1.name = "Select indexes"
	select_indexes_1.node_tree = bgi_select_indexes
	#Input_2
	select_indexes_1.inputs[0].default_value = 5
	#Input_3
	select_indexes_1.inputs[1].default_value = 6
	
	#node Select indexes.002
	select_indexes_002 = bgi_card_holder.nodes.new("GeometryNodeGroup")
	select_indexes_002.name = "Select indexes.002"
	select_indexes_002.node_tree = bgi_select_indexes
	#Input_2
	select_indexes_002.inputs[0].default_value = 15
	#Input_3
	select_indexes_002.inputs[1].default_value = 15
	
	#node Select indexes.001
	select_indexes_001 = bgi_card_holder.nodes.new("GeometryNodeGroup")
	select_indexes_001.name = "Select indexes.001"
	select_indexes_001.node_tree = bgi_select_indexes
	#Input_2
	select_indexes_001.inputs[0].default_value = 12
	#Input_3
	select_indexes_001.inputs[1].default_value = 12
	
	#node Boolean Math.002
	boolean_math_002_1 = bgi_card_holder.nodes.new("FunctionNodeBooleanMath")
	boolean_math_002_1.name = "Boolean Math.002"
	boolean_math_002_1.operation = 'OR'
	
	#node Transform Geometry.005
	transform_geometry_005 = bgi_card_holder.nodes.new("GeometryNodeTransform")
	transform_geometry_005.name = "Transform Geometry.005"
	#Rotation
	transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Reroute.002
	reroute_002 = bgi_card_holder.nodes.new("NodeReroute")
	reroute_002.name = "Reroute.002"
	#node Math.048
	math_048 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_048.name = "Math.048"
	math_048.operation = 'DIVIDE'
	math_048.use_clamp = False
	#Value_001
	math_048.inputs[1].default_value = 2.0
	
	#node Math.049
	math_049 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_049.name = "Math.049"
	math_049.operation = 'DIVIDE'
	math_049.use_clamp = False
	#Value_001
	math_049.inputs[1].default_value = 2.0
	
	#node Combine XYZ.011
	combine_xyz_011 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_011.name = "Combine XYZ.011"
	#X
	combine_xyz_011.inputs[0].default_value = 0.0
	#Z
	combine_xyz_011.inputs[2].default_value = 0.0
	
	#node Math.050
	math_050 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_050.name = "Math.050"
	math_050.operation = 'ADD'
	math_050.use_clamp = False
	
	#node Group Input.018
	group_input_018 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_018.name = "Group Input.018"
	group_input_018.outputs[0].hide = True
	group_input_018.outputs[2].hide = True
	group_input_018.outputs[4].hide = True
	group_input_018.outputs[6].hide = True
	
	#node Vector Math.001
	vector_math_001 = bgi_card_holder.nodes.new("ShaderNodeVectorMath")
	vector_math_001.name = "Vector Math.001"
	vector_math_001.operation = 'MULTIPLY'
	#Vector_001
	vector_math_001.inputs[1].default_value = (1.0, -1.0, 1.0)
	
	#node Transform Geometry.004
	transform_geometry_004 = bgi_card_holder.nodes.new("GeometryNodeTransform")
	transform_geometry_004.name = "Transform Geometry.004"
	#Rotation
	transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.010
	combine_xyz_010 = bgi_card_holder.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_010.name = "Combine XYZ.010"
	#Y
	combine_xyz_010.inputs[1].default_value = 0.0
	#Z
	combine_xyz_010.inputs[2].default_value = 0.0
	
	#node Set Position.007
	set_position_007 = bgi_card_holder.nodes.new("GeometryNodeSetPosition")
	set_position_007.name = "Set Position.007"
	#Position
	set_position_007.inputs[2].default_value = (0.0, 0.0, 0.0)
	
	#node Group Output
	group_output_1 = bgi_card_holder.nodes.new("NodeGroupOutput")
	group_output_1.name = "Group Output"
	group_output_1.is_active_output = True
	
	#node Join Geometry
	join_geometry = bgi_card_holder.nodes.new("GeometryNodeJoinGeometry")
	join_geometry.name = "Join Geometry"
	
	#node Realize Instances
	realize_instances = bgi_card_holder.nodes.new("GeometryNodeRealizeInstances")
	realize_instances.name = "Realize Instances"
	
	#node Reroute.003
	reroute_003 = bgi_card_holder.nodes.new("NodeReroute")
	reroute_003.name = "Reroute.003"
	#node Frame.009
	frame_009 = bgi_card_holder.nodes.new("NodeFrame")
	frame_009.label = "Side element"
	frame_009.name = "Frame.009"
	frame_009.label_size = 20
	frame_009.shrink = True
	
	#node Math.009
	math_009_1 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_009_1.name = "Math.009"
	math_009_1.operation = 'COSINE'
	math_009_1.use_clamp = False
	
	#node Math.010
	math_010_1 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_010_1.name = "Math.010"
	math_010_1.operation = 'MULTIPLY'
	math_010_1.use_clamp = False
	
	#node Math.015
	math_015 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_015.name = "Math.015"
	math_015.operation = 'ADD'
	math_015.use_clamp = False
	
	#node Math.011
	math_011 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_011.name = "Math.011"
	math_011.operation = 'SUBTRACT'
	math_011.use_clamp = False
	
	#node Math.013
	math_013 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_013.name = "Math.013"
	math_013.operation = 'DIVIDE'
	math_013.use_clamp = False
	
	#node Group Input.004
	group_input_004_1 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_004_1.name = "Group Input.004"
	group_input_004_1.outputs[0].hide = True
	group_input_004_1.outputs[1].hide = True
	group_input_004_1.outputs[2].hide = True
	group_input_004_1.outputs[3].hide = True
	group_input_004_1.outputs[5].hide = True
	group_input_004_1.outputs[6].hide = True
	
	#node Group Input.005
	group_input_005 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_005.name = "Group Input.005"
	group_input_005.outputs[1].hide = True
	group_input_005.outputs[2].hide = True
	group_input_005.outputs[4].hide = True
	group_input_005.outputs[5].hide = True
	group_input_005.outputs[6].hide = True
	
	#node Group Input.007
	group_input_007 = bgi_card_holder.nodes.new("NodeGroupInput")
	group_input_007.name = "Group Input.007"
	group_input_007.outputs[0].hide = True
	group_input_007.outputs[1].hide = True
	group_input_007.outputs[2].hide = True
	group_input_007.outputs[3].hide = True
	group_input_007.outputs[5].hide = True
	group_input_007.outputs[6].hide = True
	
	#node Math.016
	math_016 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_016.name = "Math.016"
	math_016.operation = 'MULTIPLY'
	math_016.use_clamp = False
	#Value_001
	math_016.inputs[1].default_value = 2.0
	
	#node Math.024
	math_024 = bgi_card_holder.nodes.new("ShaderNodeMath")
	math_024.name = "Math.024"
	math_024.operation = 'SUBTRACT'
	math_024.use_clamp = False
	
	#node Reroute
	reroute_1 = bgi_card_holder.nodes.new("NodeReroute")
	reroute_1.name = "Reroute"
	
	
	#Set parents
	math_017.parent = frame_001_1
	math_018.parent = frame_001_1
	combine_xyz_003.parent = frame_001_1
	group_input_003_1.parent = frame_001_1
	mesh_line.parent = frame_001_1
	combine_xyz_002_1.parent = frame_001_1
	math_014.parent = frame_001_1
	transform_geometry_001.parent = frame_001_1
	group_input_001_1.parent = frame_001_1
	math_007.parent = frame_001_1
	math_008.parent = frame_001_1
	mesh_to_points.parent = frame_001_1
	grid.parent = frame_009
	combine_xyz_008.parent = frame_009
	set_position_004.parent = frame_009
	math_038.parent = frame_009
	math_037.parent = frame_009
	math_036.parent = frame_009
	math_039.parent = frame_009
	group_input_014.parent = frame_009
	group_input_012.parent = frame_009
	position.parent = frame_002
	group.parent = frame_002
	group_input_006.parent = frame_002
	math_020.parent = frame_002
	math_019.parent = frame_002
	group_input_002_1.parent = frame_002
	math_021.parent = frame_002
	math_022.parent = frame_002
	math_023.parent = frame_002
	math_012.parent = frame_002
	index.parent = frame_002
	set_position.parent = frame_002
	vector_rotate.parent = frame_002
	instance_on_points.parent = frame_002
	combine_xyz_001.parent = frame_1
	combine_xyz_1.parent = frame_1
	math.parent = frame_1
	math_003.parent = frame_1
	math_004_1.parent = frame_1
	math_002.parent = frame_1
	math_006.parent = frame_1
	math_001.parent = frame_1
	reroute_001.parent = frame_1
	cube.parent = frame_1
	group_input_011.parent = frame_1
	math_005_1.parent = frame_1
	group_input_2.parent = frame_1
	transform_geometry.parent = frame_1
	combine_xyz_009.parent = frame_009
	math_042.parent = frame_009
	math_043.parent = frame_009
	extrude_mesh.parent = frame_009
	set_position_005.parent = frame_009
	math_045.parent = frame_009
	group_input_013.parent = frame_009
	math_040.parent = frame_009
	math_041.parent = frame_009
	group_input_015.parent = frame_009
	math_044.parent = frame_009
	extrude_mesh_001.parent = frame_009
	group_input_017.parent = frame_009
	math_046.parent = frame_009
	math_047.parent = frame_009
	extrude_mesh_002.parent = frame_009
	set_position_006.parent = frame_009
	select_indexes_1.parent = frame_009
	select_indexes_002.parent = frame_009
	select_indexes_001.parent = frame_009
	boolean_math_002_1.parent = frame_009
	transform_geometry_005.parent = frame_010
	reroute_002.parent = frame_010
	math_048.parent = frame_010
	math_049.parent = frame_010
	combine_xyz_011.parent = frame_010
	math_050.parent = frame_010
	group_input_018.parent = frame_010
	vector_math_001.parent = frame_010
	transform_geometry_004.parent = frame_010
	combine_xyz_010.parent = frame_009
	set_position_007.parent = frame_009
	reroute_003.parent = frame_009
	math_009_1.parent = frame_001_1
	math_010_1.parent = frame_001_1
	math_015.parent = frame_001_1
	math_011.parent = frame_001_1
	math_013.parent = frame_001_1
	group_input_004_1.parent = frame_001_1
	group_input_005.parent = frame_001_1
	group_input_007.parent = frame_001_1
	math_016.parent = frame_001_1
	math_024.parent = frame_001_1
	reroute_1.parent = frame_001_1
	
	#Set locations
	frame_001_1.location = (1930.0, 100.0)
	frame_002.location = (3027.0, 324.0)
	frame_1.location = (1962.0, 416.0)
	frame_010.location = (1496.83984375, 834.8624877929688)
	math_017.location = (-2550.0, -280.0)
	math_018.location = (-2370.0, -280.0)
	combine_xyz_003.location = (-2010.0, -280.0)
	group_input_003_1.location = (-2750.0, -380.0)
	mesh_line.location = (-2190.0, 0.0)
	combine_xyz_002_1.location = (-2550.0, -140.0)
	math_014.location = (-3110.0, -120.0)
	transform_geometry_001.location = (-1810.0, -100.0)
	group_input_001_1.location = (-3970.0, -300.0)
	math_007.location = (-2750.0, -220.0)
	math_008.location = (-2370.0, 20.0)
	mesh_to_points.location = (-1630.0, -180.0)
	grid.location = (-1060.0, -840.0)
	combine_xyz_008.location = (-840.0, -920.0)
	set_position_004.location = (-560.0, -820.0)
	math_038.location = (-1480.0, -820.0)
	math_037.location = (-1260.0, -820.0)
	math_036.location = (-1480.0, -980.0)
	math_039.location = (-1660.0, -1100.0)
	group_input_014.location = (-1260.0, -1000.0)
	group_input_012.location = (-1860.0, -920.0)
	position.location = (-1577.003173828125, -833.8056640625)
	group.location = (-1573.438232421875, -581.5791015625)
	group_input_006.location = (-2446.033935546875, -991.0418090820312)
	math_020.location = (-2260.5576171875, -864.9547729492188)
	math_019.location = (-2055.9970703125, -762.6195068359375)
	group_input_002_1.location = (-2477.653076171875, -648.55810546875)
	math_021.location = (-2263.390869140625, -469.70361328125)
	math_022.location = (-2086.294189453125, -488.6546630859375)
	math_023.location = (-1831.8023681640625, -507.83599853515625)
	math_012.location = (-1207.8590087890625, -468.23516845703125)
	index.location = (-1402.9014892578125, -545.8402709960938)
	set_position.location = (-1203.3345947265625, -632.7984619140625)
	vector_rotate.location = (-1380.6348876953125, -742.5078125)
	instance_on_points.location = (-999.4872436523438, -383.5027770996094)
	combine_xyz_001.location = (-149.05105590820312, -226.1741943359375)
	combine_xyz_1.location = (-325.9454040527344, -50.780948638916016)
	math.location = (-329.0421447753906, -197.6778106689453)
	math_003.location = (-568.05908203125, -136.11904907226562)
	math_004_1.location = (-769.612548828125, -124.79510498046875)
	math_002.location = (-553.548095703125, 53.7738037109375)
	math_006.location = (-763.4810791015625, 40.877532958984375)
	math_001.location = (-759.9774169921875, 204.79714965820312)
	reroute_001.location = (-382.6703796386719, -308.0303955078125)
	cube.location = (-146.71456909179688, -45.32170486450195)
	group_input_011.location = (-766.5849609375, -292.05438232421875)
	math_005_1.location = (-977.35986328125, 200.3018798828125)
	group_input_2.location = (-1192.7413330078125, -27.695465087890625)
	transform_geometry.location = (70.38475799560547, -40.947845458984375)
	combine_xyz_009.location = (-240.0, -1160.0)
	math_042.location = (-860.0, -1320.0)
	math_043.location = (-620.0, -1180.0)
	extrude_mesh.location = (-360.0, -820.0)
	set_position_005.location = (100.0, -820.0)
	math_045.location = (-440.0, -1240.0)
	group_input_013.location = (-1080.0, -1160.0)
	math_040.location = (-1080.0, -1240.0)
	math_041.location = (-860.0, -1120.0)
	group_input_015.location = (-1280.0, -1380.0)
	math_044.location = (-60.0, -1240.0)
	extrude_mesh_001.location = (300.0, -820.0)
	group_input_017.location = (-240.0, -1380.0)
	math_046.location = (-60.0, -1400.0)
	math_047.location = (120.0, -1260.0)
	extrude_mesh_002.location = (680.0, -860.0)
	set_position_006.location = (500.0, -840.0)
	select_indexes_1.location = (-160.0, -920.0)
	select_indexes_002.location = (480.0, -1380.0)
	select_indexes_001.location = (480.0, -1240.0)
	boolean_math_002_1.location = (680.0, -1200.0)
	transform_geometry_005.location = (531.7548828125, -1937.054931640625)
	reroute_002.location = (364.801025390625, -1851.8154296875)
	math_048.location = (-182.791748046875, -1926.697998046875)
	math_049.location = (-180.6600341796875, -2103.59423828125)
	combine_xyz_011.location = (176.31884765625, -1966.407470703125)
	math_050.location = (-1.3826904296875, -1986.879638671875)
	group_input_018.location = (-379.4031982421875, -2067.2734375)
	vector_math_001.location = (361.861328125, -2006.668701171875)
	transform_geometry_004.location = (530.9212646484375, -1671.7396240234375)
	combine_xyz_010.location = (280.0, -1240.0)
	set_position_007.location = (860.0, -980.0)
	group_output_1.location = (2919.333251953125, -212.6666717529297)
	join_geometry.location = (2532.666748046875, -212.6666717529297)
	realize_instances.location = (2726.0, -212.6666717529297)
	reroute_003.location = (-660.0, -1340.0)
	frame_009.location = (9.0, -19.0)
	math_009_1.location = (-3770.0, -460.0)
	math_010_1.location = (-3470.0, -420.0)
	math_015.location = (-2910.0, -160.0)
	math_011.location = (-3310.0, -280.0)
	math_013.location = (-3110.0, -280.0)
	group_input_004_1.location = (-3310.0, -440.0)
	group_input_005.location = (-3310.0, -180.0)
	group_input_007.location = (-2550.0, -40.0)
	math_016.location = (-2370.0, -460.0)
	math_024.location = (-2190.0, -280.0)
	reroute_1.location = (-2850.0, -560.0)
	
	#Set dimensions
	frame_001_1.width, frame_001_1.height = 2538.0, 689.8333129882812
	frame_002.width, frame_002.height = 1676.0, 726.4998779296875
	frame_1.width, frame_1.height = 1461.33349609375, 657.8333740234375
	frame_010.width, frame_010.height = 1109.3333740234375, 641.8333740234375
	math_017.width, math_017.height = 140.0, 100.0
	math_018.width, math_018.height = 140.0, 100.0
	combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
	group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
	mesh_line.width, mesh_line.height = 140.0, 100.0
	combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
	math_014.width, math_014.height = 140.0, 100.0
	transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
	group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
	math_007.width, math_007.height = 140.0, 100.0
	math_008.width, math_008.height = 140.0, 100.0
	mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
	grid.width, grid.height = 140.0, 100.0
	combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
	set_position_004.width, set_position_004.height = 140.0, 100.0
	math_038.width, math_038.height = 140.0, 100.0
	math_037.width, math_037.height = 140.0, 100.0
	math_036.width, math_036.height = 140.0, 100.0
	math_039.width, math_039.height = 140.0, 100.0
	group_input_014.width, group_input_014.height = 140.0, 100.0
	group_input_012.width, group_input_012.height = 140.0, 100.0
	position.width, position.height = 140.0, 100.0
	group.width, group.height = 140.0, 100.0
	group_input_006.width, group_input_006.height = 140.0, 100.0
	math_020.width, math_020.height = 140.0, 100.0
	math_019.width, math_019.height = 140.0, 100.0
	group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
	math_021.width, math_021.height = 140.0, 100.0
	math_022.width, math_022.height = 140.0, 100.0
	math_023.width, math_023.height = 140.0, 100.0
	math_012.width, math_012.height = 140.0, 100.0
	index.width, index.height = 140.0, 100.0
	set_position.width, set_position.height = 140.0, 100.0
	vector_rotate.width, vector_rotate.height = 140.0, 100.0
	instance_on_points.width, instance_on_points.height = 140.0, 100.0
	combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
	combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
	math.width, math.height = 140.0, 100.0
	math_003.width, math_003.height = 140.0, 100.0
	math_004_1.width, math_004_1.height = 140.0, 100.0
	math_002.width, math_002.height = 140.0, 100.0
	math_006.width, math_006.height = 140.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	reroute_001.width, reroute_001.height = 16.0, 100.0
	cube.width, cube.height = 140.0, 100.0
	group_input_011.width, group_input_011.height = 140.0, 100.0
	math_005_1.width, math_005_1.height = 140.0, 100.0
	group_input_2.width, group_input_2.height = 140.0, 100.0
	transform_geometry.width, transform_geometry.height = 140.0, 100.0
	combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
	math_042.width, math_042.height = 140.0, 100.0
	math_043.width, math_043.height = 140.0, 100.0
	extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
	set_position_005.width, set_position_005.height = 140.0, 100.0
	math_045.width, math_045.height = 140.0, 100.0
	group_input_013.width, group_input_013.height = 140.0, 100.0
	math_040.width, math_040.height = 140.0, 100.0
	math_041.width, math_041.height = 140.0, 100.0
	group_input_015.width, group_input_015.height = 140.0, 100.0
	math_044.width, math_044.height = 140.0, 100.0
	extrude_mesh_001.width, extrude_mesh_001.height = 140.0, 100.0
	group_input_017.width, group_input_017.height = 140.0, 100.0
	math_046.width, math_046.height = 140.0, 100.0
	math_047.width, math_047.height = 140.0, 100.0
	extrude_mesh_002.width, extrude_mesh_002.height = 140.0, 100.0
	set_position_006.width, set_position_006.height = 140.0, 100.0
	select_indexes_1.width, select_indexes_1.height = 140.0, 100.0
	select_indexes_002.width, select_indexes_002.height = 140.0, 100.0
	select_indexes_001.width, select_indexes_001.height = 140.0, 100.0
	boolean_math_002_1.width, boolean_math_002_1.height = 140.0, 100.0
	transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
	reroute_002.width, reroute_002.height = 16.0, 100.0
	math_048.width, math_048.height = 140.0, 100.0
	math_049.width, math_049.height = 140.0, 100.0
	combine_xyz_011.width, combine_xyz_011.height = 140.0, 100.0
	math_050.width, math_050.height = 140.0, 100.0
	group_input_018.width, group_input_018.height = 140.0, 100.0
	vector_math_001.width, vector_math_001.height = 140.0, 100.0
	transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
	combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
	set_position_007.width, set_position_007.height = 140.0, 100.0
	group_output_1.width, group_output_1.height = 140.0, 100.0
	join_geometry.width, join_geometry.height = 140.0, 100.0
	realize_instances.width, realize_instances.height = 140.0, 100.0
	reroute_003.width, reroute_003.height = 16.0, 100.0
	frame_009.width, frame_009.height = 2918.666748046875, 769.1666870117188
	math_009_1.width, math_009_1.height = 140.0, 100.0
	math_010_1.width, math_010_1.height = 140.0, 100.0
	math_015.width, math_015.height = 140.0, 100.0
	math_011.width, math_011.height = 140.0, 100.0
	math_013.width, math_013.height = 140.0, 100.0
	group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
	group_input_005.width, group_input_005.height = 140.0, 100.0
	group_input_007.width, group_input_007.height = 140.0, 100.0
	math_016.width, math_016.height = 140.0, 100.0
	math_024.width, math_024.height = 140.0, 100.0
	reroute_1.width, reroute_1.height = 16.0, 100.0
	
	#initialize bgi_card_holder links
	#combine_xyz_1.Vector -> cube.Size
	bgi_card_holder.links.new(combine_xyz_1.outputs[0], cube.inputs[0])
	#cube.Mesh -> transform_geometry.Geometry
	bgi_card_holder.links.new(cube.outputs[0], transform_geometry.inputs[0])
	#reroute_001.Output -> math.Value
	bgi_card_holder.links.new(reroute_001.outputs[0], math.inputs[0])
	#combine_xyz_001.Vector -> transform_geometry.Translation
	bgi_card_holder.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
	#math.Value -> combine_xyz_001.Z
	bgi_card_holder.links.new(math.outputs[0], combine_xyz_001.inputs[2])
	#math_001.Value -> math_002.Value
	bgi_card_holder.links.new(math_001.outputs[0], math_002.inputs[0])
	#math_002.Value -> combine_xyz_1.X
	bgi_card_holder.links.new(math_002.outputs[0], combine_xyz_1.inputs[0])
	#math_003.Value -> combine_xyz_1.Y
	bgi_card_holder.links.new(math_003.outputs[0], combine_xyz_1.inputs[1])
	#reroute_001.Output -> combine_xyz_1.Z
	bgi_card_holder.links.new(reroute_001.outputs[0], combine_xyz_1.inputs[2])
	#math_006.Value -> math_002.Value
	bgi_card_holder.links.new(math_006.outputs[0], math_002.inputs[1])
	#math_004_1.Value -> math_003.Value
	bgi_card_holder.links.new(math_004_1.outputs[0], math_003.inputs[0])
	#group_input_2.Count -> math_005_1.Value
	bgi_card_holder.links.new(group_input_2.outputs[4], math_005_1.inputs[0])
	#group_input_2.Inner Width -> math_006.Value
	bgi_card_holder.links.new(group_input_2.outputs[0], math_006.inputs[0])
	#group_input_2.Count -> math_006.Value
	bgi_card_holder.links.new(group_input_2.outputs[4], math_006.inputs[1])
	#group_input_2.Tickness -> math_004_1.Value
	bgi_card_holder.links.new(group_input_2.outputs[3], math_004_1.inputs[0])
	#group_input_2.Tickness -> math_001.Value
	bgi_card_holder.links.new(group_input_2.outputs[3], math_001.inputs[1])
	#math_005_1.Value -> math_001.Value
	bgi_card_holder.links.new(math_005_1.outputs[0], math_001.inputs[0])
	#combine_xyz_002_1.Vector -> mesh_line.Offset
	bgi_card_holder.links.new(combine_xyz_002_1.outputs[0], mesh_line.inputs[3])
	#math_008.Value -> mesh_line.Count
	bgi_card_holder.links.new(math_008.outputs[0], mesh_line.inputs[0])
	#mesh_line.Mesh -> transform_geometry_001.Geometry
	bgi_card_holder.links.new(mesh_line.outputs[0], transform_geometry_001.inputs[0])
	#combine_xyz_003.Vector -> transform_geometry_001.Translation
	bgi_card_holder.links.new(combine_xyz_003.outputs[0], transform_geometry_001.inputs[1])
	#group_input_002_1.Tickness -> group.Thickness
	bgi_card_holder.links.new(group_input_002_1.outputs[3], group.inputs[3])
	#group_input_002_1.Inner Length -> group.Length
	bgi_card_holder.links.new(group_input_002_1.outputs[1], group.inputs[1])
	#transform_geometry_001.Geometry -> mesh_to_points.Mesh
	bgi_card_holder.links.new(transform_geometry_001.outputs[0], mesh_to_points.inputs[0])
	#mesh_to_points.Points -> instance_on_points.Points
	bgi_card_holder.links.new(mesh_to_points.outputs[0], instance_on_points.inputs[0])
	#set_position.Geometry -> instance_on_points.Instance
	bgi_card_holder.links.new(set_position.outputs[0], instance_on_points.inputs[2])
	#math_012.Value -> instance_on_points.Selection
	bgi_card_holder.links.new(math_012.outputs[0], instance_on_points.inputs[1])
	#index.Index -> math_012.Value
	bgi_card_holder.links.new(index.outputs[0], math_012.inputs[0])
	#math_007.Value -> math_017.Value
	bgi_card_holder.links.new(math_007.outputs[0], math_017.inputs[0])
	#math_017.Value -> math_018.Value
	bgi_card_holder.links.new(math_017.outputs[0], math_018.inputs[0])
	#group_input_003_1.Count -> math_017.Value
	bgi_card_holder.links.new(group_input_003_1.outputs[4], math_017.inputs[1])
	#group_input_011.Tickness -> reroute_001.Input
	bgi_card_holder.links.new(group_input_011.outputs[3], reroute_001.inputs[0])
	#group_input_011.Inner Length -> math_003.Value
	bgi_card_holder.links.new(group_input_011.outputs[1], math_003.inputs[1])
	#math_015.Value -> combine_xyz_002_1.X
	bgi_card_holder.links.new(math_015.outputs[0], combine_xyz_002_1.inputs[0])
	#group.Geometry -> set_position.Geometry
	bgi_card_holder.links.new(group.outputs[0], set_position.inputs[0])
	#vector_rotate.Vector -> set_position.Position
	bgi_card_holder.links.new(vector_rotate.outputs[0], set_position.inputs[2])
	#position.Position -> vector_rotate.Vector
	bgi_card_holder.links.new(position.outputs[0], vector_rotate.inputs[0])
	#group_input_006.Angle -> vector_rotate.Angle
	bgi_card_holder.links.new(group_input_006.outputs[5], vector_rotate.inputs[3])
	#group_input_002_1.Inner Height -> math_019.Value
	bgi_card_holder.links.new(group_input_002_1.outputs[2], math_019.inputs[0])
	#group_input_006.Angle -> math_020.Value
	bgi_card_holder.links.new(group_input_006.outputs[5], math_020.inputs[0])
	#math_020.Value -> math_019.Value
	bgi_card_holder.links.new(math_020.outputs[0], math_019.inputs[1])
	#group_input_002_1.Angle -> math_021.Value
	bgi_card_holder.links.new(group_input_002_1.outputs[5], math_021.inputs[0])
	#math_021.Value -> math_022.Value
	bgi_card_holder.links.new(math_021.outputs[0], math_022.inputs[0])
	#group_input_002_1.Tickness -> math_022.Value
	bgi_card_holder.links.new(group_input_002_1.outputs[3], math_022.inputs[1])
	#math_019.Value -> math_023.Value
	bgi_card_holder.links.new(math_019.outputs[0], math_023.inputs[0])
	#math_022.Value -> math_023.Value
	bgi_card_holder.links.new(math_022.outputs[0], math_023.inputs[1])
	#math_023.Value -> group.Height
	bgi_card_holder.links.new(math_023.outputs[0], group.inputs[2])
	#set_position_005.Geometry -> extrude_mesh_001.Mesh
	bgi_card_holder.links.new(set_position_005.outputs[0], extrude_mesh_001.inputs[0])
	#group_input_012.Tickness -> math_036.Value
	bgi_card_holder.links.new(group_input_012.outputs[3], math_036.inputs[0])
	#math_038.Value -> math_037.Value
	bgi_card_holder.links.new(math_038.outputs[0], math_037.inputs[0])
	#math_036.Value -> math_037.Value
	bgi_card_holder.links.new(math_036.outputs[0], math_037.inputs[1])
	#group_input_012.Inner Width -> math_038.Value
	bgi_card_holder.links.new(group_input_012.outputs[0], math_038.inputs[0])
	#group_input_012.Count -> math_038.Value
	bgi_card_holder.links.new(group_input_012.outputs[4], math_038.inputs[1])
	#math_037.Value -> grid.Size X
	bgi_card_holder.links.new(math_037.outputs[0], grid.inputs[0])
	#math_039.Value -> math_036.Value
	bgi_card_holder.links.new(math_039.outputs[0], math_036.inputs[1])
	#group_input_012.Count -> math_039.Value
	bgi_card_holder.links.new(group_input_012.outputs[4], math_039.inputs[0])
	#grid.Mesh -> set_position_004.Geometry
	bgi_card_holder.links.new(grid.outputs[0], set_position_004.inputs[0])
	#combine_xyz_008.Vector -> set_position_004.Offset
	bgi_card_holder.links.new(combine_xyz_008.outputs[0], set_position_004.inputs[3])
	#set_position_004.Geometry -> extrude_mesh.Mesh
	bgi_card_holder.links.new(set_position_004.outputs[0], extrude_mesh.inputs[0])
	#group_input_013.Tickness -> math_041.Value
	bgi_card_holder.links.new(group_input_013.outputs[3], math_041.inputs[0])
	#math_040.Value -> math_041.Value
	bgi_card_holder.links.new(math_040.outputs[0], math_041.inputs[1])
	#math_041.Value -> extrude_mesh.Offset Scale
	bgi_card_holder.links.new(math_041.outputs[0], extrude_mesh.inputs[3])
	#group_input_014.Tickness -> grid.Size Y
	bgi_card_holder.links.new(group_input_014.outputs[3], grid.inputs[1])
	#group_input_014.Tickness -> combine_xyz_008.Z
	bgi_card_holder.links.new(group_input_014.outputs[3], combine_xyz_008.inputs[2])
	#extrude_mesh.Mesh -> set_position_005.Geometry
	bgi_card_holder.links.new(extrude_mesh.outputs[0], set_position_005.inputs[0])
	#combine_xyz_009.Vector -> set_position_005.Offset
	bgi_card_holder.links.new(combine_xyz_009.outputs[0], set_position_005.inputs[3])
	#group_input_015.Angle -> math_042.Value
	bgi_card_holder.links.new(group_input_015.outputs[5], math_042.inputs[0])
	#math_042.Value -> math_043.Value
	bgi_card_holder.links.new(math_042.outputs[0], math_043.inputs[1])
	#math_043.Value -> combine_xyz_009.X
	bgi_card_holder.links.new(math_043.outputs[0], combine_xyz_009.inputs[0])
	#math_041.Value -> math_043.Value
	bgi_card_holder.links.new(math_041.outputs[0], math_043.inputs[0])
	#select_indexes_1.Boolean -> set_position_005.Selection
	bgi_card_holder.links.new(select_indexes_1.outputs[0], set_position_005.inputs[1])
	#extrude_mesh.Top -> extrude_mesh_001.Selection
	bgi_card_holder.links.new(extrude_mesh.outputs[1], extrude_mesh_001.inputs[1])
	#extrude_mesh_001.Mesh -> set_position_006.Geometry
	bgi_card_holder.links.new(extrude_mesh_001.outputs[0], set_position_006.inputs[0])
	#extrude_mesh_001.Top -> set_position_006.Selection
	bgi_card_holder.links.new(extrude_mesh_001.outputs[1], set_position_006.inputs[1])
	#math_045.Value -> math_044.Value
	bgi_card_holder.links.new(math_045.outputs[0], math_044.inputs[1])
	#math_044.Value -> extrude_mesh_001.Offset Scale
	bgi_card_holder.links.new(math_044.outputs[0], extrude_mesh_001.inputs[3])
	#reroute_003.Output -> math_045.Value
	bgi_card_holder.links.new(reroute_003.outputs[0], math_045.inputs[0])
	#group_input_017.Angle -> math_046.Value
	bgi_card_holder.links.new(group_input_017.outputs[5], math_046.inputs[0])
	#math_046.Value -> math_047.Value
	bgi_card_holder.links.new(math_046.outputs[0], math_047.inputs[1])
	#math_044.Value -> math_047.Value
	bgi_card_holder.links.new(math_044.outputs[0], math_047.inputs[0])
	#combine_xyz_010.Vector -> set_position_006.Offset
	bgi_card_holder.links.new(combine_xyz_010.outputs[0], set_position_006.inputs[3])
	#math_047.Value -> combine_xyz_010.X
	bgi_card_holder.links.new(math_047.outputs[0], combine_xyz_010.inputs[0])
	#set_position_006.Geometry -> extrude_mesh_002.Mesh
	bgi_card_holder.links.new(set_position_006.outputs[0], extrude_mesh_002.inputs[0])
	#extrude_mesh_001.Top -> extrude_mesh_002.Selection
	bgi_card_holder.links.new(extrude_mesh_001.outputs[1], extrude_mesh_002.inputs[1])
	#math_041.Value -> extrude_mesh_002.Offset Scale
	bgi_card_holder.links.new(math_041.outputs[0], extrude_mesh_002.inputs[3])
	#extrude_mesh_002.Mesh -> set_position_007.Geometry
	bgi_card_holder.links.new(extrude_mesh_002.outputs[0], set_position_007.inputs[0])
	#select_indexes_001.Boolean -> boolean_math_002_1.Boolean
	bgi_card_holder.links.new(select_indexes_001.outputs[0], boolean_math_002_1.inputs[0])
	#select_indexes_002.Boolean -> boolean_math_002_1.Boolean
	bgi_card_holder.links.new(select_indexes_002.outputs[0], boolean_math_002_1.inputs[1])
	#boolean_math_002_1.Boolean -> set_position_007.Selection
	bgi_card_holder.links.new(boolean_math_002_1.outputs[0], set_position_007.inputs[1])
	#combine_xyz_011.Vector -> transform_geometry_004.Translation
	bgi_card_holder.links.new(combine_xyz_011.outputs[0], transform_geometry_004.inputs[1])
	#group_input_018.Inner Length -> math_048.Value
	bgi_card_holder.links.new(group_input_018.outputs[1], math_048.inputs[0])
	#math_048.Value -> math_050.Value
	bgi_card_holder.links.new(math_048.outputs[0], math_050.inputs[0])
	#math_050.Value -> combine_xyz_011.Y
	bgi_card_holder.links.new(math_050.outputs[0], combine_xyz_011.inputs[1])
	#group_input_018.Tickness -> math_049.Value
	bgi_card_holder.links.new(group_input_018.outputs[3], math_049.inputs[0])
	#math_049.Value -> math_050.Value
	bgi_card_holder.links.new(math_049.outputs[0], math_050.inputs[1])
	#combine_xyz_011.Vector -> vector_math_001.Vector
	bgi_card_holder.links.new(combine_xyz_011.outputs[0], vector_math_001.inputs[0])
	#vector_math_001.Vector -> transform_geometry_005.Translation
	bgi_card_holder.links.new(vector_math_001.outputs[0], transform_geometry_005.inputs[1])
	#reroute_002.Output -> transform_geometry_004.Geometry
	bgi_card_holder.links.new(reroute_002.outputs[0], transform_geometry_004.inputs[0])
	#reroute_002.Output -> transform_geometry_005.Geometry
	bgi_card_holder.links.new(reroute_002.outputs[0], transform_geometry_005.inputs[0])
	#set_position_007.Geometry -> reroute_002.Input
	bgi_card_holder.links.new(set_position_007.outputs[0], reroute_002.inputs[0])
	#transform_geometry_005.Geometry -> join_geometry.Geometry
	bgi_card_holder.links.new(transform_geometry_005.outputs[0], join_geometry.inputs[0])
	#combine_xyz_009.Vector -> set_position_007.Offset
	bgi_card_holder.links.new(combine_xyz_009.outputs[0], set_position_007.inputs[3])
	#join_geometry.Geometry -> realize_instances.Geometry
	bgi_card_holder.links.new(join_geometry.outputs[0], realize_instances.inputs[0])
	#realize_instances.Geometry -> group_output_1.Geometry
	bgi_card_holder.links.new(realize_instances.outputs[0], group_output_1.inputs[0])
	#math_041.Value -> reroute_003.Input
	bgi_card_holder.links.new(math_041.outputs[0], reroute_003.inputs[0])
	#group_input_017.Inner Height -> math_044.Value
	bgi_card_holder.links.new(group_input_017.outputs[2], math_044.inputs[0])
	#group_input_015.Angle -> math_040.Value
	bgi_card_holder.links.new(group_input_015.outputs[5], math_040.inputs[0])
	#group_input_001_1.Angle -> math_009_1.Value
	bgi_card_holder.links.new(group_input_001_1.outputs[5], math_009_1.inputs[0])
	#group_input_001_1.Tickness -> math_010_1.Value
	bgi_card_holder.links.new(group_input_001_1.outputs[3], math_010_1.inputs[0])
	#math_009_1.Value -> math_010_1.Value
	bgi_card_holder.links.new(math_009_1.outputs[0], math_010_1.inputs[1])
	#math_014.Value -> math_015.Value
	bgi_card_holder.links.new(math_014.outputs[0], math_015.inputs[0])
	#math_015.Value -> math_007.Value
	bgi_card_holder.links.new(math_015.outputs[0], math_007.inputs[0])
	#group_input_001_1.Tickness -> math_011.Value
	bgi_card_holder.links.new(group_input_001_1.outputs[3], math_011.inputs[0])
	#math_010_1.Value -> math_011.Value
	bgi_card_holder.links.new(math_010_1.outputs[0], math_011.inputs[1])
	#math_011.Value -> math_013.Value
	bgi_card_holder.links.new(math_011.outputs[0], math_013.inputs[0])
	#math_013.Value -> math_015.Value
	bgi_card_holder.links.new(math_013.outputs[0], math_015.inputs[1])
	#group_input_004_1.Count -> math_013.Value
	bgi_card_holder.links.new(group_input_004_1.outputs[4], math_013.inputs[1])
	#group_input_005.Inner Width -> math_014.Value
	bgi_card_holder.links.new(group_input_005.outputs[0], math_014.inputs[0])
	#group_input_005.Tickness -> math_014.Value
	bgi_card_holder.links.new(group_input_005.outputs[3], math_014.inputs[1])
	#group_input_007.Count -> math_008.Value
	bgi_card_holder.links.new(group_input_007.outputs[4], math_008.inputs[0])
	#reroute_1.Output -> math_016.Value
	bgi_card_holder.links.new(reroute_1.outputs[0], math_016.inputs[0])
	#math_018.Value -> math_024.Value
	bgi_card_holder.links.new(math_018.outputs[0], math_024.inputs[0])
	#math_016.Value -> math_024.Value
	bgi_card_holder.links.new(math_016.outputs[0], math_024.inputs[1])
	#math_024.Value -> combine_xyz_003.X
	bgi_card_holder.links.new(math_024.outputs[0], combine_xyz_003.inputs[0])
	#math_013.Value -> reroute_1.Input
	bgi_card_holder.links.new(math_013.outputs[0], reroute_1.inputs[0])
	#transform_geometry_004.Geometry -> join_geometry.Geometry
	bgi_card_holder.links.new(transform_geometry_004.outputs[0], join_geometry.inputs[0])
	#transform_geometry.Geometry -> join_geometry.Geometry
	bgi_card_holder.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
	#instance_on_points.Instances -> join_geometry.Geometry
	bgi_card_holder.links.new(instance_on_points.outputs[0], join_geometry.inputs[0])
	return bgi_card_holder

def bgi_card_holder_create():
	bgi_divisor = bgi_divisor_create()
	bgi_select_indexes = bgi_select_indexes_create()

	return bgi_card_holder_node_group(bgi_divisor, bgi_select_indexes)