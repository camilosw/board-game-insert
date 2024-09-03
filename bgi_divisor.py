import bpy

#initialize bgi_divisor node group
def bgi_divisor_node_group():
	bgi_divisor = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Divisor")

	bgi_divisor.is_modifier = True
	
	#bgi_divisor interface
	#Socket Geometry
	geometry_socket = bgi_divisor.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket.attribute_domain = 'POINT'
	
	#Socket Width
	width_socket = bgi_divisor.interface.new_socket(name = "Width", in_out='INPUT', socket_type = 'NodeSocketFloat')
	width_socket.subtype = 'NONE'
	width_socket.default_value = 0.0
	width_socket.min_value = -3.4028234663852886e+38
	width_socket.max_value = 3.4028234663852886e+38
	width_socket.attribute_domain = 'POINT'
	
	#Socket Length
	length_socket = bgi_divisor.interface.new_socket(name = "Length", in_out='INPUT', socket_type = 'NodeSocketFloat')
	length_socket.subtype = 'NONE'
	length_socket.default_value = 0.0
	length_socket.min_value = -3.4028234663852886e+38
	length_socket.max_value = 3.4028234663852886e+38
	length_socket.attribute_domain = 'POINT'
	
	#Socket Height
	height_socket = bgi_divisor.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
	height_socket.subtype = 'NONE'
	height_socket.default_value = 0.0
	height_socket.min_value = -10000.0
	height_socket.max_value = 10000.0
	height_socket.attribute_domain = 'POINT'
	
	#Socket Thickness
	thickness_socket = bgi_divisor.interface.new_socket(name = "Thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
	thickness_socket.subtype = 'DISTANCE'
	thickness_socket.default_value = 0.0
	thickness_socket.min_value = -3.4028234663852886e+38
	thickness_socket.max_value = 3.4028234663852886e+38
	thickness_socket.attribute_domain = 'POINT'
	
	#Socket Orientation
	orientation_socket = bgi_divisor.interface.new_socket(name = "Orientation", in_out='INPUT', socket_type = 'NodeSocketBool')
	orientation_socket.attribute_domain = 'POINT'
	
	#Socket Add tickness to length
	add_tickness_to_length_socket = bgi_divisor.interface.new_socket(name = "Add tickness to length", in_out='INPUT', socket_type = 'NodeSocketBool')
	add_tickness_to_length_socket.attribute_domain = 'POINT'
	
	#Socket Vertices Z
	vertices_z_socket = bgi_divisor.interface.new_socket(name = "Vertices Z", in_out='INPUT', socket_type = 'NodeSocketInt')
	vertices_z_socket.subtype = 'NONE'
	vertices_z_socket.default_value = 2
	vertices_z_socket.min_value = 2
	vertices_z_socket.max_value = 1000
	vertices_z_socket.attribute_domain = 'POINT'
	
	
	#initialize bgi_divisor nodes
	#node Frame.003
	frame_003 = bgi_divisor.nodes.new("NodeFrame")
	frame_003.label = "Create box"
	frame_003.name = "Frame.003"
	frame_003.label_size = 20
	frame_003.shrink = True
	
	#node Frame
	frame = bgi_divisor.nodes.new("NodeFrame")
	frame.label = "Box lenght"
	frame.name = "Frame"
	frame.label_size = 20
	frame.shrink = True
	
	#node Frame.001
	frame_001 = bgi_divisor.nodes.new("NodeFrame")
	frame_001.label = "Displace to base top"
	frame_001.name = "Frame.001"
	frame_001.label_size = 20
	frame_001.shrink = True
	
	#node Math.004
	math_004 = bgi_divisor.nodes.new("ShaderNodeMath")
	math_004.name = "Math.004"
	math_004.operation = 'DIVIDE'
	math_004.use_clamp = False
	#Value_001
	math_004.inputs[1].default_value = 2.0
	
	#node Math.005
	math_005 = bgi_divisor.nodes.new("ShaderNodeMath")
	math_005.name = "Math.005"
	math_005.operation = 'ADD'
	math_005.use_clamp = False
	
	#node Combine XYZ
	combine_xyz = bgi_divisor.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz.name = "Combine XYZ"
	#X
	combine_xyz.inputs[0].default_value = 0.0
	#Y
	combine_xyz.inputs[1].default_value = 0.0
	
	#node Reroute
	reroute = bgi_divisor.nodes.new("NodeReroute")
	reroute.name = "Reroute"
	#node Group Input
	group_input = bgi_divisor.nodes.new("NodeGroupInput")
	group_input.name = "Group Input"
	group_input.outputs[2].hide = True
	group_input.outputs[6].hide = True
	group_input.outputs[7].hide = True
	
	#node Switch
	switch = bgi_divisor.nodes.new("GeometryNodeSwitch")
	switch.name = "Switch"
	switch.input_type = 'FLOAT'
	
	#node Math.010
	math_010 = bgi_divisor.nodes.new("ShaderNodeMath")
	math_010.name = "Math.010"
	math_010.operation = 'MULTIPLY'
	math_010.use_clamp = False
	#Value_001
	math_010.inputs[1].default_value = 2.0
	
	#node Math.009
	math_009 = bgi_divisor.nodes.new("ShaderNodeMath")
	math_009.name = "Math.009"
	math_009.operation = 'ADD'
	math_009.use_clamp = False
	
	#node Switch.002
	switch_002 = bgi_divisor.nodes.new("GeometryNodeSwitch")
	switch_002.name = "Switch.002"
	switch_002.input_type = 'FLOAT'
	
	#node Switch.006
	switch_006 = bgi_divisor.nodes.new("GeometryNodeSwitch")
	switch_006.name = "Switch.006"
	switch_006.input_type = 'VECTOR'
	#False
	switch_006.inputs[1].default_value = (0.0, 0.0, 0.0)
	#True
	switch_006.inputs[2].default_value = (0.0, 0.0, 1.5707999467849731)
	
	#node Group Input.004
	group_input_004 = bgi_divisor.nodes.new("NodeGroupInput")
	group_input_004.name = "Group Input.004"
	group_input_004.outputs[0].hide = True
	group_input_004.outputs[1].hide = True
	group_input_004.outputs[2].hide = True
	group_input_004.outputs[3].hide = True
	group_input_004.outputs[5].hide = True
	group_input_004.outputs[6].hide = True
	group_input_004.outputs[7].hide = True
	
	#node Transform Geometry.003
	transform_geometry_003 = bgi_divisor.nodes.new("GeometryNodeTransform")
	transform_geometry_003.name = "Transform Geometry.003"
	#Scale
	transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
	
	#node Group Output
	group_output = bgi_divisor.nodes.new("NodeGroupOutput")
	group_output.name = "Group Output"
	group_output.is_active_output = True
	
	#node Group Input.003
	group_input_003 = bgi_divisor.nodes.new("NodeGroupInput")
	group_input_003.name = "Group Input.003"
	group_input_003.outputs[0].hide = True
	group_input_003.outputs[1].hide = True
	group_input_003.outputs[4].hide = True
	group_input_003.outputs[5].hide = True
	group_input_003.outputs[6].hide = True
	group_input_003.outputs[7].hide = True
	
	#node Group Input.002
	group_input_002 = bgi_divisor.nodes.new("NodeGroupInput")
	group_input_002.name = "Group Input.002"
	group_input_002.outputs[0].hide = True
	group_input_002.outputs[1].hide = True
	group_input_002.outputs[4].hide = True
	group_input_002.outputs[5].hide = True
	group_input_002.outputs[6].hide = True
	group_input_002.outputs[7].hide = True
	
	#node Cube.001
	cube_001 = bgi_divisor.nodes.new("GeometryNodeMeshCube")
	cube_001.name = "Cube.001"
	#Vertices X
	cube_001.inputs[1].default_value = 2
	#Vertices Y
	cube_001.inputs[2].default_value = 2
	
	#node Combine XYZ.002
	combine_xyz_002 = bgi_divisor.nodes.new("ShaderNodeCombineXYZ")
	combine_xyz_002.name = "Combine XYZ.002"
	
	#node Group Input.001
	group_input_001 = bgi_divisor.nodes.new("NodeGroupInput")
	group_input_001.name = "Group Input.001"
	group_input_001.outputs[0].hide = True
	group_input_001.outputs[1].hide = True
	group_input_001.outputs[2].hide = True
	group_input_001.outputs[3].hide = True
	group_input_001.outputs[4].hide = True
	group_input_001.outputs[5].hide = True
	group_input_001.outputs[7].hide = True
	
	
	
	#Set parents
	math_004.parent = frame_001
	math_005.parent = frame_001
	combine_xyz.parent = frame_001
	reroute.parent = frame_003
	switch.parent = frame
	math_010.parent = frame
	math_009.parent = frame
	switch_002.parent = frame
	group_input_003.parent = frame_003
	group_input_002.parent = frame_001
	cube_001.parent = frame_003
	combine_xyz_002.parent = frame_003
	group_input_001.parent = frame_003
	
	#Set locations
	frame_003.location = (-107.13336181640625, -207.04380798339844)
	frame.location = (33.70123291015625, -186.63803100585938)
	frame_001.location = (-290.7784423828125, -6.9626922607421875)
	math_004.location = (340.18634033203125, -239.5447540283203)
	math_005.location = (512.5308837890625, -274.523193359375)
	combine_xyz.location = (702.570556640625, -211.09552001953125)
	reroute.location = (193.40106201171875, 293.4632873535156)
	group_input.location = (-905.763916015625, 153.0467071533203)
	switch.location = (-264.0897216796875, 307.9230651855469)
	math_010.location = (-658.4554443359375, 192.7105712890625)
	math_009.location = (-453.9743957519531, 196.95045471191406)
	switch_002.location = (-658.0614013671875, 389.9866027832031)
	switch_006.location = (420.8339538574219, 433.635986328125)
	group_input_004.location = (241.64031982421875, 378.9696960449219)
	transform_geometry_003.location = (787.190185546875, 11.105818748474121)
	group_output.location = (982.4453735351562, 12.077887535095215)
	group_input_003.location = (118.40478515625, 216.35008239746094)
	group_input_002.location = (148.77267456054688, -351.8467712402344)
	cube_001.location = (513.6312255859375, 306.442626953125)
	combine_xyz_002.location = (336.7364501953125, 269.2989501953125)
	group_input_001.location = (337.138916015625, 138.62557983398438)
	
	#Set dimensions
	frame_003.width, frame_003.height = 593.3333740234375, 285.83331298828125
	frame.width, frame.height = 592.0, 407.16668701171875
	frame_001.width, frame_001.height = 752.0, 279.16668701171875
	math_004.width, math_004.height = 140.0, 100.0
	math_005.width, math_005.height = 140.0, 100.0
	combine_xyz.width, combine_xyz.height = 140.0, 100.0
	reroute.width, reroute.height = 16.0, 100.0
	group_input.width, group_input.height = 140.0, 100.0
	switch.width, switch.height = 140.0, 100.0
	math_010.width, math_010.height = 140.0, 100.0
	math_009.width, math_009.height = 140.0, 100.0
	switch_002.width, switch_002.height = 140.0, 100.0
	switch_006.width, switch_006.height = 140.0, 100.0
	group_input_004.width, group_input_004.height = 140.0, 100.0
	transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
	group_output.width, group_output.height = 140.0, 100.0
	group_input_003.width, group_input_003.height = 140.0, 100.0
	group_input_002.width, group_input_002.height = 140.0, 100.0
	cube_001.width, cube_001.height = 140.0, 100.0
	combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
	group_input_001.width, group_input_001.height = 140.0, 100.0
	
	#initialize bgi_divisor links
	#combine_xyz_002.Vector -> cube_001.Size
	bgi_divisor.links.new(combine_xyz_002.outputs[0], cube_001.inputs[0])
	#cube_001.Mesh -> transform_geometry_003.Geometry
	bgi_divisor.links.new(cube_001.outputs[0], transform_geometry_003.inputs[0])
	#combine_xyz.Vector -> transform_geometry_003.Translation
	bgi_divisor.links.new(combine_xyz.outputs[0], transform_geometry_003.inputs[1])
	#math_005.Value -> combine_xyz.Z
	bgi_divisor.links.new(math_005.outputs[0], combine_xyz.inputs[2])
	#switch.Output -> reroute.Input
	bgi_divisor.links.new(switch.outputs[0], reroute.inputs[0])
	#group_input.Orientation -> switch_002.Switch
	bgi_divisor.links.new(group_input.outputs[4], switch_002.inputs[0])
	#reroute.Output -> combine_xyz_002.Y
	bgi_divisor.links.new(reroute.outputs[0], combine_xyz_002.inputs[1])
	#math_010.Value -> math_009.Value
	bgi_divisor.links.new(math_010.outputs[0], math_009.inputs[0])
	#math_004.Value -> math_005.Value
	bgi_divisor.links.new(math_004.outputs[0], math_005.inputs[0])
	#group_input.Thickness -> math_010.Value
	bgi_divisor.links.new(group_input.outputs[3], math_010.inputs[0])
	#switch_002.Output -> math_009.Value
	bgi_divisor.links.new(switch_002.outputs[0], math_009.inputs[1])
	#group_input.Length -> switch_002.False
	bgi_divisor.links.new(group_input.outputs[1], switch_002.inputs[1])
	#group_input.Width -> switch_002.True
	bgi_divisor.links.new(group_input.outputs[0], switch_002.inputs[2])
	#transform_geometry_003.Geometry -> group_output.Geometry
	bgi_divisor.links.new(transform_geometry_003.outputs[0], group_output.inputs[0])
	#group_input_002.Height -> math_004.Value
	bgi_divisor.links.new(group_input_002.outputs[2], math_004.inputs[0])
	#group_input_002.Thickness -> math_005.Value
	bgi_divisor.links.new(group_input_002.outputs[3], math_005.inputs[1])
	#group_input_003.Thickness -> combine_xyz_002.X
	bgi_divisor.links.new(group_input_003.outputs[3], combine_xyz_002.inputs[0])
	#group_input_003.Height -> combine_xyz_002.Z
	bgi_divisor.links.new(group_input_003.outputs[2], combine_xyz_002.inputs[2])
	#group_input.Add tickness to length -> switch.Switch
	bgi_divisor.links.new(group_input.outputs[5], switch.inputs[0])
	#switch_002.Output -> switch.False
	bgi_divisor.links.new(switch_002.outputs[0], switch.inputs[1])
	#math_009.Value -> switch.True
	bgi_divisor.links.new(math_009.outputs[0], switch.inputs[2])
	#switch_006.Output -> transform_geometry_003.Rotation
	bgi_divisor.links.new(switch_006.outputs[0], transform_geometry_003.inputs[2])
	#group_input_004.Orientation -> switch_006.Switch
	bgi_divisor.links.new(group_input_004.outputs[4], switch_006.inputs[0])
	#group_input_001.Vertices Z -> cube_001.Vertices Z
	bgi_divisor.links.new(group_input_001.outputs[6], cube_001.inputs[3])
	return bgi_divisor


def bgi_divisor_create():
	if "BGI Divisor" in bpy.data.node_groups:
		return bpy.data.node_groups["BGI Divisor"]
	else:
		return bgi_divisor_node_group()