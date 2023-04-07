
class Integral_VC:
    def vc_integral(self, graph):
        vc_result = []
        vc_variable = [0 for i in range(len(graph.nodes))]
        for e in graph.edges:
            from_vertex = e[0]
            to_vertex = e[1]
            if (vc_variable[from_vertex] + vc_variable[to_vertex]) >= 1:
                continue
            if graph.nodes[from_vertex]["cost"] < graph.nodes[to_vertex]["cost"]:
                vc_variable[from_vertex] = 1
                vc_result.append(from_vertex)
            else:
                vc_variable[to_vertex] = 1
                vc_result.append(to_vertex)
        # print(vc_result)
        vc_cost = 0
        for i in vc_result:
            vc_cost += graph.nodes[i]["cost"]
        return vc_cost