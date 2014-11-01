import bpy, re, string
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodeTreeChanged, allowCompiling, forbidCompiling

def updateNode(node, context):
	nodeTreeChanged()

class mn_Text_Split(Node, AnimationNode):
	bl_idname = "mn_Text_Split"
	bl_label = "Split Text"

	split_options = [
		("Characters", "Characters", ""),
		("Words", "Words", ""),
		("Sentences", "Sentences", ""),
		("Lines", "Lines", "") ]

	split_menu = bpy.props.EnumProperty(name = "Split by", items = split_options, default = "Words")
	

	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_StringSocket","Text")
		self.outputs.new("mn_StringListSocket", "List")
		self.outputs.new("mn_IntegerSocket", "Length")
		allowCompiling()
	
	def draw_buttons(self, context, layout):
		layout.prop(self, "split_menu")

	def execute(self, input):
		output = {}
		options = self.split_menu
		txt = input["Text"]
		string_list = []

		if txt == "":
			return ""
		if options == "Characters":
			string_list = list(txt)
		elif options == "Words":
			string_list = txt.split()
		elif options == "Lines":
			string_list = txt.split('\n')
		elif options == "Sentences":
			string_list = re.split(r' *[\.\?!][\'"\)\]]* *', txt)

		output["List"] = string_list
		output["Length"] = len(string_list)
		return output
