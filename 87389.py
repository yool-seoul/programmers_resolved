def solution(n):
    for i in range (2, int(n**0.5)+1):
        if (n-1) % i == 0:
            return i
    return n-1

# 다른 풀이법
def solution2(n):
    return  min([x for x in range(1, n+1) if n % x == 1])

print(solution(10) == 3)
print(solution(12) == 11)
print(solution(9) == 2)
print(solution(36) == 5)