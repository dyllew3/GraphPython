class DFS(object):
	def __init__(self,graph,vertex):
		self.visited = dict()
		self.depth_first_search(graph,vertex)




	def depth_first_search(self,graph,vertex):
		self.visited[vertex] = True
		for v in graph.nodes[vertex]:
			
			if(self.visited[v] == False):
				self.depth_first_search(graph,vertex)
		pass

	def is_visited(self,vertex):
		return self.visited[vertex]
	
	pass
