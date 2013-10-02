from Tkinter import *
from math import *

from network_speak import *

#
# -- Constants -- 
#

STAGE_HEIGHT = 400
STAGE_WIDTH  = 400


#
# Setup
#

master = Tk()
w = Canvas(master, width=STAGE_WIDTH, height=STAGE_HEIGHT)
w.pack()


# - - - - - - - - - - - - - - - - - - - - - - - -
#
# Drawing Methods
#

def draw_network(n_map, c_graph):
	"""
	Draws the network using Tkinter. 

	Precondition: 
	n_map is a dictionary of node elements where
	key = uid and object = Node()
	c_graph is a 2D-array of connections.
	"""
	uid_n_map 		 = prepare_n_map_for_drawing(n_map)
	uid_n_map		 = influence_to_size(uid_n_map, c_graph)
	#
	# For : draw_node_object(node)
	#
	draw_edges(c_graph, uid_n_map)
	draw_nodes(uid_n_map)

	mainloop()

def influence_to_size(uid_n_map, c_graph):
	n_width  = len(c_graph[0])
	n_height = len(c_graph)

	result = {}
	print uid_n_map

	for y in xrange(0 , n_height):
		num = 0
		for x in xrange(0, n_width):
			num = num + c_graph[y][x]
		result[y] = num
			
	for key in uid_n_map:
		size = result[key] * 4;
		uid_n_map[key].frame.size = size

	return uid_n_map
		

def prepare_n_map_for_drawing(n_map):
	'''
	Returns dictionary where objects are Node() objects
	and keys are the Node() objects' uid.

	Precondition: An n_map with Node() names as keys.
	'''

	n_nodes = len(n_map)

	y_comp  = STAGE_HEIGHT/2
	x_comp  = STAGE_WIDTH /2

	node_the =  2 * pi / float(n_nodes)
	node_dis = 50 * n_nodes / 6

	nodes_positions = [None for _ in range(n_nodes)]

	i = 0

	new_n_map = {}

	for key in n_map:

		# Set frame of nodes

		node_x = cos(node_the * i) * node_dis   + x_comp
		node_y = sin(node_the * i) * node_dis	+ y_comp
		i = i + 1

		node = n_map[key]
		node.frame.x = node_x
		node.frame.y = node_y
		node.frame.size = 10
		if node.label == '':
			node.label = node.name

		new_n_map[node.uid] = node

	return new_n_map

	

def draw_edges (c_graph, uid_n_map):

	n_width  = len(c_graph[0])
	n_height = len(c_graph)

	for y in xrange(0 , n_height):
		for x in xrange(0, n_width):
			if (c_graph[y][x] > 0):
				w.create_line(
					uid_n_map[x].frame.x, 
					uid_n_map[x].frame.y,
				 	uid_n_map[y].frame.x,
				 	uid_n_map[y].frame.y, 
				 	width=1)

def draw_nodes (uid_n_map):
	for key in uid_n_map:
		node = uid_n_map[key]
		x1 = node.frame.x - node.frame.size/2
		y1 = node.frame.y - node.frame.size/2
		x2 = node.frame.x + node.frame.size/2
		y2 = node.frame.y + node.frame.size/2

		w.create_rectangle(x1, y1, x2, y2, fill="blue")

		if node.label != '':
			draw_label(x1, y1, node.label)

def draw_label(x, y, string):
	w.create_text(x, y, text=string, anchor=E, font='Helvetica')

def draw_axes():
	w.create_line(0, STAGE_HEIGHT/2, STAGE_WIDTH, STAGE_WIDTH /2)
	w.create_line(STAGE_WIDTH/2,  0, STAGE_WIDTH/2, STAGE_HEIGHT)


if __name__ == '__main__':
	def work_network(string):

		cpath = c_path_from_string(string)
		nmap  = map_node_list(get_node_names(c_path_from_string(string)))
		c_matrix = c_graph_from_connection_path_and_map(cpath, nmap)

		draw_network(nmap, c_matrix)
	
	
	NETWORK 	 = "A.S.A.D.A.F.A.G.A.H.D.E.F.E.R.T.Q.W.D.S.E.F.R.T"
	
	work_network(NETWORK)






