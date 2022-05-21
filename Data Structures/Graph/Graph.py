# Directed Graph implementation using Linked lists

from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices) -> None:
        self.vertices = vertices # total number of vertices
        self.array = [] # This array holds multiple linkedlists equal to the number of veritces 

        # Create new Linked list for each vertex
        for _ in range(vertices):
            self.array.append(LinkedList())


    # Add edge from source to destination

    def add_edge(self, source, dest):
        if source < self.vertices and dest < self.vertices:
            self.array[source].insert_at_head(dest)

    def print_graph(self):
        print("Adjacency List of Directed Graph")
        for i in range(self.vertices):
            print("|",i, end= "| =>")
            temp = self.array[i].get_head()

            while temp is not None:
                print("[",temp.value,end ="]->")
                temp = temp.next
            print("None")


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()