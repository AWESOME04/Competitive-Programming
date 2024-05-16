class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = defaultdict(int)
        count = 0

        for row in grid:
            res[tuple(row)] += 1

        for col in zip(*grid):
            count += res[tuple(col)]

        return count
