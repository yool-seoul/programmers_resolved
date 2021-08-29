def solution(arr1, arr2):
    I, J, K = len(arr1), len(arr2[0]), len(arr2)
    arr3 = [[0] * J for _ in range(I)]

    for i in range(I):
        for j in range(J):
            arr3[i][j] = 0
            for k in range(K):
                arr3[i][j] += arr1[i][k] * arr2[k][j]
    return arr3


# one line coding
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
            == [[15, 15], [15, 15], [15, 15]])
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) 
            == [[22, 22, 11], [36, 28, 18], [29, 20, 14]])