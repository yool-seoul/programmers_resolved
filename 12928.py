def solution(n):
#    return sum([i for i in range(1, n+1) if n%i == 0])

# for loop 의 범위를 줄이면 성능 향상됨. 
    return n + sum([i for i in range(1, (n//2) + 1) if n%i == 0])

print(solution(12) == 28)
print(solution(5) == 6)