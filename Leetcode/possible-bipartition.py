class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Edge list -> Adj List
        adj_list = defaultdict(list)
        for src, des in dislikes:
            adj_list[src].append(des)
            adj_list[des].append(src)
        
        # dfs implementation
        def dfs(node):
            for neighbour in adj_list[node]:
                if color[neighbour] != 0:
                    if color[neighbour] == color[node]:
                        return False
                else:
                    if color[node] == 1:
                        color[neighbour] = -1
                    elif color[node] == -1:
                        color[neighbour] = 1
                    if not dfs(neighbour):
                        return False
            return True
                
        color = [0 for _ in range(n+1)]
        for node in adj_list:
            if color[node] == 0:
                color[node] = 1
                if not dfs(node):
                    return False
        return True
