class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque([(0, 0)])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        visited.add((0, 0))
        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    if ((0 <= nr < ROWS) and
                        0 <= nc < COLS and
                            grid[nr][nc] == 0 and
                                (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            length += 1

        return -1
