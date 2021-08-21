def isPrime(num):
    # 문제의 조건에 따르면 num 의 최소값은 6임.
    if num % 2 == 0:
        return 0
    
    for i in range(3, num, 2):
        if num % i == 0:
            return 0

    return 1

def solution(nums):
    cnt = 0
    for c in [(c1, c2, c3) for c1 in nums for c2 in nums for c3 in nums]:
        if c[0] < c[1] and c[1] < c[2]:
            cnt += isPrime(sum(c))
    return cnt

import numpy as np

num = np.random.randint(3, 51)
arr = []
for i in range(num):
    arr.append(np.random.randint(1, 1000))


# Best solutions
def solution2(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
#print(solution(arr))