def solution(a):
    t = 1
    for v in a:
        t *= v
        if (t**0.5).is_integer():
            return 'found'
    return 'not found'

print(solution([5,1,2,3,1]) == 'not found')
print(solution([2,4,2,5,1]) == 'found')