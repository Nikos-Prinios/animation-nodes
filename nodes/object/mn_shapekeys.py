import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodeTreeChanged, allowCompiling, forbidCompiling

def updateNode(node, context):
	nodeTreeChanged()

class mn_ShapeKeys(Node, AnimationNode):
	bl_idname = "mn_ShapeKeys"
	bl_label = "Object Shape Keys"

	def get_shapes_menu_items(self, context):
		shapes_menu_items = []
		for s in bpy.data.shape_keys:
			for sh in s.key_blocks:
				shapes_menu_items.append((sh.name, sh.name, ""))
		if len(shapes_menu_items) == 0: shapes_menu_items.append(("NONE", "NONE", ""))
		return shapes_menu_items

	shapes_menu = bpy.props.EnumProperty(name = "Shape Keys Menu", items = get_shapes_menu_items)
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_ObjectSocket", "Object")
		self.inputs.new("mn_FloatSocket", "Value")
		allowCompiling()
	
	def draw_buttons(self, context, layout):
		col = layout.column(align = True)
		layout.prop(self, "shapes_menu")

	def execute(self, input):
		obj = input["Object"]
		if obj is None:
			return ""
		Shape = self.shapes_menu
		Value = input["Value"]
		try:
			obj_shape_keys = obj.data.shape_keys.key_blocks
			if Shape in obj_shape_keys:
				obj.data.shape_keys.key_blocks[Shape].value=Value
		except:
			return ""

