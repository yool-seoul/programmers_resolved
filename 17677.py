def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    s1 = [str1[i:i+2] for i in range(0, len(str1), 2) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2]
    s1 += [str1[i:i+2] for i in range(1, len(str1), 2) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2]

    s2 = [str2[i:i+2] for i in range(0, len(str2), 2) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2]
    s2 += [str2[i:i+2] for i in range(1, len(str2), 2) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2]

    n1 = len(s1)
    n2 = len(s2)
    n3 = 0
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and s1[i] != '':
                s1[i] = s2[j] = ''
                n3 += 1

    return int((n3/(n1+n2-n3)*65536)) if n1+n2-n3 else 65536


print(solution('FRANCE', 'french') == 16384)
print(solution('handshake', 'shake hands') == 65536)
print(solution('aa1+aa2', 'AAAA12') == 43690)
print(solution('E=M*C^2', 'e=m*c^2') == 65536)