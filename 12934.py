def solution(n):
    x = n**0.5
    return (x+1)**2 if (x == int(x)) else -1
    
print(solution(121) == 144)
print(solution(3) == -1)