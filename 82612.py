def solution(price, money, count):
    s = sum([price * (c+1) for c in range(count)])
    return s - money if s >= money else 0

print(solution(3, 20, 4))

# Best solution
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)