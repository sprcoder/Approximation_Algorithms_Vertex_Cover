import integral_vc
class Linear_VC:
    def vc_linear(self, graph):
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
        integral = integral_vc.Integral_VC()
        opt_cost = integral.vc_integral(graph)
        return round(vc_cost/opt_cost, 3)