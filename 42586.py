import math
def solution(progresses, speeds):
    answer = []
    rs = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    cnt = 1
    m = 0
    for r in rs:
        if r > m:
            if m != 0:
                answer.append(cnt)
                cnt = 1
            m = r
        else:
            cnt += 1

    answer.append(cnt)
    return answer


# best solution
def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]



print(solution2([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])