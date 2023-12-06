class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] != 0:
                    adj_list[i].append(j)

        visited = set()
        def dfs(i, j):
            if(i < 0 or i == rows or j < 0 or j == cols or (i, j) in visited or not isConnected[i][j]):
                return
            
            visited.add((i, j))

            return(dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1))
            
            
        provinces = 0

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j):
                    provinces += 1

        return provinces
