import bpy

#initialize bgi_select_indexes node group
def bgi_select_indexes_node_group():
	bgi_select_indexes = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "BGI Select Indexes")

	
	#bgi_select_indexes interface
	#Socket Boolean
	boolean_socket = bgi_select_indexes.interface.new_socket(name = "Boolean", in_out='OUTPUT', socket_type = 'NodeSocketBool')
	boolean_socket.attribute_domain = 'POINT'
	
	#Socket From
	from_socket = bgi_select_indexes.interface.new_socket(name = "From", in_out='INPUT', socket_type = 'NodeSocketInt')
	from_socket.subtype = 'NONE'
	from_socket.default_value = 0
	from_socket.min_value = -2147483648
	from_socket.max_value = 2147483647
	from_socket.attribute_domain = 'POINT'
	
	#Socket To
	to_socket = bgi_select_indexes.interface.new_socket(name = "To", in_out='INPUT', socket_type = 'NodeSocketInt')
	to_socket.subtype = 'NONE'
	to_socket.default_value = 1
	to_socket.min_value = -2147483648
	to_socket.max_value = 2147483647
	to_socket.attribute_domain = 'POINT'
	
	
	#initialize bgi_select_indexes nodes
	#node Compare
	compare = bgi_select_indexes.nodes.new("FunctionNodeCompare")
	compare.name = "Compare"
	compare.data_type = 'INT'
	compare.mode = 'ELEMENT'
	compare.operation = 'GREATER_EQUAL'
	
	#node Boolean Math.002
	boolean_math_002 = bgi_select_indexes.nodes.new("FunctionNodeBooleanMath")
	boolean_math_002.name = "Boolean Math.002"
	boolean_math_002.operation = 'AND'
	
	#node Compare.001
	compare_001 = bgi_select_indexes.nodes.new("FunctionNodeCompare")
	compare_001.name = "Compare.001"
	compare_001.data_type = 'INT'
	compare_001.mode = 'ELEMENT'
	compare_001.operation = 'LESS_EQUAL'
	
	#node Index.002
	index_002 = bgi_select_indexes.nodes.new("GeometryNodeInputIndex")
	index_002.name = "Index.002"
	
	#node Group Input
	group_input_1 = bgi_select_indexes.nodes.new("NodeGroupInput")
	group_input_1.name = "Group Input"
	
	#node Select indexes
	select_indexes = bgi_select_indexes.nodes.new("NodeGroupOutput")
	select_indexes.name = "Select indexes"
	select_indexes.is_active_output = True
	
	
	
	
	#Set locations
	compare.location = (-17.02735710144043, 78.89606475830078)
	boolean_math_002.location = (176.45225524902344, 13.74402904510498)
	compare_001.location = (-19.65577507019043, -89.41551971435547)
	index_002.location = (-186.090087890625, -94.55722045898438)
	group_input_1.location = (-429.8978576660156, -16.65589714050293)
	select_indexes.location = (397.9938659667969, 12.272765159606934)
	
	#Set dimensions
	compare.width, compare.height = 140.0, 100.0
	boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
	compare_001.width, compare_001.height = 140.0, 100.0
	index_002.width, index_002.height = 140.0, 100.0
	group_input_1.width, group_input_1.height = 140.0, 100.0
	select_indexes.width, select_indexes.height = 140.0, 100.0
	
	#initialize bgi_select_indexes links
	#compare.Result -> boolean_math_002.Boolean
	bgi_select_indexes.links.new(compare.outputs[0], boolean_math_002.inputs[0])
	#index_002.Index -> compare_001.A
	bgi_select_indexes.links.new(index_002.outputs[0], compare_001.inputs[2])
	#compare_001.Result -> boolean_math_002.Boolean
	bgi_select_indexes.links.new(compare_001.outputs[0], boolean_math_002.inputs[1])
	#index_002.Index -> compare.A
	bgi_select_indexes.links.new(index_002.outputs[0], compare.inputs[2])
	#boolean_math_002.Boolean -> select_indexes.Boolean
	bgi_select_indexes.links.new(boolean_math_002.outputs[0], select_indexes.inputs[0])
	#group_input_1.From -> compare.B
	bgi_select_indexes.links.new(group_input_1.outputs[0], compare.inputs[3])
	#group_input_1.To -> compare_001.B
	bgi_select_indexes.links.new(group_input_1.outputs[1], compare_001.inputs[3])
	return bgi_select_indexes

def bgi_select_indexes_create():
	if "BGI Select Indexes" in bpy.data.node_groups:
		return bpy.data.node_groups["BGI Select Indexes"]
	else:
		return bgi_select_indexes_node_group()