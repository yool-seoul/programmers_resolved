from itertools import permutations as pm
def solution(k, dungeons):
    M = 0
    for d in pm(dungeons):
        L = k
        D = 0
        for d1, d2 in d:
            if L >= d1:
                D += 1
                L -= d2
        if D > M:
            M = D
    return M



print(solution(80, [[80,20],[50,40],[30,10]]) == 3)