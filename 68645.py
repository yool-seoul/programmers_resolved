def solution(n):
    L = [[0 for c in range(n)] for r in range(n)]
    L[0][0] = 1
    dir, i, j, k = 0, 0, 0, 1
    while k < n*(n+1)//2:
        if dir == 0:
            if i+1 < n and not L[i+1][j]:
                i+=1; k+=1
            else:
                dir = 1
        elif dir == 1:
            if j+1 < n and not L[i][j+1]:
                j+=1; k+=1
            else:
                dir = 2
        elif dir == 2:
            if i-1 > 0 and j-1 > 0 and not L[i-1][j-1]:
                i-=1; j-=1; k+=1
            else:
                dir = 0
        L[i][j] = k
    
    return list(filter(lambda x: x>0, sum(L, [])))
    return [v for v in sum(L, []) if v > 0]        # list comprehension 방법. 가독성이 더 좋다.


print(solution(4) == [1,2,9,3,10,8,4,5,6,7])
print(solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9])
print(solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])