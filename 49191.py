def solution2(n, results):
    T = [[0]*n for _ in range(n)]

    for i in range(n):
        T[i][i] = 9

    while True:
        changed = False
        for a, b in results:
            T[a-1][b-1] = 1
            T[b-1][a-1] = -1
            for i in range(n):
                if T[b-1][i] == 1:
                    if T[a-1][i] != 1:
                        T[a-1][i] = 1
                        T[i][a-1] = -1
                        changed = True
                if T[a-1][i] == -1:
                    if T[b-1][i] != -1:
                        T[b-1][i] = -1
                        T[i][b-1] = 1
                        changed = True
                    T[b-1][i] = -1
                    T[i][b-1] = 1
        if not changed:
            break
    return n - sum([1 if 0 in T[i] else 0 for i in range(n)])


# default dict 이용한 풀이
from collections import defaultdict
def solution(n, results):
    win, lose = defaultdict(set), defaultdict(set)
    for w, l in results:
        lose[l].add(w)
        win[w].add(l)

    for i in range(1, n+1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer


# 선수의 수는 1명 이상 100명 이하입니다.
# 경기 결과는 1개 이상 4,500개 이하입니다.
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(4, [[1,2],[2,3],[3,4]]), 4)
print(solution(4, [[1,2],[2,3],[2,4]]), 2)
