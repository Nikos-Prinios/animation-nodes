import bpy, math
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling
from mn_utils import *

def updateNode(node, context):
	nodeTreeChanged()


class orbit(Node, AnimationNode):
	bl_idname = "mn_VectorOrbit"
	bl_label = "Vector Orbit"

	axisProperty = bpy.props.EnumProperty(name="axis",items=[("x","x","x"),("y","y","y"),("z","z","z")],update = nodePropertyChanged)

	def init(self, context):
		self.inputs.new("mn_VectorSocket", "Input")
		self.inputs.new("mn_VectorSocket", "Origin point")
		self.inputs.new("mn_FloatSocket", "Distance")
		self.inputs.new("mn_FloatSocket","Time")
		self.outputs.new("mn_VectorSocket", "Output")

	def draw_buttons(self, context, layout):
			col = layout.column(align = True)
			
			row = col.row(align = True)
			row.label("Axis")
			row.prop(self, 'axisProperty', expand=True)

	def execute(self, input):
		Vector_in = input["Input"]
		Origin = input["Origin point"]
		time = input["Time"]
		distance = input["Distance"]

		# X
		if self.axisProperty == "x":
			Vector_in[1] = (math.sin(time * (math.pi / 180)) * distance + Origin[0])
			Vector_in[2] = (math.cos(time * (math.pi / 180)) * distance + Origin[2])
		# Y
		if self.axisProperty == "y":
			Vector_in[0] = (math.sin(time * (math.pi / 180)) * distance + Origin[0])
			Vector_in[2] = (math.cos(time * (math.pi / 180)) * distance + Origin[2])
		# Z
		if self.axisProperty == "z":
			Vector_in[0] = (math.sin(time * (math.pi / 180)) * distance + Origin[0])
			Vector_in[1] = (math.cos(time * (math.pi / 180)) * distance + Origin[2])
		
		output = {}
		output["Output"] = [Vector_in[0],Vector_in[1],Vector_in[2]]
		return output
