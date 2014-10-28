import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodeTreeChanged, allowCompiling, forbidCompiling


def updateNode(node, context):
	nodeTreeChanged()

class mn_ShapeKeys(Node, AnimationNode):
	bl_idname = "mn_ShapeKeys"
	bl_label = "Object Shape Keys"

	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_ObjectSocket", "Object")
		self.inputs.new("mn_StringSocket", "Shape key")
		self.inputs.new("mn_FloatSocket", "Value")
		allowCompiling()

	def execute(self, input):
		object = input["Object"]
		Shape = input["Shape key"]
		Value = input["Value"]
		obj_shape_keys = object.data.shape_keys.key_blocks
		if Shape in obj_shape_keys:
			object.data.shape_keys.key_blocks[Shape].value=Value

		if object is None:
			return ""

