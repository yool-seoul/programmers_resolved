def solution(n):
    return [c for c in reversed(list(map(int, str(n))))]

# 더 짧은 해법. reverse first.
    return list(map(int, reversed(str(n))))
    return [int(i) for i in str(n)][::-1]
    return list(map(int, list(str(n))[::-1]))


print(solution(12345) == [5, 4, 3, 2, 1])