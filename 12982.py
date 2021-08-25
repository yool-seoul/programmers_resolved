def solution(D, budget):
    s = 0
    for i, d in enumerate(sorted(D), start=1):
        s += d
        if s > budget:
            return i-1
    return len(D)


# complexity high but simple to read
def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


print(solution([1,3,2,5,4], 9) == 3)
print(solution([2,2,3,3], 10) == 4)
print(solution([100, 200], 10) == 0)
print(solution([1,1,2,2,3], 100) == 5)
print(solution([100, 200], 110) == 1)