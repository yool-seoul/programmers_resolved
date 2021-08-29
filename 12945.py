def solution(n):
    p1 = 0
    p2 = 1
    for _ in range(2, n):
        p1, p2 = p2, p1+p2
    return (p1+p2)%1234567

def solution2(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a

print(solution2(1) == 1)
print(solution2(2) == 1)
print(solution2(3) == 2)
print(solution2(5) == 5)
print(solution2(6) == 8)