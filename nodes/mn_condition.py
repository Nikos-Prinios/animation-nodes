import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodeTreeChanged, allowCompiling, forbidCompiling


def updateNode(node, context):
	nodeTreeChanged()

class mn_Condition(Node, AnimationNode):
	bl_idname = "mn_Condition"
	bl_label = "Condition"
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_BooleanSocket", "Condition")
		self.inputs.new("mn_GenericSocket", "True")
		self.inputs.new("mn_GenericSocket", "False")
		self.outputs.new("mn_GenericSocket", "Value")
		allowCompiling()
		
	def execute(self, input):
		output = {}

		condition = input["Condition"]
		A = input["True"]
		B = input["False"]

		if condition:
			output["Value"] = A
		else:
			output["Value"] = B

		return output
		
