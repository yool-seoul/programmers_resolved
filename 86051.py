def solution(numbers):
    return sum(set([0,1,2,3,4,5,6,7,8,9]) - set(numbers))

# best solution
    return 45 - sum(numbers)

print(solution([1,2,3,4,6,7,8,0]) == 14)
print(solution([5,8,4,0,6,7,9]) == 6)