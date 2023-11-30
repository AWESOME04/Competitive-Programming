class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bomb(grid, m, n, i, j):
            if i < n and j < m and i >= 0 and j >= 0:
                if grid[j][i] == "1":
                    grid[j][i] = "2"
                    bomb(grid, m, n, i + 1, j)
                    bomb(grid, m, n, i - 1, j)
                    bomb(grid, m, n, i , j + 1)
                    bomb(grid, m, n, i , j - 1)
            return
        r = 0 
        m = len(grid)
        n = len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    r = r + 1
                    bomb(grid, m, n, x, y)
        return r
