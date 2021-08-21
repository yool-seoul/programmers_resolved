def solution(board, moves):
    q = [0]
    answer = 0
    for i in moves:
        for j in range(len(board[0])):
            v = board[j][i-1]
            if v != 0:
                if q[-1] == v:
                    q.pop()
                    answer += 2
                else:
                    q.append(v)
                board[j][i-1] = 0
                break
    return answer