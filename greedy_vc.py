import integral_vc

class VC_Graph:

	def printVertexCover(self, graph):

		# Initialize all vertices as not visited.
		visited = [False] * len(graph.nodes)
		vc_cost = 0
		# Consider all edges one by one
		for u in sorted(graph.nodes(), key=lambda n: graph.nodes[n]['cost']):
			if not visited[u]:
				for v in graph.neighbors(u):
					if not visited[v]:
						visited[v] = True
						visited[u] = True
						break
    # Print the vertex cover

		for j in range(len(graph.nodes)):
			if visited[j]:
				vc_cost += graph.nodes[j]["cost"]
		integral = integral_vc.Integral_VC()
		opt_cost = integral.vc_integral(graph)
		return round(vc_cost/opt_cost, 3)
    
