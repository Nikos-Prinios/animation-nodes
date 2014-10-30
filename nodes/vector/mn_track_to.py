def draw_buttons(self, context, layout):
		col = layout.column(align = True)
			
		row = col.row(align = True)
		row.label("Axis")
		row.prop(self, "axis", index = 0, text = "x")
		row.prop(self, "axis", index = 1, text = "y")
		row.prop(self, "axis", index = 2, text = "z")


	def angle(self,target_x,object_x,target_y,object_y,i,offset):

		if target_y < object_y:
			i *= -1
			
		result = (math.acos((target_x-object_x)/math.sqrt((target_x-object_x)**2 + (target_y-object_y)**2)) * i) + offset
		return result

	def execute(self, input):
		
		offset = input["Offset"]
		obj = input["input"]

		output = {}
		result = [0.0,0.0,0.0]

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

		if self.axis[0]:
			result[0] = self.angle(track_y, obj_y, track_z, obj_z, 1, offset)
		if self.axis[1]:
			result[1] = self.angle(track_x, obj_x, track_z, obj_z, -1, offset)
		if self.axis[2]:
			result[2] = self.angle(track_x, obj_x, track_y, obj_y, 1, offset)
		
		output["output"] = result
		return output
