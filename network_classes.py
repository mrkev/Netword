from network_base import *
from random import *

class Node(object):
	"""docstring for Node"""

	uid  = 0
	name = ''
	label = ''

	def __init__(self, node_uid, node_name):
		super(Node, self).__init__()

		self.uid  = node_uid
		self.name = node_name

		self.frame = Frame(0,0,0,0)


class Frame(object):
	"""docstring for Frame"""

	def size():
	    doc = "The size property."
	    def fget(self):
	        return self._size
	    def fset(self, value):
	        self._size = value
	        self.w = value
	        self.h = value
	    def fdel(self):
	        del self._size
	    return locals()
	
	size = property(**size())
	
	def __init__(self, x, y, w, h):
		super(Frame, self).__init__()
		self.x = x
		self.y = y
		self.w = w
		self.h = h


class CGraph(object):
	"""docstring for CGraph"""

	_graph = []

	def __init__(self, matrix=[]):

		super(CGraph, self).__init__()
		if len(matrix) == 0:
			pass
		self._graph = matrix

	def __iter__():
		pass
	
	def normalize(self):

		_graph = self._graph
		print self._graph

		n_width  = len(_graph[0])
		n_height = len(_graph)
	
		for y in xrange(0 , n_height):
			for x in xrange(0, n_width):
				if _graph[y][x] == _graph[x][y]:
					_graph[x][y] = 0
	
				if y == x:
					_graph[y][x] = 0
		
		self._graph = _graph

	def generate_with_size(self, size):
		self._graph = [[0 for _ in range(size)] for _ in range(size)]

	def generate_rand_with_size(self, size):
		self._graph = [[randint(0,1) for _ in range(size)] for _ in range(size)]

	def generate_solid_with_size(self, size):
		self._graph = [[1 for _ in range(size)] for _ in range(size)]


if __name__ == '__main__':

	thing = [[1,1,1],
			 [1,1,1], 
			 [1,1,1]]
	
	graph = CGraph()
	graph.generate_rand_with_size(10)
	
	print_matrix(graph._graph)
	
	



