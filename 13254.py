def solution(mylist):
    return [len(m) for m in mylist]



# 아래와 같은 방식도 가능
solution = lambda my_list: list(map(len,my_list))

print(solution([[1], [2]]) == [1,1])
print(solution([[1, 2], [3, 4], [5]]) == [2,2,1])