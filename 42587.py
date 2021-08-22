def solution(prio, loc):
    cnt = 0
    
    while len(prio) >= 1:
        max_num = max(prio)
        num = prio.pop(0)
        loc -= 1

        if num >= max_num:
            cnt += 1
        else:
            prio.append(num)
            if loc == -1:
                loc = len(prio)-1

        if loc == -1:
            break

    return cnt


# 아래 코드는 왜 일부 테스트에서 failed 되는지  잘 모르겠음.
def solution2(prio, loc):
    mine = prio[loc]
    cnt2 = flag = 0

    cnt1 = sum(prio[i] < mine for i in range(len(prio)))
    
    for i in range(len(prio)-1, loc, -1):
        if flag:
            if prio[i] == mine:
                cnt2 += 1
        else:
            if prio[i] > mine:
                flag = 1
                cnt2 = 0
#    print(len(prio) - cnt1 - cnt2, '-', len(prio), cnt1, cnt2)    
    return len(prio) - cnt1 - cnt2

if __name__ == '__main__':
    PR = [[2, 1, 3, 2], [1, 1, 9, 1, 1, 1], [2, 2, 9, 1, 1, 2], [2, 2, 9, 1, 1, 2], [7], 
         [7, 8, 9, 3, 3, 1, 7, 3, 3, 1, 6, 3, 3], [7, 8, 9, 3, 3, 1, 7, 3, 3, 1, 6, 3, 3]]
    L = [2, 0, 0, 1, 0, 4, 7]
    R = [1, 5, 3, 4, 1, 9, 10]
    for pr, l, r in zip(PR, L, R):
        print(solution(pr, l)==r)