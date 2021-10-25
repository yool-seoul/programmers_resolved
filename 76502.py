def solution(s):
    S = list(s)
    D = {'}':'{', ']':'[', ')':'('}
    f = 0
    for _ in range(len(s)):
        V = [0,]
        for c in S:
            if c == '{' or c == '(' or c == '[':
                V.append(c)
            else:
                if D[c] != V[-1]:
                    f += 1
                    V = [0,]
                    break
                V.pop()
        f += 1 if len(V) != 1 else 0
        S.append(S.pop(0))
    return len(s) - f



print(solution("[](){}") == 3)
print(solution("}]()[{") == 2)
print(solution("[)(]") == 0)
print(solution("}}}") == 0)
print(solution("(") == 0)
print(solution("{{{{{") == 0)
print(solution("]]]]]") == 0)