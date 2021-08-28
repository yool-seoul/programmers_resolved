def solution(x):
    return (x % sum([int(str(x)[i]) for i in range(len(str(x)))]) == 0)
    
# shorter code
    return n % sum([int(c) for c in str(n)]) == 0
    return x % sum(list(map(int, str(x)))) == 0
for c in str(12345):
    print(c)

print(list(map(int, str(12345))))

print(solution(10) == True)
print(solution(12) == True)
print(solution(11) == False)
print(solution(13) == False)
