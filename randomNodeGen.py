import networkx as nx
import matplotlib.pyplot as plt
from numpy import random
import greedy_vc, pricing_vc, linear_vc
import pprint

def random_graph_gen(n, p):   
  """
    Method that generates random graph using erdos renyi random graph generation from the networkx library.
    The cost of the vertices are uniformly sampled from [0,1]. Used numpy to generate uniform random values
    The erdos_renyi_graph takes 2 parameters. 
    n -> no.of Parameters & p -> probability of an edge occuring between a pair of nodes.
  """
  graph = nx.erdos_renyi_graph(n, p) # Edges prob can be calculated by the logic E = p(n(n-1)/2)
  vertex_cost = random.uniform(0.0,1.0, n)
  iter = 0
  vertex_dict = {}
  for item in vertex_cost:
    vertex_dict[iter] = item
    iter += 1
  nx.set_node_attributes(graph, vertex_dict, name="cost")
  # Uncomment below code to visualize the graph generated
  # nx.draw(graph, with_labels=True)
  # plt.show()
  return graph

if __name__ == "__main__":
  """
    Main logic execution
    With various values of n & p, generates m graphs
    For each graph generated, identifies the vertex cost generated by 3 different algorithms
      Greedy, Pricing and LP-Based Rounding Algorithms
    Each algorithm retuns a ratio 
      The total cost it generated to the optimal cost generated 
      by the Integral Progam for Vertex Cover
    
    Result shows the ratio generated algorithms for each pair of parameters involved.
  """
  greedy = greedy_vc.GreedyVC()
  pricing = pricing_vc.PricingVC()
  linear = linear_vc.LinearVC()

  # Parameter values
  n_val = [100, 120, 140, 160, 180, 200]
  p_val = [0.1, 0.2, 0.3, 0.4, 0.5]
  m = 200
  # Dictionary to store the values
  avg_ratio = {}
  # Graph list for storing graphs generated by the random graph method
  m_graph = []
  for i in n_val:
    avg_ratio[i] = {}
    for j in p_val:
      avg_ratio[i][j] = {}
      avg_ratio[i][j]["greedy"] = []
      avg_ratio[i][j]["pricing"] = []
      avg_ratio[i][j]["linear"] = []
      greedy_ratio = 0
      pricing_ratio = 0
      linear_ratio = 0
      for m_count in range(0, m):
        m_graph.append(random_graph_gen(i, j))
      for g_item in m_graph:
        greedy_ratio += greedy.printVertexCover(g_item)
        pricing_ratio += pricing.vc_pricing(g_item)
        linear_ratio += linear.vc_linear(g_item)
      avg_ratio[i][j]["greedy"].append(round(greedy_ratio/m,3))
      avg_ratio[i][j]["pricing"].append(round(pricing_ratio/m,3))
      avg_ratio[i][j]["linear"].append(round(linear_ratio/m,3))

      # Reset the graph list
      m_graph = []

  pp = pprint.PrettyPrinter(indent=2)
  pp.pprint(avg_ratio)
