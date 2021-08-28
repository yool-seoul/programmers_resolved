def solution(s):
    d = ''
    b = 0
    for i, c in enumerate(s):
        b = i+1 if c == ' ' else b
        d += c.upper() if ((i-b)%2 == 0) else c.lower()
    return d

# one line solution
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


print(solution('try hello  world'))
print(solution('try hello world') == 'TrY HeLlO WoRlD')