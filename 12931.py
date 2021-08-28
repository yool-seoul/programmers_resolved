def solution(n):
    return sum(list(map(int, str(n))))

# 요 방법도 가능함.
    return sum([int(i) for i in str(n)])

print(solution(123) == 6)
print(solution(987) == 24)