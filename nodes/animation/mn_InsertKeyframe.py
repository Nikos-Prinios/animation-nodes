import bpy
from bpy.types import Node
from animation_nodes.mn_node_base import AnimationNode
from animation_nodes.mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling
from animation_nodes.mn_utils import *

class mn_InsertKeyframe(Node, AnimationNode):
	bl_idname = "mn_InsertKeyframe"
	bl_label = "Insert Keyframe"
	node_category = "animation"
	loc = bpy.props.BoolVectorProperty(update = nodePropertyChanged)
	rot = bpy.props.BoolVectorProperty(update = nodePropertyChanged)
	sca = bpy.props.BoolVectorProperty(update = nodePropertyChanged)

	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_FloatSocket", "Frame")
		self.inputs.new("mn_FloatSocket", "From")
		self.inputs.new("mn_FloatSocket", "To")
		self.inputs.new("mn_ObjectSocket", "Object")
		
		allowCompiling()
		
	def draw_buttons(self, context, layout):
		col = layout.column(align = True)
		
		row = col.row(align = True)
		row.label("Location")
		row.prop(self, "loc", index = 0, text = "X")
		row.prop(self, "loc", index = 1, text = "Y")
		row.prop(self, "loc", index = 2, text = "Z")
		row = col.row(align = True)
		row.label("Rotation")
		row.prop(self, "rot", index = 0, text = "X")
		row.prop(self, "rot", index = 1, text = "Y")
		row.prop(self, "rot", index = 2, text = "Z")
		row = col.row(align = True)
		row.label("Scale")
		row.prop(self, "sca", index = 0, text = "X")
		row.prop(self, "sca", index = 1, text = "Y")
		row.prop(self, "sca", index = 2, text = "Z")
		
		
	def execute(self, input):
		obj1 = input["Object"]
		f = input["Frame"]
		From = input["From"]
		To = input["To"]
		s = False
		if f > From and f < To:

			for i in range(3):
				if self.loc[i]:
					s = obj1.keyframe_insert(data_path='location', frame=(f), index= i)
				if self.rot[i]:
					s = obj1.keyframe_insert(data_path='rotation_euler', frame=(f), index= i)
				if self.sca[i]:
					s = obj1.keyframe_insert(data_path='scale', frame=(f), index= i)
