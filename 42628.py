# 이렇게 풀면 효율이 떨어지긴 함.
def solution(operations):
    L = []
    for s in operations:
        c, v = s.split(' ')
        v = int(v)
        if c == 'I':
            L.append(v)
            L = sorted(L, reverse=True)
        elif c == 'D' and v == 1 and len(L):
            L = L[1:]
        elif c == 'D' and v == -1 and len(L):
            L = L[0:-1]
    return [L[0], L[-1]] if len(L) else [0, 0]


print(solution(["I 16", "D 1"]) == [0,0])
print(solution(["I 16", "D 1", "D 1"]) == [0,0])
print(solution(["I 16", "I 15","D 1"]) == [15])
print(solution(["I 7","I 5","I -5","D -1"]) == [7,5])
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]) == [0, 0])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]) == [333, -45])