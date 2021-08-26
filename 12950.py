def solution(arr1, arr2):
    arr3 = [i+j for i, j in zip(arr1, arr2)]

    print(arr3)
    return arr3


    

print(solution([[1,2],[3,4]], [[3,4],[5,6]]) == [[4,6],[7,9]])
print(solution([[1],[2]], [[3],[4]]) == [[4],[6]])