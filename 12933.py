def solution(n):
    a = list(str(n))
    a.sort(reverse=True)
    a = ''.join(a)
    return int(a)

# one line coding
def solution2(n):
    return int("".join(sorted(str(n), reverse=True)))

print(solution2(118372) == 873211)