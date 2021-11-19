
class Graph:

    def __init__(self, nodes):
        self.nodes_number = nodes
        self.graph = []
        self.dist = []

    def add_link(self, from_node, to_node, way):
        self.graph.append([from_node, to_node, way])

    def print_arr(self, dist):
        for i in range(self.nodes_number):
            print(i,"   ",dist[i])

    def Bellman_Ford(self, start):

        dist = [float("Inf")] * self.nodes_number
        dist[start] = 0
        for i in range(self.nodes_number - 1):
            relaxed = True
            for from_node, to_node, way in self.graph:
                if dist[from_node] != float("Inf") and dist[from_node] + way < dist[to_node]:
                    dist[to_node] = dist[from_node] + way
                    relaxed = False
            if relaxed == True:
                break


        self.dist = dist

        for from_node, to_node, way in self.graph:
            if dist[from_node] != float("Inf") and dist[from_node] + way < dist[to_node]:
                print("Graph contains negative weight cycle")
                self.dist=[None]
                return

        self.print_arr(dist)
        print(self.graph)

if __name__ == '__main__':
    graph = Graph(5)

    graph.add_link(0, 1, -3)
    graph.add_link(0, 2, 2)
    graph.add_link(1, 2, 5)
    graph.add_link(1, 3, 4)
    graph.add_link(1, 4, 6)
    graph.add_link(3, 2, 3)
    graph.add_link(3, 1, 5)
    graph.add_link(4, 3, -2)

    graph.Bellman_Ford(0)

