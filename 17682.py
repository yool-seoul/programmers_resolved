def solution(dartResult):
    b = {'S': 1, 'D': 2, 'T': 3}
    p = [0, 0, 0]
    i = 0

    dartResult = dartResult.replace('10', 'A')
    for c in dartResult:
        if c == 'A':
            n = 10
        elif c.isdigit():
            n = int(c)
        elif c in ['S', 'D', 'T']:
            p[i] = n ** b[c]
            i += 1
        elif c == '#':
            p[i-1] *= -1
        elif c == '*':
            p[i-1] *= 2
            if i > 1:
                p[i-2] *= 2

    return sum(p)


# 정규식 풀이법

import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution('1S2D*3T') == 37)
print(solution('1D2S#10S') == 9)
print(solution('1D2S0T') == 3)
print(solution('1S*2T*3S') == 23)
print(solution('1D#2S*3S') == 5)
print(solution('1T2D3D#') == -4)
print(solution('1D2S3T*') == 59)