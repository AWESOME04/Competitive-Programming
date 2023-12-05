class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c):
            # base case
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
                
            visited.add((r, c))

            # recursive call
            return 1+ dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        tot_area = 0
        for i in range(rows):
            for j in range(cols):
                tot_area = max(tot_area, dfs(i,j))
        
        return tot_area
