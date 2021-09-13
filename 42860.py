def solution(name):
    # ord('A') : 65, ord('N') : 78, ord('Z') : 90
    v = [0, 0, 0]
    s = j = v2 = m = mi = 0
    L = len(name)
    for i in range(L):
        s += 13 - abs(ord(name[i]) - 78)
        if i >= 1:
            if name[i] == 'A':
                v[j] += 1
                v2 += 1
                m, mi = (v2, i) if m < v2 else (m, mi)
            else:
                j=1
                v[1] = 0
                m, mi = (v2, i) if m < v2 else (m, mi)
                v2 = 0
    
    v[2] = m * 2 - mi

    return s - max(v) + L - 1



print(solution('JEROEN') == 56)
print(solution('JAN') == 23)
print(solution('BAAAAB') == 3)
print(solution('AAB') == 2)
print(solution('ABBBBAA') == 8)
print(solution('AABBBAA') == 7)
print(solution('ABABAAAAAAABA') == 11)
