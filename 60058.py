
def solution(p):
    if p == '':
        return ''

    b = 0
    flag = True
    for i in range(len(p)):
        b += 1 if p[i] == '(' else -1
        if b == 0:
            break
        elif b < 0:
            flag = False

    u = p[:i+1]
    v = p[i+1:]

    if flag:
        return u + solution(v)
    else:
        u2 = ''
        for c in u[1:-1]:
            u2 += '(' if c == ')' else ')'

        return '(' + solution(v) + ')' + u2        



print(solution("(()())()") == "(()())()")
print(solution(")(") == "()")
print(solution("()))((()") == "()(())()")
print(solution("))()((") == "()()()")