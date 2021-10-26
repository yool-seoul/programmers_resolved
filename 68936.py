def solution(arr):
    n = len(arr)
    r = sum([arr[i].count(1) for i in range(n)])

    if r == 0:
        return [1, 0]
    elif r == n*n:
        return [0, 1]
    elif n == 2:
        r = arr[0].count(0) + arr[1].count(0)
        return [r, 4-r]
    else:
        R = [[0, 0, 0, 0], [0, 0, 0, 0]]
        for k in range(4):
            n2 = n//2
            M = [[0] * n2] * n2
            for i in range(n2):
                M[i] = arr[i+(k%2)*n2][(k//2)*n2:(1+k//2)*n2]
            R[0][k], R[1][k] = solution(M)
        return [sum(R[0]), sum(R[1])]




print(solution([[0,0], [0,0]]) == [1, 0])
print(solution([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == [0,1])
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4,9])
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10,15])
