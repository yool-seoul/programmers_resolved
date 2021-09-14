# correct approach but inefficient.
def solution2(board):
    w, h = len(board[0]), len(board)
    for i in range(min(w, h), 1, -1):
        for j in range(w-i+1):
            for k in range(h-i+1):
                sum = 0
                for a in range(j, j+i):
                    for b in range(k, k+i):
                        sum += board[b][a]
                if sum == i**2:
                    return sum
    for i in range(h):
        if 1 in board[i]:
            return 1
    return 0

# O(n^2) 솔루션
def solution(board):
    w, h = len(board[0]), len(board)
    m = 0
    if w <= 1 or h <= 1:
        for i in range(h):
            if 1 in board[i]:
                return 1
    else:
        for i in range(1, h):
            for j in range(1, w):
                if board[i][j] == 1:
                    board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                    m = board[i][j] if m < board[i][j] else m    
    return m*m

print(solution2([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9)
print(solution2([[0,0,1,1],[1,1,1,1]]) == 4)
print(solution2([[1]]) == 1)
print(solution2([[0, 0, 1, 0]]) == 1)
print(solution2([[0], [0], [1], [0]]) == 1)
print(solution2([[0], [0], [0], [0]]) == 0)
print(solution2([[0]]) == 0)