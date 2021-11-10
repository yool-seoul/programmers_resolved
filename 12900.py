# 알고보니 c[2] = c[1] + c[0] 의 문제네.
def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b % 1000000007
# simple but inefficient
#from functools import reduce
#def fac(n):
#    return 1 if n == 0 else reduce(lambda x,y: x*y, list(range(1, n+1)))
def fac(n):
    if not fac.D[n]:
        for i in range(1, n+1):
            fac.D[i] = fac.D[i-1] * i
    return fac.D[n]
fac.D = [0] * 60001
fac.D[0] = fac.D[1] = 1

def com(n, r):
    return fac(n)//(fac(r)*fac(n-r))

def solution2(n):
    return sum([com(n-i, i) for i in range(1+n//2)]) % 1000000007
    

#가로의 길이 n은 60,000이하의 자연수 입니다.
#경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.
import time
s = time.time()
print(solution(1) == 1)
print(solution(2) == 2)
print(solution(3) == 3)
print(solution(4) == 5)
print(solution(5) == 8)
print(solution(6) == 13)
print(solution(7) == 21)
print(solution(10000) == 24223428)
e = time.time()
print('Elapsed time:', e-s)
