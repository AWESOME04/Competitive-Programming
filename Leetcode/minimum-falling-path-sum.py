class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        for r in range(1, N):
            for c in range(N):
                mid = matrix[r-1][c]
                left = matrix[r-1][c-1] if c > 0 else float("inf")
                right = matrix[r-1][c+1] if c < N-1 else float("inf")
                matrix[r][c] = matrix[r][c] + min(mid, left, right)
        return min(matrix[-1])
