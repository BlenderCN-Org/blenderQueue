bl_info = {
	"name": "Blender Queue",
	"author": "Patrick W. Crawford",
	"version": (1, 0),
	"blender": (2, 72, 1),
	"location": "Properties > Render",
	"description": "Render queues via command line",
	"warning": "",
	"wiki_url": "http://www.theduckcow.com",
	"category": "Render"}


import bpy, os, subprocess
from subprocess import Popen, PIPE

def renderQueue(self, context):
	
	print("hello render commandline")
	
	blendPath = bpy.path.abspath("//") # could also do bpy.data.filepath
	print("-b {x} -x 1 -a".format(x=blendPath))
	
	""" I have no idea what I'm doing (below) """
	
	#get the blender path
	
	#below shows currently open command line OR opens new if not already open
	command = ['open', '-W', '-a', 'Terminal.app']
	# and blender would return and be active once you closed the terminal (..twice. first time closed reappears)

	#command = ['open', '-W', '-a', 'Terminal.app', '~']
	#makes it do nothing. Through just terminal, will launch new window regardless at that directory
	# even adding "&" made it work as I wanted!!!!!! ie in terminal: "open -W -a Terminal.app ~/Desktop &"
	# opened a new terminal window at said directory, but original process would keep going
	
	#subprocess.call(command)
	#below won't freeze blender, but then can't see shell
	#subprocess.Popen(command, creationflags=0x00000008)
	# yay! windows only -_-
	
	# will NOT freeze blender! popen is the proper way to do background...
	# but same deal, if terminal already open just brings that forward..
	
	#os.system("start cmd /K dir")
	
	# below works on command line (mac at least), but not through python so far
	#command = ['open', '-a', 'Terminal', "`pwd`"]
	#command = []
	"""
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, err = p.communicate(b"")
	rc = p.returncode
	"""


class RENDER_queue(bpy.types.Operator):
	"""Command Line Render start"""
	bl_idname = "render.queue"
	bl_label = "Command Line"
	#bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):

		renderQueue(self, context)

		return {'FINISHED'}


# This allows you to right click on a button and link to the manual
"""
def add_object_manual_map():
	url_manual_prefix = "http://www.theduckcow.com"
	url_manual_mapping = (
		("bpy.ops.mesh.add_object", "Modeling/Objects"),
		)
	return url_manual_prefix, url_manual_mapping
"""

def render_panel(self, context):

	#layout = self.layout
	
	#add the two buttons here!
	self.layout.operator(
		RENDER_queue.bl_idname,
		text="Render Queue",
		icon='CONSOLE')

	#the list of queue'd objects, via text file
	"""
	ob = context.object
	group = ob.vertex_groups.active

	rows = 2
	if group:
		rows = 4
	row = layout.row()
	row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=rows)

	col = row.column(align=True)
	col.operator("object.vertex_group_add", icon='ZOOMIN', text="")
	col.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
	col.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
	if group:
		col.separator()
		col.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
		col.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

	if ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex)):
		row = layout.row()

		sub = row.row(align=True)
		sub.operator("object.vertex_group_assign", text="Assign")
		sub.operator("object.vertex_group_remove_from", text="Remove")

		sub = row.row(align=True)
		sub.operator("object.vertex_group_select", text="Select")
		sub.operator("object.vertex_group_deselect", text="Deselect")

		layout.prop(context.tool_settings, "vertex_group_weight", text="Weight")
	"""


def register():
	bpy.utils.register_class(RENDER_queue)
	try:
		bpy.types.RENDER_PT_render.remove(render_panel)
	except:
		print("oh well")
	bpy.types.RENDER_PT_render.append(render_panel)
	
	
	#bpy.utils.register_manual_map(add_object_manual_map)
	#bpy.types.INFO_MT_mesh_add.append(add_object_button)


def unregister():
	bpy.utils.unregister_class(RENDER_queue)
	bpy.types.RENDER_PT_render.remove(render_panel)
	
	#bpy.utils.unregister_manual_map(add_object_manual_map)
	#bpy.types.INFO_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
	register()
