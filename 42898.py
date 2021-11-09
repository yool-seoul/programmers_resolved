def solution(m, n, puddles):
    T = [[1 for _ in range(m)] for _ in range(n)]

    for pj, pi in puddles:
        T[pi-1][pj-1] = 0

    for i in range(n-1):
        if not T[i][0]:
            T[i+1][0] = 0

    for j in range(m-1):
        if not T[0][j]:
            T[0][j+1] = 0
            
    for i in range(1, n):
        for j in range(1, m):
            if T[i][j] > 0:
                T[i][j] = T[i-1][j] + T[i][j-1]

    return T[n-1][m-1] % 1000000007



print(solution(4, 3, [[2, 2]]), 4)
print(solution(2, 2, []), 2)
print(solution(3, 3, []), 6)
print(solution(3, 3, [[2, 2]]), 2)
print(solution(3, 3, [[2, 3]]), 3)
print(solution(3, 3, [[1, 3]]), 5)
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]) == 0)
print(solution(4, 4, [[3, 2], [2, 4]]) == 7)
print(solution(100, 100, []) == 690285631)