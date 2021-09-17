def solution(n):
    cnt = 0
    while n > 0:
        cnt += n%2
        n //= 2
    return cnt

# best solution 이진법으로 풀면 됨.
def solution2(n):
    return bin(n).count('1')


print(solution(1) == 1)
print(solution(5) == 2)
print(solution(6) == 2)
print(solution(7) == 3)
print(solution(5000) == 5)