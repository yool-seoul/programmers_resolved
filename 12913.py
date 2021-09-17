def solution(land):
    M = land[0]
    for L in land[1:]:
        N = M.copy()
        for i in range(len(M)):
            t, M[i] = M[i], 0
            N[i] = max(M) + L[i]
            M[i] = t
        M = N
    return max(M)


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]) == 16)
print(solution([[5, 1, 1, 1, 4], [5, 3, 1, 1, 1]]) == 9)
print(solution([[1,1,1,1], [2,2,2,3], [3,3,3,6], [4,4,4,7]]) == 14)