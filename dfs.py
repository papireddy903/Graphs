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
        

    def dfs(self, start):
        def helper(node, visited, dfs_order):
            visited.add(node)
            dfs_order.append(node) 

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    helper(neighbor, visited, dfs_order)

        
        dfs_order = []

        visited = set()
        helper(start,visited,dfs_order)
        
        return dfs_order 

            


            
graph_adj_list = GraphList()
graph_adj_list.add_edge(0,1)
graph_adj_list.add_edge(0,2)
graph_adj_list.add_edge(1,2)
graph_adj_list.add_edge(0,3)

dfs_recursive_result = graph_adj_list.dfs(0)
print("DFS Traversal Order (Recursive):", dfs_recursive_result)