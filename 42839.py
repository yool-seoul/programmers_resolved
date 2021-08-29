from itertools import permutations as pm

def isPrime2(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return 0
    return 1

# all 내장함수 사용하여 prime 구하기 간략화.
# https://codepractice.tistory.com/87
def isPrime(num):
    return all([(num%j) for j in range(2, int(num**0.5)+1)]) and num>1
    

def solution(numbers):
    S = set()
    for i in range(1, len(numbers)+1):
        S |= set(map(int, map(''.join, pm(numbers, i))))

    print(S, '-', sum([isPrime(s) for s in S]))
    return sum([isPrime(s) for s in S])

# prime number 를 구할 때, 에라토스테네스의 체를 이용하면 Set를 활용할 수 있어서 복잡도가 낮아지고 코드도 간단해 짐.
# 근데 아래 코드는, 찾아낸 prime number 가 하나도 없을 때 max(a) 에서 에러가 나옴.
def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, pm(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

#print(isPrime(12))
print(solution('17') == 3)
print(solution('011') == 2)
print(solution('0') == 0)
print(solution('0001') == 0)
print(solution('0023') == 4)
print(solution('999') == 0)