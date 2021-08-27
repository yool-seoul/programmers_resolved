def solution(arr1, arr2):
    arr3 = arr1.copy()
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr3[i][j] = arr1[i][j] + arr2[i][j]
    return arr3


# 한 줄 코딩
def solution2(A, B):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]


print(solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]])
print(solution([[1],[2]], [[3],[4]]) == [[4],[6]])

