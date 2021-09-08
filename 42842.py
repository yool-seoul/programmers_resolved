def solution(brown, yellow):
    Y = [(i, int(yellow/i)) for i in range(1, int(yellow**0.5)+1) if yellow%i == 0]
    for y in Y:
        if (sum(y)+2)*2 == brown:
            return [y[1]+2, y[0]+2]


# 둘레의 길이를 이용한 풀이법
def solution2(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

# 근의 공식을 이용한 풀이
import math
def solution3(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]


print(solution(12, 4) == [4,4])
print(solution(10, 2) == [4,3])
print(solution(8, 1) == [3,3])
print(solution(24, 24) == [8,6])
print(solution(24, 25) == [7,7])