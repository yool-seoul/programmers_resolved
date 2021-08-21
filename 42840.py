def solution(answers):
    answer = []
    r = [-10000, 0, 0, 0]
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    r[1] = [x - y for x, y in zip(a1*2000, answers)].count(0)
    r[2] = [x - y for x, y in zip(a2*1250, answers)].count(0)
    r[3] = [x - y for x, y in zip(a3*1000, answers)].count(0)
    m = max(r)
    [answer.append(i) for i, v in enumerate(r) if v == m]
    return answer