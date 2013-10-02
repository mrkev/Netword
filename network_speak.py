'''ATM->	Will have to make c_graph_from_string for each statement, and 
		combinde it all into a single c_graph'''

from network_base  import *
from network_classes import *

def clean_number(string):
	tmp = list(string)
	to_kill = []
	allowed = ['1','2','3','4','5','6','7','8','9','0','.']

	for i in xrange(0,len(tmp)):
		if tmp[i] not in allowed :
			# Apparently killing them in the moment causes problems. Python's
			# for-in loops break the progression when you take items out as it
			# is iterating.
			to_kill.append(tmp[i])

	for c in to_kill:
		tmp.remove(c)

	return ''.join(tmp)

def c_graph_from_string(string):
	c_string = '.' 			# String marking connections
	s_string = '/'			# String marking separations
	m_string = ['(', ')']	# String marking magnitudes
	l_string = ['*', '*']	# String marking labels
	g_string = ['[', ']']	# String marking groups

	#elem 	 = full_partition(string, c_string)
			   # Description of all elements, in order of connection. May repeat nodes.

	nc_path  = c_path_from_string(string)
			   # The path to connect. Named Connection path.
	print 'nc_path ' + str(nc_path)

	node_map =  map_node_list(get_node_names(nc_path))
			   # Makes node names a key that return a unique id number, using the list's order.
	print 'node map ' + str(node_map)

	c_graph = c_graph_from_connection_path_and_map(nc_path, node_map)

	print_matrix(c_graph)

	return c_graph

def c_graph_from_connection_path_and_map(nc_path, node_map):
	
	# Create c_graph
	c_graph = [[0 for _ in range(len(node_map))] for _ in range(len(node_map))]

	for i in xrange(0,len(nc_path)-1): #Iterate through dictionary
		src_node_c_coordinate = node_map[nc_path[i][0]].uid
		dst_node_c_coordinate = node_map[nc_path[i+1][0]].uid
		
		#print str(i) + ': ' + str(src_node_c_coordinate) + ' & ' + str(dst_node_c_coordinate)

		# Find point x, y on c_graph and mark a connection.
		c_graph[src_node_c_coordinate][dst_node_c_coordinate] = 1

		#print str(node_map[nc_path[i]]) + '->' + str(node_map[nc_path[i+1]])

	return c_graph


def pop_contents_inside_chars(string, a_char, b_char):
	result = string
	a_pos  = string.find(a_char)
	b_pos  = string.find(b_char)
	
	if a_pos > 0 and b_pos > 0:
		result = result[a_pos:b_pos-1]

	return result


def map_node_list(node_names):
	'''
	Returns dictionary where the key is the node name of a node
	and the object is the Node instance itself.

	Precondition: A list of strings (node names)
	'''
	result = {}
	for i in xrange(0, len(node_names)):
		if node_names[i] not in result:
			node_id 	= len(result)
			node_name 	= node_names[i]
			node 		= Node(node_id, node_name)

			result[node_names[i]] = node

	return result

def get_node_names(node_list):
	''' Returns: List of strings

	Summary: Extracts node names from list of element paths

	(Longer summary)

	Value Returned is of type list

	Precondition: el_list is list of strings or shallow lists.
	'''
	n_list = node_list
	
	for i in xrange(0,len(n_list)):
		if type(n_list[i]) is list:
			n_list[i] = n_list[i][0]

	return n_list

def full_partition(string, d):
	if string.find(d) < 0:
		return string

	parts = string.split(d)

	for i in xrange(0, len(parts)):
		parts[i] = full_partition(parts[i], '*')

	return parts

def c_path_from_string(string):
	result = full_partition(string, '.')
	for i in xrange(0,len(result)):
		result[i] = [result[i]]
	return result

#
# Tests
#

if __name__ == '__main__':
	#from KCtests import *
	#s = 'A.B   C.D [E.F G].C '
	cpath = c_path_from_string('[string.lol].two.hello')
	nmap  = map_node_list(get_node_names(c_path_from_string('string.lol.two.hello')))
	print cpath
	print nmap
	print_matrix(c_graph_from_connection_path_and_map(cpath, nmap))






