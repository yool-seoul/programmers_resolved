def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sum = 0
    for i, j in zip(A, B):
        sum += i*j
    return sum


# 한 줄 코딩
def solution2(A, B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))


print(solution2([1,4,2], [5,4,4]) == 29)
print(solution2([1,2], [3,4]) == 10)