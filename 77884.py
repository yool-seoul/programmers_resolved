def divisor(n):
    cnt = len([i for i in range(1, n+1) if n%i == 0])
    return cnt%2 == 0

def solution(left, right):
    return sum([n if divisor(n) else -n for n in range(left, right+1)])


# 약수의 개수가 홀수라면, 그 수는 제곱수라는 증명을 기반으로 한 줄 코딩.
def solution2(left, right):
    return sum([-n if int(n**0.5)==n**0.5 else n for n in range(left, right+1)])

print(solution(13, 17))
print(solution2(24, 27))
print(solution(13, 17) == 43)
print(solution2(24, 27) == 52)