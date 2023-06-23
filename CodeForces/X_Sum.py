def calculate_max_sum(n, m, board):
    max_sum = 0
    for i in range(n):
        for j in range(m):
            current_sum = board[i][j]  

            r, c = i + 1, j + 1
            while r < n and c < m:
                current_sum += board[r][c]
                r += 1
                c += 1
            
            r, c = i - 1, j - 1
            while r >= 0 and c >= 0:
                current_sum += board[r][c]
                r -= 1
                c -= 1
            
            r, c = i + 1, j - 1
            while r < n and c >= 0:
                current_sum += board[r][c]
                r += 1
                c -= 1
            
            r, c = i - 1, j + 1
            while r >= 0 and c < m:
                current_sum += board[r][c]
                r -= 1
                c += 1
            max_sum = max(max_sum, current_sum)
    return max_sum


# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, m = map(int, input().split())

    # Read the chessboard values
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)

    # Calculate and print the maximum sum
    max_sum = calculate_max_sum(n, m, board)
    print(max_sum)
