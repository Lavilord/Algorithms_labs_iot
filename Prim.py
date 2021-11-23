class Graph:

    def __init__(self, nodes):
        self.nodes_number = nodes
        self.graph = []
        self.visited = []
        self.new_graph = []

    def add_link(self, node_1, node_2, way):
        self.graph.append([node_1, node_2, way])

    def add_link_to_new_graph(self, link):
        self.new_graph.append(link)

    def Prim(self,start):
        self.visited.append(start)
        while len(self.visited) < self.nodes_number:
            self.add_link_to_new_graph(self.compare(self.search_links()))


    def search_links(self):
        links_to_compare = []
        for node_1, node_2, way in self.graph:
            if node_1 in self.visited and node_2 not in self.visited:
                links_to_compare.append([node_1,node_2,way])

            if node_2 in self.visited and node_1 not in self.visited:
                links_to_compare.append([node_1,node_2,way])


        return links_to_compare

    def compare(self,links_to_compare):
        min_way= float("Inf")
        for node_1, node_2, way in links_to_compare:
            if min_way == float("Inf") or way < min_way:
                min_way = way

        for node_1, node_2, way in links_to_compare:
            if min_way == way:
                if node_1 not in self.visited:
                    self.visited.append(node_1)
                if node_2 not in self.visited:
                    self.visited.append(node_2)
                return [node_1, node_2, way]


if __name__ == '__main__':
    graph = Graph(9)

    graph.add_link(0,1,4)
    graph.add_link(0,7,8)
    graph.add_link(1,7,11)
    graph.add_link(1,2,8)
    graph.add_link(7,8,7)
    graph.add_link(7,6,1)
    graph.add_link(2,8,2)
    graph.add_link(8,6,6)
    graph.add_link(6,5,2)
    graph.add_link(2,5,4)
    graph.add_link(2,3,7)
    graph.add_link(3,5,14)
    graph.add_link(3,4,9)
    graph.add_link(5,4,10)

    graph.Prim(0)
    print(graph.graph)
    print(graph.new_graph)




