class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(r, c, k):
            for i in range(0,9):
                if board[r][i] == k:
                    return False
                if board[i][c] == k:
                    return False
                if board[(r//3)*3 + i//3][3*(c//3) + i%3] == k:
                    return False
            return True

        def solve(r, c):
                if r == 9:
                    return True
                if c == 9:
                    return solve(r + 1, 0)
                if board[r][c] == ".":
                    for k in range(1, 10):
                        if check(r, c, str(k)) == True:
                            board[r][c] = str(k)
                            if solve(r, c+1):
                                return True
                            board[r][c] = "."
                    return False
                return solve(r, c + 1)

        solve(0, 0)
