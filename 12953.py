def gcd(a, b):
    return b if a%b == 0 else gcd(b, a%b)

def solution(arr):
    b = 1
    for a in arr:
        b = int(a * b / gcd(a, b))    
    return b


print(solution([2,6,8,14]) == 168)
print(solution([1,2,3]) == 6)