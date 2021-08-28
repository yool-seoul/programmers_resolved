def solution(num):
    return 'Odd' if (num%2 == 1) else 'Even' 


# 새로운 접근법
def solution2(num):
    return ["Even", "Odd"][num%2]
    return ["Even", "Odd"][num&1]   # 2진수 AND 연산으로도 구현 가능.

print(solution2(3) == 'Odd')
print(solution2(4) == 'Even')