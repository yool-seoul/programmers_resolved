def solution(arr):
    b = []
    c = 'a'
    for a in arr:
        if c != a:
            b.append(a)
        c = a
    return b

print(solution([1,1,3,3,0,1,1]) == [1,3,0,1])
print(solution([4,4,4,3,3]) == [4,3])