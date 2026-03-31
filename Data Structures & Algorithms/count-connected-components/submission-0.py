class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei) 
        
        unconnectedGraphs = 0

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                unconnectedGraphs += 1
                dfs(node)
        
        return unconnectedGraphs
