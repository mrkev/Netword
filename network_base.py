from math import *

#
# For Debugging
#

def print_matrix(matrix):
	"""
	Prints a niceley laid out matrix

	Precondition: matrix is a square 
	list of lists. 

	Works best if len(matrix) < 100 
	and items are single digit.
	"""
	print ''
	s = ' ' if len(matrix) < 10 else '  '
	for i in xrange(0, len(matrix)):
		_ = '  ' if i < 10 else ' '
		s = s + _ + str(i)
	print s

	for i in xrange(0, len(matrix)):
		_ = ' ' if 	len(matrix) < 10 else '  '
		_ = _ if i < 10 else ' '
		print str(i) + _ + str(matrix[i])
		pass
	print ''

#
# Matrix Generators / Operations
#

def generate_e_matrix(size):
	return [[randint(0,1) for _ in range(size)] for _ in range(size)]

def generate_n_matrix(size):
	return [(random() + 1) for _ in range(size)]

def generate_solid_e_matrix(size):
	return [[1 for _ in range(size)] for _ in range(size)]

def n_matrix_from_connections(e_matrix):
	n_size = len(e_matrix)
	#print_matrix(e_matrix)

	m = [0 for _ in range(len(e_matrix))]
	for y in xrange(0 , len(e_matrix[0])):
		for x in xrange(0, n_size):
			m[y] = m[y] + e_matrix[y][x]
			m[x] = m[x] + e_matrix[y][x]

	for i in xrange(0, len(m)):
		m[i] = m[i] / (n_size / 2.0)

	#print str(m)
	return m

def normalized_e_graph(e_graph):

	c_graph = e_graph

	n_width  = len(c_graph[0])
	n_height = len(c_graph)

	for y in xrange(0 , n_height):
		for x in xrange(0, n_width):
			if c_graph[y][x] == c_graph[x][y]:
				c_graph[x][y] = 0

			if y == x:
				c_graph[y][x] = 0
	
	return c_graph
