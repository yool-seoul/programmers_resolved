def solution(s):
    d = {x: s.count(x) for x in set(s)}
    return (d.get('p', 0) + d.get('P', 0)) == (d.get('y', 0) + d.get('Y', 0))

# best code
    return s.lower().count('p') == s.lower().count('y')

print(solution('pPoooyY') == True)
print(solution('Pyy') == False)