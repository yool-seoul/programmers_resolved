def solution(mylist):
    return [x**2 for x in mylist if x%2 == 0]

print(solution([3,2,6,7]) == [4,36])