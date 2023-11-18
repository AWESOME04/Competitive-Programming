t = int(input())  # number of test cases

for _ in range(t):
    input()  # read the empty line before each test case

    board = []
    for _ in range(8):
        row = input().strip()
        board.append(row)

    # Iterate over inner cells
    for row in range(1, 7):
        for col in range(1, 7):
            if (
                board[row][col] == '#' and
                board[row-1][col-1] == '#' and
                board[row-1][col+1] == '#' and
                board[row+1][col-1] == '#' and
                board[row+1][col+1] == '#'
            ):
                bishop_row = row + 1
                bishop_col = col + 1
                break
        else:
            continue
        break

    print(bishop_row, bishop_col)
