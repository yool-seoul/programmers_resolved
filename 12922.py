def solution(n):
#    return ''.join(['수','박'][i%2] for i in range(n))

# best code
    return ("수박" * n)[:n]

# another solution
    return "수박"*(n//2) + "수"*(n%2)


print(solution(3) == '수박수')
print(solution(4) == '수박수박')