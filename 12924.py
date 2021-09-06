def solution(n):
    cnt = 0
    for i in range(1, n//2+1):
        s = 0
        for j in range(i, n):
            s += j
            if s == n:
                cnt += 1
            elif s > n:
                break
    return cnt+1

# 등차수열의 합 공식을 이용한 코딩
    return len([i  for i in range(1,num+1,2) if num % i is 0])
    
print(solution(15) == 4)