import bpy, math
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling
from mn_utils import *

def updateNode(node, context):
	nodeTreeChanged()

class mn_TrackTo(Node, AnimationNode):
	bl_idname = "mn_track_to"
	bl_label = "Track to"
	node_category = "Vector"

	axis = bpy.props.BoolVectorProperty(update = nodePropertyChanged)

	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_ObjectSocket", "input")
		self.inputs.new("mn_ObjectSocket", "track")
		self.outputs.new("mn_VectorSocket", "output")
		self.inputs.new("mn_FloatSocket", "Offset")
		allowCompiling()

	def draw_buttons(self, context, layout):
		col = layout.column(align = True)
			
		row = col.row(align = True)
		row.label("Axis")
		row.prop(self, "axis", index = 0, text = "x")
		row.prop(self, "axis", index = 1, text = "y")
		row.prop(self, "axis", index = 2, text = "z")


	def angle(self,a,b,c,d,i,offset):

		if c < d:
			i *= -1
		
		result = (math.acos((a-b)/math.sqrt((a-b)**2 + (c-d)**2)) * i) + offset
		return result

	def execute(self, input):
		output = {}
		offset = input["Offset"]
		obj = input["input"]

		if obj is None:
			return ""

		obj_x = obj.location[0]
		obj_y = obj.location[1]
		obj_z = obj.location[2]

		track = input["track"]

		if track is None:
			return ""

		track_x = track.location[0]
		track_y = track.location[1]
		track_z = track.location[2]

		X = 0.0
		Y = 0.0
		Z = 0.0

		if self.axis[0]:
			X = self.angle(track_y, obj_y, track_z, obj_z, 1, offset)
		if self.axis[1]:
			Y = self.angle(track_x, obj_x, track_z, obj_z, -1, offset)
		if self.axis[2]:
			Z = self.angle(track_x, obj_x, track_y, obj_y, 1, offset)
		
		output["output"] = [X,Y,Z]
		return output

		
