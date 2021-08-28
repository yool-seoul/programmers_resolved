def solution(n, m):
    a = {i for i in range(1, n+1) if n%i == 0}
    b = {i for i in range(1, m+1) if m%i == 0}

    lcm = max(a & b)
    gcd = int(n * m / lcm)

    return [lcm, gcd]



# best code
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))


# another solution - 유클리드 호제법 이용.
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t

    return [c, int(a*b/c)]



print(solution(3, 12) == [3, 12])
print(solution(2, 5) == [1,10])