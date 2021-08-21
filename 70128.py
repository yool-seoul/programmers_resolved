def solution(a, b): return sum(x * y for x, y in zip(a, b))

# best solution
solution2 = lambda x, y: sum(a*b for a, b in zip(x, y))

print(solution([1,2,3,4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))