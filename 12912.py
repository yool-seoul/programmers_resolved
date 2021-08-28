def solution(a, b):
    (a, b) = (b, a) if a > b else (a, b)
    return sum([i for i in range(a, b+1)])


# simplifed code, complexity = O(n), n = abs(a, b)
def solution2(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a,b+1))

# mathematical expression, complexity = O(1)
def solution3(a, b):
    return (abs(a-b)+1)*(a+b)//2    # 등차수열의 합 공식 이용.

print(solution(3, 5) == 12)
print(solution2(3, 3) == 3)
print(solution3(5, 3) == 12)