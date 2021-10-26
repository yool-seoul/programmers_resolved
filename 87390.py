def solution(n, left, right):
    return [max(v//n, v%n)+1 for v in range(left, right+1)]



print(solution(3, 2, 5) == [3,2,2,3])
print(solution(4, 7, 14) == [4,3,3,3,4,4,4,4])