def solution(n, t, m, p):
    N = list('0123456789ABCDEF')
    S = '0'
    i = 0
    while len(S) < t*m:
        c = ''
        j = i
        while j > 0:
            c += N[j%n]
            j = j//n
        S += c[::-1]
        i+=1
    return S[p-1::m][:t]

# string 을 변수로 선언할 때, 위의 방식처럼 간단히 적어주어도 됨.


def solution2(n, t, m, p):
    N = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    S = '0'
    for i in range(t*m*2):
        c = ''
        while i > 0:
            c += N[i%n]
            i = i//n
        S += c[::-1]
        if len(S) >= t * m:
            break

    S2 = ''
    for i in range(len(S)):
        if i%m == p - 1:
            S2 += S[i]
        if len(S2) == t:
            break
    return S2


print(solution(2, 6, 2, 1) == "011100")
print(solution(16, 16, 2, 1) == "02468ACE11111111")
print(solution(16, 16, 2, 2) == "13579BDF01234567")
print(solution(3, 12, 3, 2) == '101020001112')