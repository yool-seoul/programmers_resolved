def solution(s):
    L1 = L2 = 0
    while s != '1':
        L = s.count('1')
        L1 += 1
        L2 += len(s) - L
        s = bin(L)[2:]

    return [L1, L2]

print(solution("110010101001") == [3,8])
print(solution("01110") == [3,3])
print(solution("1111111") == [4,1])