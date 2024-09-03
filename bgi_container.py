import bpy

from .bgi_divisor import bgi_divisor_create

#initialize bgi_sides node group
def bgi_sides_node_group():
	bgi_sides = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Sides")

	bgi_sides.is_modifier = True
	
	#bgi_sides interface
	#Socket Geometry
	geometry_socket_1 = bgi_sides.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_1.attribute_domain = 'POINT'
	
	#Socket Width
	width_socket_1 = bgi_sides.interface.new_socket(name = "Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	width_socket_1.subtype = 'NONE'
	width_socket_1.default_value = 0.5
	width_socket_1.min_value = -10000.0
	width_socket_1.max_value = 10000.0
	width_socket_1.attribute_domain = 'POINT'
	
	#Socket Length
	length_socket_1 = bgi_sides.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	length_socket_1.subtype = 'NONE'
	length_socket_1.default_value = 0.0
	length_socket_1.min_value = -3.4028234663852886e+38
	length_socket_1.max_value = 3.4028234663852886e+38
	length_socket_1.attribute_domain = 'POINT'
	
	#Socket Height
	height_socket_1 = bgi_sides.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	height_socket_1.subtype = 'DISTANCE'
	height_socket_1.default_value = 0.0
	height_socket_1.min_value = -3.4028234663852886e+38
	height_socket_1.max_value = 3.4028234663852886e+38
	height_socket_1.attribute_domain = 'POINT'
	
	#Socket Tickness
	tickness_socket = bgi_sides.interface.new_socket(name = "Tickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	tickness_socket.subtype = 'DISTANCE'
	tickness_socket.default_value = 0.0
	tickness_socket.min_value = -3.4028234663852886e+38
	tickness_socket.max_value = 3.4028234663852886e+38
	tickness_socket.attribute_domain = 'POINT'
	
	#Socket Orientation
	orientation_socket_1 = bgi_sides.interface.new_socket(name = "Orientation", in_out='INPUT', socket_type = 'NodeSocketBool')
	orientation_socket_1.attribute_domain = 'POINT'
	
	
	#initialize bgi_sides nodes
	#node Frame.002
	frame_002 = bgi_sides.nodes.new("NodeFrame")
	frame_002.label = "Displace to side"
	frame_002.name = "Frame.002"
	frame_002.label_size = 20
	frame_002.shrink = True
	
	#node Math.008
	math_008 = bgi_sides.nodes.new("ShaderNodeMath")
	math_008.name = "Math.008"
	math_008.operation = 'DIVIDE'
	math_008.use_clamp = False
	#Value_001
	math_008.inputs[1].default_value = 2.0
	
	#node Math.006
	math_006 = bgi_sides.nodes.new("ShaderNodeMath")
	math_006.name = "Math.006"
	math_006.operation = 'DIVIDE'
	math_006.use_clamp = False
	#Value_001
	math_006.inputs[1].default_value = 2.0
	
	#node Math.007
	math_007 = bgi_sides.nodes.new("ShaderNodeMath")
	math_007.name = "Math.007"
	math_007.operation = 'ADD'
	math_007.use_clamp = False
	
	#node Group Input.001
	group_input_001_1 = bgi_sides.nodes.new("NodeGroupInput")
	group_input_001_1.name = "Group Input.001"
	group_input_001_1.outputs[0].hide = True
	group_input_001_1.outputs[1].hide = True
	group_input_001_1.outputs[2].hide = True
	group_input_001_1.outputs[4].hide = True
	group_input_001_1.outputs[5].hide = True
	
	#node Switch.001
	switch_001 = bgi_sides.nodes.new("GeometryNodeSwitch")
	switch_001.name = "Switch.001"
	switch_001.input_type = 'FLOAT'
	
	#node Group Input
	group_input_1 = bgi_sides.nodes.new("NodeGroupInput")
	group_input_1.name = "Group Input"
	group_input_1.outputs[2].hide = True
	group_input_1.outputs[3].hide = True
	group_input_1.outputs[5].hide = True
	
	#node Switch.003
	switch_003 = bgi_sides.nodes.new("GeometryNodeSwitch")
	switch_003.name = "Switch.003"
	switch_003.input_type = 'FLOAT'
	#True
	switch_003.inputs[2].default_value = 0.0
	
	#node Switch.004
	switch_004 = bgi_sides.nodes.new("GeometryNodeSwitch")
	switch_004.name = "Switch.004"
	switch_004.input_type = 'FLOAT'
	#False
	switch_004.inputs[1].default_value = 0.0
	
	#node Switch.005
	switch_005 = bgi_sides.nodes.new("GeometryNodeSwitch")
	switch_005.name = "Switch.005"
	switch_005.input_type = 'VECTOR'
	#False
	switch_005.inputs[1].default_value = (-1.0, 1.0, 1.0)
	#True
	switch_005.inputs[2].default_value = (1.0, -1.0, 1.0)
	
	#node Vector Math
	vector_math = bgi_sides.nodes.new("ShaderNodeVectorMath")
	vector_math.name = "Vector Math"
	vector_math.operation = 'MULTIPLY'
	
	#node Group Input.005
	group_input_005 = bgi_sides.nodes.new("NodeGroupInput")
	group_input_005.name = "Group Input.005"
	group_input_005.outputs[0].hide = True
	group_input_005.outputs[1].hide = True
	group_input_005.outputs[2].hide = True
	group_input_005.outputs[3].hide = True
	group_input_005.outputs[5].hide = True
	
	#node Transform Geometry.002
	transform_geometry_002 = bgi_sides.nodes.new("GeometryNodeTransform")
	transform_geometry_002.name = "Transform Geometry.002"
	#Rotation
	transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Group Output
	group_output_1 = bgi_sides.nodes.new("NodeGroupOutput")
	group_output_1.name = "Group Output"
	group_output_1.is_active_output = True
	
	#node Join Geometry.001
	join_geometry_001 = bgi_sides.nodes.new("GeometryNodeJoinGeometry")
	join_geometry_001.name = "Join Geometry.001"
	
	#node Transform Geometry.001
	transform_geometry_001 = bgi_sides.nodes.new("GeometryNodeTransform")
	transform_geometry_001.name = "Transform Geometry.001"
	#Rotation
	transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Combine XYZ.003
	combine_xyz_003 = bgi_sides.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_003.name = "Combine XYZ.003"
	#Z
	combine_xyz_003.inputs[2].default_value = 0.0
	
	#node Group Input.003
	group_input_003_1 = bgi_sides.nodes.new("NodeGroupInput")
	group_input_003_1.name = "Group Input.003"
	group_input_003_1.outputs[0].hide = True
	group_input_003_1.outputs[1].hide = True
	group_input_003_1.outputs[2].hide = True
	group_input_003_1.outputs[3].hide = True
	group_input_003_1.outputs[5].hide = True
	
	#node Boolean Math
	boolean_math = bgi_sides.nodes.new("FunctionNodeBooleanMath")
	boolean_math.name = "Boolean Math"
	boolean_math.operation = 'NOT'
	
	#node Group
	group = bgi_sides.nodes.new("GeometryNodeGroup")
	group.label = "Divisor"
	group.name = "Group"
	group.node_tree = bgi_divisor
	#Input_9
	group.inputs[6].default_value = 2
	
	#node Group Input.006
	group_input_006 = bgi_sides.nodes.new("NodeGroupInput")
	group_input_006.name = "Group Input.006"
	
	
	
	#Set parents
	math_008.parent = frame_002
	math_006.parent = frame_002
	math_007.parent = frame_002
	group_input_001_1.parent = frame_002
	switch_001.parent = frame_002
	group_input_1.parent = frame_002
	
	#Set locations
	frame_002.location = (4.264312744140625, -44.657989501953125)
	math_008.location = (-95.30523681640625, -92.51611328125)
	math_006.location = (-96.83233642578125, 79.26654052734375)
	math_007.location = (84.212158203125, 43.140045166015625)
	group_input_001_1.location = (-265.3760681152344, -169.3600311279297)
	switch_001.location = (-276.2106018066406, 75.57862854003906)
	group_input_1.location = (-469.7393798828125, 18.116851806640625)
	switch_003.location = (507.470703125, 68.81230926513672)
	switch_004.location = (506.5238037109375, -92.2652587890625)
	switch_005.location = (757.688232421875, -207.6356658935547)
	vector_math.location = (977.6840209960938, -126.65125274658203)
	group_input_005.location = (585.0435180664062, -259.8790588378906)
	transform_geometry_002.location = (1207.24755859375, -17.2479190826416)
	group_output_1.location = (1619.06103515625, 81.56816864013672)
	join_geometry_001.location = (1431.1083984375, 82.13544464111328)
	transform_geometry_001.location = (1212.310546875, 278.6878967285156)
	combine_xyz_003.location = (764.9182739257812, 0.8336200714111328)
	group_input_003_1.location = (285.28070068359375, 54.553409576416016)
	boolean_math.location = (512.9803466796875, 196.8598175048828)
	group.location = (766.5068969726562, 398.8331298828125)
	group_input_006.location = (300.96832275390625, 348.7275085449219)
	
	#Set dimensions
	frame_002.width, frame_002.height = 752.0, 381.83331298828125
	math_008.width, math_008.height = 140.0, 100.0
	math_006.width, math_006.height = 140.0, 100.0
	math_007.width, math_007.height = 140.0, 100.0
	group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
	switch_001.width, switch_001.height = 140.0, 100.0
	group_input_1.width, group_input_1.height = 140.0, 100.0
	switch_003.width, switch_003.height = 140.0, 100.0
	switch_004.width, switch_004.height = 140.0, 100.0
	switch_005.width, switch_005.height = 140.0, 100.0
	vector_math.width, vector_math.height = 140.0, 100.0
	group_input_005.width, group_input_005.height = 140.0, 100.0
	transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
	group_output_1.width, group_output_1.height = 140.0, 100.0
	join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
	transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
	combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
	group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
	boolean_math.width, boolean_math.height = 140.0, 100.0
	group.width, group.height = 140.0, 100.0
	group_input_006.width, group_input_006.height = 140.0, 100.0
	
	#initialize bgi_sides links
	#math_006.Value -> math_007.Value
	bgi_sides.links.new(math_006.outputs[0], math_007.inputs[0])
	#transform_geometry_002.Geometry -> join_geometry_001.Geometry
	bgi_sides.links.new(transform_geometry_002.outputs[0], join_geometry_001.inputs[0])
	#vector_math.Vector -> transform_geometry_002.Translation
	bgi_sides.links.new(vector_math.outputs[0], transform_geometry_002.inputs[1])
	#switch_003.Output -> combine_xyz_003.X
	bgi_sides.links.new(switch_003.outputs[0], combine_xyz_003.inputs[0])
	#group.Geometry -> transform_geometry_002.Geometry
	bgi_sides.links.new(group.outputs[0], transform_geometry_002.inputs[0])
	#group.Geometry -> transform_geometry_001.Geometry
	bgi_sides.links.new(group.outputs[0], transform_geometry_001.inputs[0])
	#math_008.Value -> math_007.Value
	bgi_sides.links.new(math_008.outputs[0], math_007.inputs[1])
	#combine_xyz_003.Vector -> vector_math.Vector
	bgi_sides.links.new(combine_xyz_003.outputs[0], vector_math.inputs[0])
	#combine_xyz_003.Vector -> transform_geometry_001.Translation
	bgi_sides.links.new(combine_xyz_003.outputs[0], transform_geometry_001.inputs[1])
	#join_geometry_001.Geometry -> group_output_1.Geometry
	bgi_sides.links.new(join_geometry_001.outputs[0], group_output_1.inputs[0])
	#math_007.Value -> switch_003.False
	bgi_sides.links.new(math_007.outputs[0], switch_003.inputs[1])
	#math_007.Value -> switch_004.True
	bgi_sides.links.new(math_007.outputs[0], switch_004.inputs[2])
	#switch_004.Output -> combine_xyz_003.Y
	bgi_sides.links.new(switch_004.outputs[0], combine_xyz_003.inputs[1])
	#group_input_003_1.Orientation -> switch_003.Switch
	bgi_sides.links.new(group_input_003_1.outputs[4], switch_003.inputs[0])
	#group_input_003_1.Orientation -> switch_004.Switch
	bgi_sides.links.new(group_input_003_1.outputs[4], switch_004.inputs[0])
	#switch_005.Output -> vector_math.Vector
	bgi_sides.links.new(switch_005.outputs[0], vector_math.inputs[1])
	#group_input_1.Width -> switch_001.False
	bgi_sides.links.new(group_input_1.outputs[0], switch_001.inputs[1])
	#switch_001.Output -> math_006.Value
	bgi_sides.links.new(switch_001.outputs[0], math_006.inputs[0])
	#group_input_1.Length -> switch_001.True
	bgi_sides.links.new(group_input_1.outputs[1], switch_001.inputs[2])
	#group_input_1.Orientation -> switch_001.Switch
	bgi_sides.links.new(group_input_1.outputs[4], switch_001.inputs[0])
	#group_input_005.Orientation -> switch_005.Switch
	bgi_sides.links.new(group_input_005.outputs[4], switch_005.inputs[0])
	#group_input_001_1.Tickness -> math_008.Value
	bgi_sides.links.new(group_input_001_1.outputs[3], math_008.inputs[0])
	#group_input_006.Height -> group.Height
	bgi_sides.links.new(group_input_006.outputs[2], group.inputs[2])
	#group_input_006.Orientation -> group.Orientation
	bgi_sides.links.new(group_input_006.outputs[4], group.inputs[4])
	#group_input_006.Tickness -> group.Thickness
	bgi_sides.links.new(group_input_006.outputs[3], group.inputs[3])
	#group_input_006.Length -> group.Length
	bgi_sides.links.new(group_input_006.outputs[1], group.inputs[1])
	#group_input_006.Width -> group.Width
	bgi_sides.links.new(group_input_006.outputs[0], group.inputs[0])
	#boolean_math.Boolean -> group.Add tickness to length
	bgi_sides.links.new(boolean_math.outputs[0], group.inputs[5])
	#group_input_006.Orientation -> boolean_math.Boolean
	bgi_sides.links.new(group_input_006.outputs[4], boolean_math.inputs[0])
	#transform_geometry_001.Geometry -> join_geometry_001.Geometry
	bgi_sides.links.new(transform_geometry_001.outputs[0], join_geometry_001.inputs[0])
	return bgi_sides

#initialize bgi_small_division node group
def bgi_small_division_node_group():
	bgi_small_division = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Small Division")

	bgi_small_division.is_modifier = True
	
	#bgi_small_division interface
	#Socket Geometry
	geometry_socket_2 = bgi_small_division.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_2.attribute_domain = 'POINT'
	
	#Socket Lenght
	lenght_socket = bgi_small_division.interface.new_socket(name = "Lenght", in_out='INPUT', socket_type = 'NodeSocketFloat')
	lenght_socket.subtype = 'NONE'
	lenght_socket.default_value = 0.5
	lenght_socket.min_value = -10000.0
	lenght_socket.max_value = 10000.0
	lenght_socket.attribute_domain = 'POINT'
	
	#Socket Height
	height_socket_2 = bgi_small_division.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	height_socket_2.subtype = 'NONE'
	height_socket_2.default_value = 0.0
	height_socket_2.min_value = -10000.0
	height_socket_2.max_value = 10000.0
	height_socket_2.attribute_domain = 'POINT'
	
	#Socket Thickness
	thickness_socket_1 = bgi_small_division.interface.new_socket(name = "Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	thickness_socket_1.subtype = 'DISTANCE'
	thickness_socket_1.default_value = 0.0
	thickness_socket_1.min_value = -3.4028234663852886e+38
	thickness_socket_1.max_value = 3.4028234663852886e+38
	thickness_socket_1.attribute_domain = 'POINT'
	
	#Socket Offset Division Main
	offset_division_main_socket = bgi_small_division.interface.new_socket(name = "Offset Division Main", in_out='INPUT', socket_type = 'NodeSocketFloat')
	offset_division_main_socket.subtype = 'NONE'
	offset_division_main_socket.default_value = 0.5
	offset_division_main_socket.min_value = -10000.0
	offset_division_main_socket.max_value = 10000.0
	offset_division_main_socket.attribute_domain = 'POINT'
	
	#Socket Enable Division
	enable_division_socket = bgi_small_division.interface.new_socket(name = "Enable Division", in_out='INPUT', socket_type = 'NodeSocketBool')
	enable_division_socket.attribute_domain = 'POINT'
	
	#Socket Offset Division
	offset_division_socket = bgi_small_division.interface.new_socket(name = "Offset Division", in_out='INPUT', socket_type = 'NodeSocketFloat')
	offset_division_socket.subtype = 'NONE'
	offset_division_socket.default_value = 0.0
	offset_division_socket.min_value = -10000.0
	offset_division_socket.max_value = 10000.0
	offset_division_socket.attribute_domain = 'POINT'
	
	#Socket Side
	side_socket = bgi_small_division.interface.new_socket(name = "Side", in_out='INPUT', socket_type = 'NodeSocketBool')
	side_socket.attribute_domain = 'POINT'
	
	
	#initialize bgi_small_division nodes
	#node Frame
	frame_1 = bgi_small_division.nodes.new("NodeFrame")
	frame_1.label = "Length"
	frame_1.name = "Frame"
	frame_1.label_size = 20
	frame_1.shrink = True
	
	#node Frame.001
	frame_001_1 = bgi_small_division.nodes.new("NodeFrame")
	frame_001_1.label = "Position"
	frame_001_1.name = "Frame.001"
	frame_001_1.label_size = 20
	frame_001_1.shrink = True
	
	#node Group Output
	group_output_2 = bgi_small_division.nodes.new("NodeGroupOutput")
	group_output_2.name = "Group Output"
	group_output_2.is_active_output = True
	
	#node Combine XYZ.003
	combine_xyz_003_1 = bgi_small_division.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_003_1.name = "Combine XYZ.003"
	#Z
	combine_xyz_003_1.inputs[2].default_value = 0.0
	
	#node Switch.001
	switch_001_1 = bgi_small_division.nodes.new("GeometryNodeSwitch")
	switch_001_1.name = "Switch.001"
	switch_001_1.input_type = 'GEOMETRY'
	
	#node Transform Geometry.002
	transform_geometry_002_1 = bgi_small_division.nodes.new("GeometryNodeTransform")
	transform_geometry_002_1.name = "Transform Geometry.002"
	#Rotation
	transform_geometry_002_1.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_002_1.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Group.003
	group_003 = bgi_small_division.nodes.new("GeometryNodeGroup")
	group_003.name = "Group.003"
	group_003.node_tree = bgi_divisor
	#Input_3
	group_003.inputs[0].default_value = 0.0
	#Input_4
	group_003.inputs[4].default_value = False
	#Input_6
	group_003.inputs[5].default_value = False
	#Input_9
	group_003.inputs[6].default_value = 2
	
	#node Group Input.001
	group_input_001_2 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_001_2.name = "Group Input.001"
	group_input_001_2.outputs[0].hide = True
	group_input_001_2.outputs[3].hide = True
	group_input_001_2.outputs[5].hide = True
	group_input_001_2.outputs[6].hide = True
	group_input_001_2.outputs[7].hide = True
	
	#node Reroute
	reroute_1 = bgi_small_division.nodes.new("NodeReroute")
	reroute_1.name = "Reroute"
	#node Math.010
	math_010_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_010_1.name = "Math.010"
	math_010_1.operation = 'SUBTRACT'
	math_010_1.use_clamp = False
	
	#node Math.013
	math_013 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_013.name = "Math.013"
	math_013.operation = 'ADD'
	math_013.use_clamp = False
	
	#node Switch
	switch_1 = bgi_small_division.nodes.new("GeometryNodeSwitch")
	switch_1.name = "Switch"
	switch_1.input_type = 'FLOAT'
	
	#node Group Input.003
	group_input_003_2 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_003_2.name = "Group Input.003"
	group_input_003_2.outputs[0].hide = True
	group_input_003_2.outputs[1].hide = True
	group_input_003_2.outputs[2].hide = True
	group_input_003_2.outputs[4].hide = True
	group_input_003_2.outputs[5].hide = True
	group_input_003_2.outputs[7].hide = True
	
	#node Math.004
	math_004_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_004_1.name = "Math.004"
	math_004_1.operation = 'DIVIDE'
	math_004_1.use_clamp = False
	#Value_001
	math_004_1.inputs[1].default_value = 2.0
	
	#node Math.009
	math_009_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_009_1.name = "Math.009"
	math_009_1.operation = 'DIVIDE'
	math_009_1.use_clamp = False
	#Value_001
	math_009_1.inputs[1].default_value = 2.0
	
	#node Group Input.002
	group_input_002_1 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_002_1.name = "Group Input.002"
	group_input_002_1.outputs[1].hide = True
	group_input_002_1.outputs[3].hide = True
	group_input_002_1.outputs[4].hide = True
	group_input_002_1.outputs[5].hide = True
	group_input_002_1.outputs[6].hide = True
	group_input_002_1.outputs[7].hide = True
	
	#node Math.006
	math_006_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_006_1.name = "Math.006"
	math_006_1.operation = 'SUBTRACT'
	math_006_1.use_clamp = False
	
	#node Math.011
	math_011 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_011.name = "Math.011"
	math_011.operation = 'ADD'
	math_011.use_clamp = False
	
	#node Math.014
	math_014 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_014.name = "Math.014"
	math_014.operation = 'SUBTRACT'
	math_014.use_clamp = False
	
	#node Math
	math = bgi_small_division.nodes.new("ShaderNodeMath")
	math.name = "Math"
	math.operation = 'MULTIPLY'
	math.use_clamp = False
	
	#node Switch.002
	switch_002_1 = bgi_small_division.nodes.new("GeometryNodeSwitch")
	switch_002_1.name = "Switch.002"
	switch_002_1.input_type = 'FLOAT'
	
	#node Switch.003
	switch_003_1 = bgi_small_division.nodes.new("GeometryNodeSwitch")
	switch_003_1.name = "Switch.003"
	switch_003_1.input_type = 'FLOAT'
	#False
	switch_003_1.inputs[1].default_value = 1.0
	#True
	switch_003_1.inputs[2].default_value = -1.0
	
	#node Group Input.005
	group_input_005_1 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_005_1.name = "Group Input.005"
	group_input_005_1.outputs[0].hide = True
	group_input_005_1.outputs[1].hide = True
	group_input_005_1.outputs[2].hide = True
	group_input_005_1.outputs[3].hide = True
	group_input_005_1.outputs[4].hide = True
	group_input_005_1.outputs[6].hide = True
	group_input_005_1.outputs[7].hide = True
	
	#node Math.012
	math_012 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_012.name = "Math.012"
	math_012.operation = 'DIVIDE'
	math_012.use_clamp = False
	#Value_001
	math_012.inputs[1].default_value = 2.0
	
	#node Math.008
	math_008_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_008_1.name = "Math.008"
	math_008_1.operation = 'ADD'
	math_008_1.use_clamp = False
	
	#node Math.005
	math_005_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_005_1.name = "Math.005"
	math_005_1.operation = 'DIVIDE'
	math_005_1.use_clamp = False
	#Value_001
	math_005_1.inputs[1].default_value = 4.0
	
	#node Math.007
	math_007_1 = bgi_small_division.nodes.new("ShaderNodeMath")
	math_007_1.name = "Math.007"
	math_007_1.operation = 'DIVIDE'
	math_007_1.use_clamp = False
	#Value_001
	math_007_1.inputs[1].default_value = 4.0
	
	#node Group Input.004
	group_input_004_1 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_004_1.name = "Group Input.004"
	group_input_004_1.outputs[1].hide = True
	group_input_004_1.outputs[4].hide = True
	group_input_004_1.outputs[5].hide = True
	group_input_004_1.outputs[6].hide = True
	group_input_004_1.outputs[7].hide = True
	
	#node Group Input
	group_input_2 = bgi_small_division.nodes.new("NodeGroupInput")
	group_input_2.name = "Group Input"
	group_input_2.outputs[0].hide = True
	group_input_2.outputs[1].hide = True
	group_input_2.outputs[2].hide = True
	group_input_2.outputs[3].hide = True
	group_input_2.outputs[4].hide = True
	group_input_2.outputs[5].hide = True
	group_input_2.outputs[7].hide = True
	
	
	
	#Set parents
	reroute_1.parent = frame_1
	math_010_1.parent = frame_1
	math_013.parent = frame_1
	switch_1.parent = frame_1
	group_input_003_2.parent = frame_1
	math_004_1.parent = frame_1
	math_009_1.parent = frame_1
	group_input_002_1.parent = frame_1
	math_006_1.parent = frame_1
	math_011.parent = frame_001_1
	math_014.parent = frame_001_1
	math.parent = frame_001_1
	switch_002_1.parent = frame_001_1
	switch_003_1.parent = frame_001_1
	group_input_005_1.parent = frame_001_1
	math_012.parent = frame_001_1
	math_008_1.parent = frame_001_1
	math_005_1.parent = frame_001_1
	math_007_1.parent = frame_001_1
	group_input_004_1.parent = frame_001_1
	group_input_2.parent = frame_001_1
	
	#Set locations
	frame_1.location = (0.0, 0.0)
	frame_001_1.location = (-1.0, -42.059242248535156)
	group_output_2.location = (712.32275390625, 0.0)
	combine_xyz_003_1.location = (299.32904052734375, -101.9224853515625)
	switch_001_1.location = (299.22412109375, 72.9136962890625)
	transform_geometry_002_1.location = (522.32275390625, 11.67864990234375)
	group_003.location = (90.892333984375, 211.0543212890625)
	group_input_001_2.location = (-99.80166625976562, 63.40488052368164)
	reroute_1.location = (-329.7860107421875, 15.988842964172363)
	math_010_1.location = (-498.2729797363281, 381.7553405761719)
	math_013.location = (-489.4416809082031, 207.5665283203125)
	switch_1.location = (-295.16595458984375, 314.9040222167969)
	group_input_003_2.location = (-683.3064575195312, 72.50564575195312)
	math_004_1.location = (-878.318603515625, 284.7608337402344)
	math_009_1.location = (-879.7392578125, 105.03276824951172)
	group_input_002_1.location = (-1060.2733154296875, 151.97671508789062)
	math_006_1.location = (-685.8379516601562, 258.4507141113281)
	math_011.location = (-329.68310546875, -150.40245056152344)
	math_014.location = (-329.68310546875, -312.5521545410156)
	math.location = (110.84293365478516, -157.5116729736328)
	switch_002_1.location = (-109.24691009521484, -163.5585479736328)
	switch_003_1.location = (-103.57552337646484, -331.3835754394531)
	group_input_005_1.location = (112.28951263427734, -84.29143524169922)
	math_012.location = (-514.9334716796875, -153.6031951904297)
	math_008_1.location = (-517.6207275390625, -325.2759094238281)
	math_005_1.location = (-701.2431640625, -303.1621398925781)
	math_007_1.location = (-703.3265991210938, -467.7384338378906)
	group_input_004_1.location = (-892.7057495117188, -185.50465393066406)
	group_input_2.location = (-327.630126953125, -486.745361328125)
	
	#Set dimensions
	frame_1.width, frame_1.height = 962.6666870117188, 486.5
	frame_001_1.width, frame_001_1.height = 1203.3333740234375, 593.1666259765625
	group_output_2.width, group_output_2.height = 140.0, 100.0
	combine_xyz_003_1.width, combine_xyz_003_1.height = 140.0, 100.0
	switch_001_1.width, switch_001_1.height = 140.0, 100.0
	transform_geometry_002_1.width, transform_geometry_002_1.height = 140.0, 100.0
	group_003.width, group_003.height = 140.0, 100.0
	group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
	reroute_1.width, reroute_1.height = 16.0, 100.0
	math_010_1.width, math_010_1.height = 140.0, 100.0
	math_013.width, math_013.height = 140.0, 100.0
	switch_1.width, switch_1.height = 140.0, 100.0
	group_input_003_2.width, group_input_003_2.height = 140.0, 100.0
	math_004_1.width, math_004_1.height = 140.0, 100.0
	math_009_1.width, math_009_1.height = 140.0, 100.0
	group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
	math_006_1.width, math_006_1.height = 140.0, 100.0
	math_011.width, math_011.height = 140.0, 100.0
	math_014.width, math_014.height = 140.0, 100.0
	math.width, math.height = 140.0, 100.0
	switch_002_1.width, switch_002_1.height = 140.0, 100.0
	switch_003_1.width, switch_003_1.height = 140.0, 100.0
	group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
	math_012.width, math_012.height = 140.0, 100.0
	math_008_1.width, math_008_1.height = 140.0, 100.0
	math_005_1.width, math_005_1.height = 140.0, 100.0
	math_007_1.width, math_007_1.height = 140.0, 100.0
	group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
	group_input_2.width, group_input_2.height = 140.0, 100.0
	
	#initialize bgi_small_division links
	#math_009_1.Value -> math_006_1.Value
	bgi_small_division.links.new(math_009_1.outputs[0], math_006_1.inputs[1])
	#math_006_1.Value -> math_010_1.Value
	bgi_small_division.links.new(math_006_1.outputs[0], math_010_1.inputs[0])
	#math_012.Value -> math_011.Value
	bgi_small_division.links.new(math_012.outputs[0], math_011.inputs[0])
	#math_008_1.Value -> math_011.Value
	bgi_small_division.links.new(math_008_1.outputs[0], math_011.inputs[1])
	#math_007_1.Value -> math_008_1.Value
	bgi_small_division.links.new(math_007_1.outputs[0], math_008_1.inputs[1])
	#math_004_1.Value -> math_006_1.Value
	bgi_small_division.links.new(math_004_1.outputs[0], math_006_1.inputs[0])
	#math.Value -> combine_xyz_003_1.Y
	bgi_small_division.links.new(math.outputs[0], combine_xyz_003_1.inputs[1])
	#combine_xyz_003_1.Vector -> transform_geometry_002_1.Translation
	bgi_small_division.links.new(combine_xyz_003_1.outputs[0], transform_geometry_002_1.inputs[1])
	#switch_001_1.Output -> transform_geometry_002_1.Geometry
	bgi_small_division.links.new(switch_001_1.outputs[0], transform_geometry_002_1.inputs[0])
	#group_003.Geometry -> switch_001_1.True
	bgi_small_division.links.new(group_003.outputs[0], switch_001_1.inputs[2])
	#math_005_1.Value -> math_008_1.Value
	bgi_small_division.links.new(math_005_1.outputs[0], math_008_1.inputs[0])
	#transform_geometry_002_1.Geometry -> group_output_2.Geometry
	bgi_small_division.links.new(transform_geometry_002_1.outputs[0], group_output_2.inputs[0])
	#math_006_1.Value -> math_013.Value
	bgi_small_division.links.new(math_006_1.outputs[0], math_013.inputs[0])
	#switch_1.Output -> group_003.Length
	bgi_small_division.links.new(switch_1.outputs[0], group_003.inputs[1])
	#math_010_1.Value -> switch_1.False
	bgi_small_division.links.new(math_010_1.outputs[0], switch_1.inputs[1])
	#math_013.Value -> switch_1.True
	bgi_small_division.links.new(math_013.outputs[0], switch_1.inputs[2])
	#math_012.Value -> math_014.Value
	bgi_small_division.links.new(math_012.outputs[0], math_014.inputs[1])
	#math_008_1.Value -> math_014.Value
	bgi_small_division.links.new(math_008_1.outputs[0], math_014.inputs[0])
	#math_011.Value -> switch_002_1.False
	bgi_small_division.links.new(math_011.outputs[0], switch_002_1.inputs[1])
	#math_014.Value -> switch_002_1.True
	bgi_small_division.links.new(math_014.outputs[0], switch_002_1.inputs[2])
	#group_input_2.Side -> switch_002_1.Switch
	bgi_small_division.links.new(group_input_2.outputs[6], switch_002_1.inputs[0])
	#switch_002_1.Output -> math.Value
	bgi_small_division.links.new(switch_002_1.outputs[0], math.inputs[0])
	#switch_003_1.Output -> math.Value
	bgi_small_division.links.new(switch_003_1.outputs[0], math.inputs[1])
	#group_input_2.Side -> switch_003_1.Switch
	bgi_small_division.links.new(group_input_2.outputs[6], switch_003_1.inputs[0])
	#group_input_001_2.Height -> group_003.Height
	bgi_small_division.links.new(group_input_001_2.outputs[1], group_003.inputs[2])
	#group_input_001_2.Thickness -> group_003.Thickness
	bgi_small_division.links.new(group_input_001_2.outputs[2], group_003.inputs[3])
	#group_input_001_2.Enable Division -> switch_001_1.Switch
	bgi_small_division.links.new(group_input_001_2.outputs[4], switch_001_1.inputs[0])
	#group_input_002_1.Lenght -> math_004_1.Value
	bgi_small_division.links.new(group_input_002_1.outputs[0], math_004_1.inputs[0])
	#group_input_002_1.Thickness -> math_009_1.Value
	bgi_small_division.links.new(group_input_002_1.outputs[2], math_009_1.inputs[0])
	#group_input_003_2.Offset Division Main -> math_013.Value
	bgi_small_division.links.new(group_input_003_2.outputs[3], math_013.inputs[1])
	#reroute_1.Output -> switch_1.Switch
	bgi_small_division.links.new(reroute_1.outputs[0], switch_1.inputs[0])
	#group_input_003_2.Offset Division Main -> math_010_1.Value
	bgi_small_division.links.new(group_input_003_2.outputs[3], math_010_1.inputs[1])
	#group_input_003_2.Side -> reroute_1.Input
	bgi_small_division.links.new(group_input_003_2.outputs[6], reroute_1.inputs[0])
	#group_input_004_1.Lenght -> math_005_1.Value
	bgi_small_division.links.new(group_input_004_1.outputs[0], math_005_1.inputs[0])
	#group_input_004_1.Thickness -> math_007_1.Value
	bgi_small_division.links.new(group_input_004_1.outputs[2], math_007_1.inputs[0])
	#group_input_005_1.Offset Division -> combine_xyz_003_1.X
	bgi_small_division.links.new(group_input_005_1.outputs[5], combine_xyz_003_1.inputs[0])
	#group_input_004_1.Offset Division Main -> math_012.Value
	bgi_small_division.links.new(group_input_004_1.outputs[3], math_012.inputs[0])
	return bgi_small_division

#initialize bgi_container node group
def bgi_container_node_group():
	bgi_container = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Container")

	bgi_container.is_modifier = True
	
	#bgi_container interface
	#Socket Geometry
	geometry_socket_3 = bgi_container.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_3.attribute_domain = 'POINT'
	
	#Socket Inner Width
	inner_width_socket = bgi_container.interface.new_socket(name = "Inner Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_width_socket.subtype = 'DISTANCE'
	inner_width_socket.default_value = 0.10000000149011612
	inner_width_socket.min_value = 0.0
	inner_width_socket.max_value = 3.4028234663852886e+38
	inner_width_socket.attribute_domain = 'POINT'
	
	#Socket Inner Length
	inner_length_socket = bgi_container.interface.new_socket(name = "Inner Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_length_socket.subtype = 'DISTANCE'
	inner_length_socket.default_value = 0.10000000149011612
	inner_length_socket.min_value = 0.0
	inner_length_socket.max_value = 3.4028234663852886e+38
	inner_length_socket.attribute_domain = 'POINT'
	
	#Socket Inner Height
	inner_height_socket = bgi_container.interface.new_socket(name = "Inner Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	inner_height_socket.subtype = 'DISTANCE'
	inner_height_socket.default_value = 0.05000000074505806
	inner_height_socket.min_value = 0.0
	inner_height_socket.max_value = 3.4028234663852886e+38
	inner_height_socket.attribute_domain = 'POINT'
	
	#Socket Thickness
	thickness_socket_2 = bgi_container.interface.new_socket(name = "Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	thickness_socket_2.subtype = 'DISTANCE'
	thickness_socket_2.default_value = 0.005000000353902578
	thickness_socket_2.min_value = 0.0
	thickness_socket_2.max_value = 3.4028234663852886e+38
	thickness_socket_2.attribute_domain = 'POINT'
	
	#Socket Enable Main Division
	enable_main_division_socket = bgi_container.interface.new_socket(name = "Enable Main Division", in_out='INPUT', socket_type = 'NodeSocketBool')
	enable_main_division_socket.attribute_domain = 'POINT'
	
	#Socket Offset Main Division
	offset_main_division_socket = bgi_container.interface.new_socket(name = "Offset Main Division", in_out='INPUT', socket_type = 'NodeSocketFloat')
	offset_main_division_socket.subtype = 'DISTANCE'
	offset_main_division_socket.default_value = 0.0
	offset_main_division_socket.min_value = -3.4028234663852886e+38
	offset_main_division_socket.max_value = 3.4028234663852886e+38
	offset_main_division_socket.attribute_domain = 'POINT'
	
	#Socket Enable Small Division 1
	enable_small_division_1_socket = bgi_container.interface.new_socket(name = "Enable Small Division 1", in_out='INPUT', socket_type = 'NodeSocketBool')
	enable_small_division_1_socket.attribute_domain = 'POINT'
	
	#Socket Offset Small Division 1
	offset_small_division_1_socket = bgi_container.interface.new_socket(name = "Offset Small Division 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
	offset_small_division_1_socket.subtype = 'DISTANCE'
	offset_small_division_1_socket.default_value = 0.0
	offset_small_division_1_socket.min_value = -3.4028234663852886e+38
	offset_small_division_1_socket.max_value = 3.4028234663852886e+38
	offset_small_division_1_socket.attribute_domain = 'POINT'
	
	#Socket Enable Small Division 2
	enable_small_division_2_socket = bgi_container.interface.new_socket(name = "Enable Small Division 2", in_out='INPUT', socket_type = 'NodeSocketBool')
	enable_small_division_2_socket.attribute_domain = 'POINT'
	
	#Socket Offset Small Division 2
	offset_small_division_2_socket = bgi_container.interface.new_socket(name = "Offset Small Division 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
	offset_small_division_2_socket.subtype = 'DISTANCE'
	offset_small_division_2_socket.default_value = 0.0
	offset_small_division_2_socket.min_value = -3.4028234663852886e+38
	offset_small_division_2_socket.max_value = 3.4028234663852886e+38
	offset_small_division_2_socket.attribute_domain = 'POINT'
	
	
	#initialize bgi_container nodes
	#node Frame
	frame_2 = bgi_container.nodes.new("NodeFrame")
	frame_2.label = "Base"
	frame_2.name = "Frame"
	frame_2.label_size = 20
	frame_2.shrink = True
	
	#node Frame.001
	frame_001_2 = bgi_container.nodes.new("NodeFrame")
	frame_001_2.label = "Sides"
	frame_001_2.name = "Frame.001"
	frame_001_2.label_size = 20
	frame_001_2.shrink = True
	
	#node Frame.003
	frame_003_1 = bgi_container.nodes.new("NodeFrame")
	frame_003_1.label = "Small Divisions"
	frame_003_1.name = "Frame.003"
	frame_003_1.label_size = 20
	frame_003_1.shrink = True
	
	#node Frame.002
	frame_002_1 = bgi_container.nodes.new("NodeFrame")
	frame_002_1.label = "Main Division"
	frame_002_1.name = "Frame.002"
	frame_002_1.label_size = 20
	frame_002_1.shrink = True
	
	#node Cube
	cube = bgi_container.nodes.new("GeometryNodeMeshCube")
	cube.name = "Cube"
	#Vertices X
	cube.inputs[1].default_value = 2
	#Vertices Y
	cube.inputs[2].default_value = 2
	#Vertices Z
	cube.inputs[3].default_value = 2
	
	#node Combine XYZ.001
	combine_xyz_001 = bgi_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_001.name = "Combine XYZ.001"
	#X
	combine_xyz_001.inputs[0].default_value = 0.0
	#Y
	combine_xyz_001.inputs[1].default_value = 0.0
	
	#node Combine XYZ
	combine_xyz_1 = bgi_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_1.name = "Combine XYZ"
	
	#node Math
	math_1 = bgi_container.nodes.new("ShaderNodeMath")
	math_1.name = "Math"
	math_1.operation = 'DIVIDE'
	math_1.use_clamp = False
	#Value_001
	math_1.inputs[1].default_value = 2.0
	
	#node Reroute
	reroute_2 = bgi_container.nodes.new("NodeReroute")
	reroute_2.name = "Reroute"
	#node Reroute.001
	reroute_001 = bgi_container.nodes.new("NodeReroute")
	reroute_001.name = "Reroute.001"
	#node Math.001
	math_001 = bgi_container.nodes.new("ShaderNodeMath")
	math_001.name = "Math.001"
	math_001.operation = 'MULTIPLY'
	math_001.use_clamp = False
	#Value_001
	math_001.inputs[1].default_value = 2.0
	
	#node Math.002
	math_002 = bgi_container.nodes.new("ShaderNodeMath")
	math_002.name = "Math.002"
	math_002.operation = 'ADD'
	math_002.use_clamp = False
	
	#node Math.003
	math_003 = bgi_container.nodes.new("ShaderNodeMath")
	math_003.name = "Math.003"
	math_003.operation = 'ADD'
	math_003.use_clamp = False
	
	#node Transform Geometry
	transform_geometry = bgi_container.nodes.new("GeometryNodeTransform")
	transform_geometry.name = "Transform Geometry"
	#Rotation
	transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Group Input
	group_input_3 = bgi_container.nodes.new("NodeGroupInput")
	group_input_3.name = "Group Input"
	group_input_3.outputs[2].hide = True
	group_input_3.outputs[4].hide = True
	group_input_3.outputs[5].hide = True
	group_input_3.outputs[6].hide = True
	group_input_3.outputs[7].hide = True
	group_input_3.outputs[8].hide = True
	group_input_3.outputs[9].hide = True
	group_input_3.outputs[10].hide = True
	
	#node Group
	group_1 = bgi_container.nodes.new("GeometryNodeGroup")
	group_1.label = "Sides"
	group_1.name = "Group"
	group_1.node_tree = bgi_sides
	#Input_5
	group_1.inputs[4].default_value = False
	
	#node Group.001
	group_001 = bgi_container.nodes.new("GeometryNodeGroup")
	group_001.label = "Sides"
	group_001.name = "Group.001"
	group_001.node_tree = bgi_sides
	#Input_5
	group_001.inputs[4].default_value = True
	
	#node Group Input.001
	group_input_001_3 = bgi_container.nodes.new("NodeGroupInput")
	group_input_001_3.name = "Group Input.001"
	group_input_001_3.outputs[4].hide = True
	group_input_001_3.outputs[5].hide = True
	group_input_001_3.outputs[6].hide = True
	group_input_001_3.outputs[7].hide = True
	group_input_001_3.outputs[8].hide = True
	group_input_001_3.outputs[9].hide = True
	group_input_001_3.outputs[10].hide = True
	
	#node Group Input.002
	group_input_002_2 = bgi_container.nodes.new("NodeGroupInput")
	group_input_002_2.name = "Group Input.002"
	group_input_002_2.outputs[4].hide = True
	group_input_002_2.outputs[5].hide = True
	group_input_002_2.outputs[6].hide = True
	group_input_002_2.outputs[7].hide = True
	group_input_002_2.outputs[8].hide = True
	group_input_002_2.outputs[9].hide = True
	group_input_002_2.outputs[10].hide = True
	
	#node Group Input.007
	group_input_007 = bgi_container.nodes.new("NodeGroupInput")
	group_input_007.name = "Group Input.007"
	group_input_007.outputs[0].hide = True
	group_input_007.outputs[4].hide = True
	group_input_007.outputs[8].hide = True
	group_input_007.outputs[9].hide = True
	group_input_007.outputs[10].hide = True
	
	#node Group.005
	group_005 = bgi_container.nodes.new("GeometryNodeGroup")
	group_005.label = "Small Division"
	group_005.name = "Group.005"
	group_005.node_tree = bgi_small_division
	#Input_7
	group_005.inputs[6].default_value = True
	
	#node Group Input.008
	group_input_008 = bgi_container.nodes.new("NodeGroupInput")
	group_input_008.name = "Group Input.008"
	group_input_008.outputs[0].hide = True
	group_input_008.outputs[4].hide = True
	group_input_008.outputs[6].hide = True
	group_input_008.outputs[7].hide = True
	group_input_008.outputs[10].hide = True
	
	#node Group.004
	group_004 = bgi_container.nodes.new("GeometryNodeGroup")
	group_004.label = "Small Division"
	group_004.name = "Group.004"
	group_004.node_tree = bgi_small_division
	#Input_7
	group_004.inputs[6].default_value = False
	
	#node Group Output
	group_output_3 = bgi_container.nodes.new("NodeGroupOutput")
	group_output_3.name = "Group Output"
	group_output_3.is_active_output = True
	
	#node Join Geometry
	join_geometry = bgi_container.nodes.new("GeometryNodeJoinGeometry")
	join_geometry.name = "Join Geometry"
	
	#node Transform Geometry.001
	transform_geometry_001_1 = bgi_container.nodes.new("GeometryNodeTransform")
	transform_geometry_001_1.name = "Transform Geometry.001"
	#Rotation
	transform_geometry_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry_001_1.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Switch
	switch_2 = bgi_container.nodes.new("GeometryNodeSwitch")
	switch_2.name = "Switch"
	switch_2.input_type = 'GEOMETRY'
	
	#node Combine XYZ.002
	combine_xyz_002_1 = bgi_container.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_002_1.name = "Combine XYZ.002"
	#X
	combine_xyz_002_1.inputs[0].default_value = 0.0
	#Z
	combine_xyz_002_1.inputs[2].default_value = 0.0
	
	#node Group.002
	group_002 = bgi_container.nodes.new("GeometryNodeGroup")
	group_002.name = "Group.002"
	group_002.node_tree = bgi_divisor
	#Input_2
	group_002.inputs[1].default_value = 0.0
	#Input_4
	group_002.inputs[4].default_value = True
	#Input_6
	group_002.inputs[5].default_value = False
	#Input_9
	group_002.inputs[6].default_value = 2
	
	#node Group Input.003
	group_input_003_3 = bgi_container.nodes.new("NodeGroupInput")
	group_input_003_3.name = "Group Input.003"
	group_input_003_3.outputs[1].hide = True
	group_input_003_3.outputs[6].hide = True
	group_input_003_3.outputs[7].hide = True
	group_input_003_3.outputs[8].hide = True
	group_input_003_3.outputs[9].hide = True
	group_input_003_3.outputs[10].hide = True
	
	
	
	#Set parents
	cube.parent = frame_2
	combine_xyz_001.parent = frame_2
	combine_xyz_1.parent = frame_2
	math_1.parent = frame_2
	reroute_2.parent = frame_2
	reroute_001.parent = frame_2
	math_001.parent = frame_2
	math_002.parent = frame_2
	math_003.parent = frame_2
	transform_geometry.parent = frame_2
	group_input_3.parent = frame_2
	group_1.parent = frame_001_2
	group_001.parent = frame_001_2
	group_input_001_3.parent = frame_001_2
	group_input_002_2.parent = frame_001_2
	group_input_007.parent = frame_003_1
	group_005.parent = frame_003_1
	group_input_008.parent = frame_003_1
	group_004.parent = frame_003_1
	transform_geometry_001_1.parent = frame_002_1
	switch_2.parent = frame_002_1
	combine_xyz_002_1.parent = frame_002_1
	group_002.parent = frame_002_1
	group_input_003_3.parent = frame_002_1
	
	#Set locations
	frame_2.location = (-147.6666259765625, 817.3333129882812)
	frame_001_2.location = (-151.33334350585938, -185.66665649414062)
	frame_003_1.location = (-265.3333435058594, -803.0)
	frame_002_1.location = (-610.3333740234375, -1060.0)
	cube.location = (-146.71456909179688, -45.32170486450195)
	combine_xyz_001.location = (-149.05105590820312, -226.1741943359375)
	combine_xyz_1.location = (-325.9454040527344, -50.780948638916016)
	math_1.location = (-329.0421447753906, -197.6778106689453)
	reroute_2.location = (-774.226318359375, -306.66412353515625)
	reroute_001.location = (-382.6703796386719, -308.0303955078125)
	math_001.location = (-774.8916625976562, 32.60940933227539)
	math_002.location = (-565.8108520507812, 31.8595027923584)
	math_003.location = (-568.05908203125, -136.11904907226562)
	transform_geometry.location = (70.38475799560547, -40.947845458984375)
	group_input_3.location = (-964.4511108398438, -187.9259796142578)
	group_1.location = (69.69564056396484, 571.5012817382812)
	group_001.location = (68.90235900878906, 345.7874755859375)
	group_input_001_3.location = (-128.0389862060547, 519.2620849609375)
	group_input_002_2.location = (-128.83218383789062, 293.54827880859375)
	group_input_007.location = (-15.168620109558105, 593.4089965820312)
	group_005.location = (194.1497344970703, 408.5351257324219)
	group_input_008.location = (-7.443929195404053, 356.0987548828125)
	group_004.location = (192.83740234375, 647.1287231445312)
	group_output_3.location = (425.3333435058594, -19.33333396911621)
	join_geometry.location = (232.0, -19.33333396911621)
	transform_geometry_001_1.location = (88.33331298828125, 1002.0)
	switch_2.location = (-124.33331298828125, 1002.0)
	combine_xyz_002_1.location = (-124.33331298828125, 828.0)
	group_002.location = (-336.99993896484375, 1137.3333740234375)
	group_input_003_3.location = (-530.333251953125, 944.0)
	
	#Set dimensions
	frame_2.width, frame_2.height = 1232.6666259765625, 441.8333435058594
	frame_001_2.width, frame_001_2.height = 396.6666564941406, 473.1666259765625
	frame_003_1.width, frame_003_1.height = 407.33331298828125, 523.8333129882812
	frame_002_1.width, frame_002_1.height = 816.6666259765625, 491.166748046875
	cube.width, cube.height = 140.0, 100.0
	combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
	combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
	math_1.width, math_1.height = 140.0, 100.0
	reroute_2.width, reroute_2.height = 16.0, 100.0
	reroute_001.width, reroute_001.height = 16.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	math_002.width, math_002.height = 140.0, 100.0
	math_003.width, math_003.height = 140.0, 100.0
	transform_geometry.width, transform_geometry.height = 140.0, 100.0
	group_input_3.width, group_input_3.height = 140.0, 100.0
	group_1.width, group_1.height = 140.0, 100.0
	group_001.width, group_001.height = 140.0, 100.0
	group_input_001_3.width, group_input_001_3.height = 140.0, 100.0
	group_input_002_2.width, group_input_002_2.height = 140.0, 100.0
	group_input_007.width, group_input_007.height = 140.0, 100.0
	group_005.width, group_005.height = 140.0, 100.0
	group_input_008.width, group_input_008.height = 140.0, 100.0
	group_004.width, group_004.height = 140.0, 100.0
	group_output_3.width, group_output_3.height = 140.0, 100.0
	join_geometry.width, join_geometry.height = 140.0, 100.0
	transform_geometry_001_1.width, transform_geometry_001_1.height = 140.0, 100.0
	switch_2.width, switch_2.height = 140.0, 100.0
	combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
	group_002.width, group_002.height = 140.0, 100.0
	group_input_003_3.width, group_input_003_3.height = 140.0, 100.0
	
	#initialize bgi_container links
	#combine_xyz_1.Vector -> cube.Size
	bgi_container.links.new(combine_xyz_1.outputs[0], cube.inputs[0])
	#cube.Mesh -> transform_geometry.Geometry
	bgi_container.links.new(cube.outputs[0], transform_geometry.inputs[0])
	#reroute_001.Output -> math_1.Value
	bgi_container.links.new(reroute_001.outputs[0], math_1.inputs[0])
	#combine_xyz_001.Vector -> transform_geometry.Translation
	bgi_container.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
	#math_1.Value -> combine_xyz_001.Z
	bgi_container.links.new(math_1.outputs[0], combine_xyz_001.inputs[2])
	#group_input_3.Thickness -> math_001.Value
	bgi_container.links.new(group_input_3.outputs[3], math_001.inputs[0])
	#math_001.Value -> math_002.Value
	bgi_container.links.new(math_001.outputs[0], math_002.inputs[0])
	#group_input_3.Inner Width -> math_002.Value
	bgi_container.links.new(group_input_3.outputs[0], math_002.inputs[1])
	#math_002.Value -> combine_xyz_1.X
	bgi_container.links.new(math_002.outputs[0], combine_xyz_1.inputs[0])
	#math_001.Value -> math_003.Value
	bgi_container.links.new(math_001.outputs[0], math_003.inputs[0])
	#group_input_3.Inner Length -> math_003.Value
	bgi_container.links.new(group_input_3.outputs[1], math_003.inputs[1])
	#math_003.Value -> combine_xyz_1.Y
	bgi_container.links.new(math_003.outputs[0], combine_xyz_1.inputs[1])
	#group_input_3.Thickness -> reroute_2.Input
	bgi_container.links.new(group_input_3.outputs[3], reroute_2.inputs[0])
	#reroute_2.Output -> reroute_001.Input
	bgi_container.links.new(reroute_2.outputs[0], reroute_001.inputs[0])
	#reroute_001.Output -> combine_xyz_1.Z
	bgi_container.links.new(reroute_001.outputs[0], combine_xyz_1.inputs[2])
	#group_input_001_3.Inner Width -> group_1.Width
	bgi_container.links.new(group_input_001_3.outputs[0], group_1.inputs[0])
	#group_input_001_3.Thickness -> group_1.Tickness
	bgi_container.links.new(group_input_001_3.outputs[3], group_1.inputs[3])
	#group_input_001_3.Inner Height -> group_1.Height
	bgi_container.links.new(group_input_001_3.outputs[2], group_1.inputs[2])
	#group_input_001_3.Inner Length -> group_1.Length
	bgi_container.links.new(group_input_001_3.outputs[1], group_1.inputs[1])
	#group_input_002_2.Inner Width -> group_001.Width
	bgi_container.links.new(group_input_002_2.outputs[0], group_001.inputs[0])
	#group_input_002_2.Thickness -> group_001.Tickness
	bgi_container.links.new(group_input_002_2.outputs[3], group_001.inputs[3])
	#group_input_002_2.Inner Height -> group_001.Height
	bgi_container.links.new(group_input_002_2.outputs[2], group_001.inputs[2])
	#group_input_002_2.Inner Length -> group_001.Length
	bgi_container.links.new(group_input_002_2.outputs[1], group_001.inputs[1])
	#group_input_003_3.Inner Height -> group_002.Height
	bgi_container.links.new(group_input_003_3.outputs[2], group_002.inputs[2])
	#group_input_003_3.Thickness -> group_002.Thickness
	bgi_container.links.new(group_input_003_3.outputs[3], group_002.inputs[3])
	#group_input_003_3.Enable Main Division -> switch_2.Switch
	bgi_container.links.new(group_input_003_3.outputs[4], switch_2.inputs[0])
	#group_002.Geometry -> switch_2.True
	bgi_container.links.new(group_002.outputs[0], switch_2.inputs[2])
	#switch_2.Output -> transform_geometry_001_1.Geometry
	bgi_container.links.new(switch_2.outputs[0], transform_geometry_001_1.inputs[0])
	#combine_xyz_002_1.Vector -> transform_geometry_001_1.Translation
	bgi_container.links.new(combine_xyz_002_1.outputs[0], transform_geometry_001_1.inputs[1])
	#group_input_003_3.Offset Main Division -> combine_xyz_002_1.Y
	bgi_container.links.new(group_input_003_3.outputs[5], combine_xyz_002_1.inputs[1])
	#group_input_003_3.Inner Width -> group_002.Width
	bgi_container.links.new(group_input_003_3.outputs[0], group_002.inputs[0])
	#group_input_007.Offset Small Division 1 -> group_004.Offset Division
	bgi_container.links.new(group_input_007.outputs[7], group_004.inputs[5])
	#group_input_007.Thickness -> group_004.Thickness
	bgi_container.links.new(group_input_007.outputs[3], group_004.inputs[2])
	#group_input_007.Inner Height -> group_004.Height
	bgi_container.links.new(group_input_007.outputs[2], group_004.inputs[1])
	#group_input_007.Inner Length -> group_004.Lenght
	bgi_container.links.new(group_input_007.outputs[1], group_004.inputs[0])
	#group_input_007.Enable Small Division 1 -> group_004.Enable Division
	bgi_container.links.new(group_input_007.outputs[6], group_004.inputs[4])
	#group_input_007.Offset Main Division -> group_004.Offset Division Main
	bgi_container.links.new(group_input_007.outputs[5], group_004.inputs[3])
	#group_input_008.Thickness -> group_005.Thickness
	bgi_container.links.new(group_input_008.outputs[3], group_005.inputs[2])
	#group_input_008.Inner Height -> group_005.Height
	bgi_container.links.new(group_input_008.outputs[2], group_005.inputs[1])
	#group_input_008.Inner Length -> group_005.Lenght
	bgi_container.links.new(group_input_008.outputs[1], group_005.inputs[0])
	#group_input_008.Offset Main Division -> group_005.Offset Division Main
	bgi_container.links.new(group_input_008.outputs[5], group_005.inputs[3])
	#group_005.Geometry -> join_geometry.Geometry
	bgi_container.links.new(group_005.outputs[0], join_geometry.inputs[0])
	#group_input_008.Enable Small Division 2 -> group_005.Enable Division
	bgi_container.links.new(group_input_008.outputs[8], group_005.inputs[4])
	#group_input_008.Offset Small Division 2 -> group_005.Offset Division
	bgi_container.links.new(group_input_008.outputs[9], group_005.inputs[5])
	#join_geometry.Geometry -> group_output_3.Geometry
	bgi_container.links.new(join_geometry.outputs[0], group_output_3.inputs[0])
	#group_004.Geometry -> join_geometry.Geometry
	bgi_container.links.new(group_004.outputs[0], join_geometry.inputs[0])
	#transform_geometry_001_1.Geometry -> join_geometry.Geometry
	bgi_container.links.new(transform_geometry_001_1.outputs[0], join_geometry.inputs[0])
	#group_001.Geometry -> join_geometry.Geometry
	bgi_container.links.new(group_001.outputs[0], join_geometry.inputs[0])
	#group_1.Geometry -> join_geometry.Geometry
	bgi_container.links.new(group_1.outputs[0], join_geometry.inputs[0])
	#transform_geometry.Geometry -> join_geometry.Geometry
	bgi_container.links.new(transform_geometry.outputs[0], join_geometry.inputs[0])
	return bgi_container

def bgi_container_create():
	bgi_divisor = bgi_divisor_create()
	
	if "BGI Sides" in bpy.data.node_groups:
		bgi_sides = bpy.data.node_groups["BGI Sides"]
	else:
		bgi_sides = bgi_sides_node_group(bgi_divisor)

	if "BGI Small Division" in bpy.data.node_groups:
		bgi_small_division = bpy.data.node_groups["BGI Small Division"]
	else:
		bgi_small_division = bgi_small_division_node_group(bgi_divisor)

	return bgi_container_node_group(bgi_divisor, bgi_sides, bgi_small_division)