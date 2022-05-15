class Graph:
    # initialize empty dictionary to store the vertices and edges
    def __init__(self) -> None:
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
        
    def add_edge(self, src, dest):
        # since this is an undirected graph, 
        # edge from src to dest will also be a edge from dest to source.

        if src in self.adj_list.keys() and dest in self.adj_list.keys():
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # if vertices exist without an edge, program will crash
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass

    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            # remove all the edges from v
            for other_vertex in self.adj_list[v]:
                self.adj_list[other_vertex].remove(v)

            del self.adj_list[v]

    
    def print_graph(self):
        for v in self.adj_list:
            print(v, " : ", self.adj_list[v])

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')


graph.add_edge('B', 'D')
graph.add_edge('C', 'D')


print("Added edges: ")
graph.print_graph()

graph.remove_edge('A', 'D')
graph.remove_vertex('D')
print("\n New list \n")
graph.print_graph()

