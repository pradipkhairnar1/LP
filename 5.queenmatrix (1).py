n = 8
board = [[0]*n for _ in range(n)]

def safe(r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False
        if c-(r-i) >= 0 and board[i][c-(r-i)] == 1:
            return False
        if c+(r-i) < n and board[i][c+(r-i)] == 1:
            return False
    return True

def solve(r):
    if r == n:
        return True

    for c in range(n):
        if safe(r, c):
            board[r][c] = 1
            if solve(r+1):
                return True
            board[r][c] = 0
    return False

# First queen placed at row 0, column 0
board[0][0] = 1

if solve(1):
    for row in board:
        print(row)
else:
    print("No solution")