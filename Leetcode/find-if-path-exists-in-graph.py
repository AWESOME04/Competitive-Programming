class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            # base case
            if node == destination:
                return True

            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    if found:
                        return True
            return False   

        graph = {i: [] for i in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited_set = set()
        return dfs(source, visited_set)
