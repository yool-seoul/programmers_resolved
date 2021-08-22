def solution(numbers):
    a = set()
    for n1 in range(len(numbers)):
        for n2 in range(n1+1, len(numbers)):
            a.add(numbers[n1] + numbers[n2])
    return sorted(list(a))

print(solution([7,2,1,3,4,1]))        # [2,3,4,5,6,7]
print(solution([5,0,2,7]))          # [2,5,7,9,12]

# one line code
def solution(numbers): return sorted({numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})

# uses an external module, combination
from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))