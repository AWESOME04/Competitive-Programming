class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force - O(m * n)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False


        # O(log(m * n)) using binary search

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1 
            else:
                break
        
        if not (top <= bot):
            return False
        mid_row = (top + bot) // 2
        
        l,r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[mid_row][m]:
                l = m + 1
            elif target < matrix[mid_row][m]:
                r = m - 1
            else:
                return True

        return False
