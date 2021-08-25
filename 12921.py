import time
import math
def isPrime(n):
    for i in range(3, int(math.sqrt(n)+1), 2):  # sqrt 대신에 **0.5 이렇게 0.5 제곱해도 됨.
        if n % i == 0:
            return 0
    return 1

# N이 천만일 때, time : 44.72360610961914
def solution(N):
    return sum([isPrime(n) for n in range(3, N+1, 2)]) + 1    # condition: n >= 2


# 에라토스테네스의 체
# N이 천만일 때, time : 3.7364108562469482
def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(i*i,n+1,i))
    return len(num)


# print(solution(1) == 0)    # out of condition
print(solution(2) == 1)
print(solution(3) == 2)
print(solution(4) == 2)
print(solution(10) == 4)
print(solution(5) == 3)
print(solution(996) == 167)
print(solution(997) == 168)
print(solution(1000) == 168)
print(solution(10000) == 1229)
print(solution2(100000) == 9592)

start = time.time()  # 시작 시간 저장
#print(solution2(1000000) == 78498)
print(solution(10000000) == 664918)
#print(solution2(100000000) == 5762209)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간