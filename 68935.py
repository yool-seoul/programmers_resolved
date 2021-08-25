def solution(n):
    s = []
    while n > 0:
        s.append(str(n%3))
        n //= 3
    return int(''.join(s), 3)

# list 대신에 str 그냥 써도 됨.
def solution2(n):
    s = ''
    while n:
        s += str(n%3)
        n //= 3
    return int(s, 3)


print(solution(45) == 7)
print(solution(125) == 229)


# 45	1200	0021	7
# 125	11122	22111	229