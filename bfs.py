from collections import deque 

class GraphList:
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


    def bfs(self, start):
        visited = set()

        queue = deque([start]) 

        bfs_order = [] 

        while queue:
            node = queue.popleft() 

            if node not in visited:
                visited.add(node) 
            
                bfs_order.append(node) 

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
            
        return bfs_order 

            

        




graph_adj_list = GraphList()
graph_adj_list.add_edge('A', 'B')
graph_adj_list.add_edge('A', 'D')
graph_adj_list.add_edge('B', 'C')
graph_adj_list.add_edge('B', 'E')
graph_adj_list.add_edge('C', 'E')
graph_adj_list.add_edge('E', 'D')

print(graph_adj_list.bfs('A'))
