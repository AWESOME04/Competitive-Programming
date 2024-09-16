class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == "X":
                    if (i == 0 or board[i-1][j] == ".") and \
                        (j == 0 or board[i][j-1] == "."):
                        res += 1
        return res
