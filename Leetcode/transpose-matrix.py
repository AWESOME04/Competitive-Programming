class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for num in range(len(matrix[0])):
                ans[num][row] = matrix[row][num]

        return ans
