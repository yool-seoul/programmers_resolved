def solution(people, limit):
    cnt = 0
    P = sorted(people, reverse=True)
    j = len(P)-1
    for i in range(len(P)):
        if i > j:
            break
        if P[i] + P[j] <= limit:
            j-=1
        cnt+=1
    return cnt

# 직관적이긴하나, 효율성테스트를 통과하지 못하는 코드
def solution3(people, limit):
    B = []
    cnt = 0
    for p in sorted(people, reverse=True):
        flag = True
        for b in B:
            if b + p <= limit:
                B.remove(b)
                cnt+=1
                flag = False
                break
        if(flag):
            B.append(p)
    return len(B)+cnt


# 탑승객 2명 제한이 없다면 적용할 수 있는 코드
def solution2(people, limit):
    B = [0] * len(people)
    for p in sorted(people, reverse=True):
        for i in range(len(people)):
            if B[i] + p <= limit:
                B[i] += p
                break
    return sum(1 for b in B if b > 0)



print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
print(solution([5,6,7,8,14], 20) == 3)  # 5,7,8 - 6,14
print(solution([40,50,150,160], 200) == 2)
print(solution([100,500,500,900,950], 1000) == 3)
