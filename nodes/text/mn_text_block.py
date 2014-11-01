import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodeTreeChanged, allowCompiling, forbidCompiling
from mn_utils import *

def updateNode(node, context):
	nodeTreeChanged()

class mn_Text_block(Node, AnimationNode):
	bl_idname = "mn_Text_block"
	bl_label = "Text block"

	def get_text_menu_items(self, context):
		text_items = []
		for txt in bpy.data.texts:
			text_items.append((txt.name, txt.name, ""))
		if len(text_items) == 0: text_items.append(("NONE", "NONE", ""))
		return text_items

	txt_blocks_menu = bpy.props.EnumProperty(name = "Text block", items = get_text_menu_items)
	
	def init(self, context):
		forbidCompiling()
		self.outputs.new("mn_StringSocket", "output")
		allowCompiling()
	
	def draw_buttons(self, context, layout):
		layout.prop(self, "txt_blocks_menu")

	def execute(self, input):
		text = self.txt_blocks_menu
		
		if text == "NONE": return ""

		output_string = ''
		for line in bpy.data.texts[text].lines:
			output_string = output_string + '\n' + line.body
		
		output = {}
		output["output"] = output_string
		return output
