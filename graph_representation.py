class GraphList:   # Adjancency List
    def __init__(self):
        self.graph = {}


    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = [] 
        
        if node2 not in self.graph[node1]:
            self.graph[node1].append(node2) 

    
        if node2 not in self.graph:
            self.graph[node2] = []

        if node1 not in self.graph[node2]:
            self.graph[node2].append(node1)
    
    def display(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}") 

class GraphMatrix:  # Adjacency Matrix
    def __init__(self, nodes):
        self.nodes = nodes 
        self.n = len(nodes)
        self.graph = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self,node1,node2):
        i = self.nodes.index(node1) 
        j = self.nodes.index(node2) 
        self.graph[i][j] = 1 
        self.graph[j][i] = 1 
    
    def display(self):
        for i, row in enumerate(self.graph):
            print(self.nodes[i], row)



graph_adj_list = GraphList()
graph_adj_list.add_edge('A', 'B')
graph_adj_list.add_edge('A', 'C')
graph_adj_list.add_edge('B', 'D')
graph_adj_list.add_edge('B', 'E')
graph_adj_list.add_edge('C', 'F')
graph_adj_list.add_edge('E', 'F')

graph_adj_list.display()


nodes = ['A', 'B', 'C', 'D', 'E', 'F']
graph_adj_matrix = GraphMatrix(nodes)
graph_adj_matrix.add_edge('A', 'B')
graph_adj_matrix.add_edge('A', 'C')
graph_adj_matrix.add_edge('B', 'D')
graph_adj_matrix.add_edge('B', 'E')
graph_adj_matrix.add_edge('C', 'F')
graph_adj_matrix.add_edge('E', 'F')

graph_adj_matrix.display()

