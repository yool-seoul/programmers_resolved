def solution(x, n):
    return [x*i for i in range(1, n+1)]
        

# another solution
    return list(range(x, x*(n+1) ,x))
print(solution(2, 5) == [2,4,6,8,10])
print(solution(4, 3) == [4, 8, 12])
print(solution(-4, 2) == [-4, -8])