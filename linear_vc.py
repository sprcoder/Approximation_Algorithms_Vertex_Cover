import integral_vc
class LinearVC:
    """
      Class to implement Linear Programming based Rounding Algorithm for Vertex Cover
    """

    def vc_linear(self, graph):
        """
          Method to identify the vertex cover and cost generated by the Linear Programming Algorithm
          Parameter:
            Graph 
          Return:
            Ratio of total cost of vertex cover to the optimal cost generated by the Integer Program
          Logic:
            Have a varaible for each list that can have values between [0,1]
            Iterate through all the edges
              Check for the constraints for each edge Eg: e1(x1, x2) then check X1+X2>=1
              If the condition is not passed then assign the corresponding edges with 0.5 
            Vertex Cover is the vertices that has a variable with value greater than or equal to 0.5
        """
        vc_result = []
        vc_variable = [0 for i in range(len(graph.nodes))]
        for e in graph.edges:
            from_vertex = e[0]
            to_vertex = e[1]
            if (vc_variable[from_vertex] + vc_variable[to_vertex]) >= 1:
                continue
            if vc_variable[from_vertex] == 0:
                vc_variable[from_vertex] = 0.5
                vc_result.append(from_vertex)
            if vc_variable[to_vertex] == 0:
                vc_variable[to_vertex] = 0.5
                vc_result.append(to_vertex)
        # print(vc_result)
        vc_cost = 0
        for i in vc_result:
            vc_cost += graph.nodes[i]["cost"]
        integral = integral_vc.IntegralVC()
        opt_cost = integral.vc_integral(graph)
        return round(vc_cost/opt_cost, 3)