def solution(s):
    lv = 0
    D = dict()

    for c in s:
        if c == '{':
            lv += 1
            k = 1
            L = []
            n = ''
        elif c == '}':
            if lv == 2:
                L.append(int(n))
                D[k] = L
            lv -= 1
        elif c == ',':
            if lv == 2:
                L.append(int(n))
                n = ''
                k += 1
        else:
            if lv == 2:
                n += c
    
    S = list(D[1])
    for i in range(1, len(D)):
        diff = set(D[i+1]) - set(D[i])
        S.append(diff.pop())

    return S



import re
from collections import Counter
def solution2(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
    # 원소의 갯수가 가장 많은 순서대로 리스트에 담으면 됨.


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}") == [2, 1, 3, 4])
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") == [2, 1, 3, 4])
print(solution("{{20,111},{111}}") == [111, 20])
print(solution("{{123}}") == [123])
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}") == [3, 2, 4, 1])
