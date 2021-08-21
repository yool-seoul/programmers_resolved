def findViolation(arr, threshold):
    dic = {'P':10, 'O':1, 'X':0}
    nums = [dic[a] for a in arr]
    return 0 if sum(nums) >= threshold else 1 

def sol2(places):
    answer = []
    for p in places:
        res = 1
        m = list(zip(*p))
        for i in range(5):
            for j in range(5):
                if i < 4:
                    if findViolation((m[i][j], m[i+1][j]), 20):
                        res =0
                        continue
                if j < 4:
                    if findViolation((m[i][j], m[i][j+1]), 20):
                        res = 0
                        continue
                if i < 4 and j < 4:
                    if findViolation((m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1]), 21):
                        res = 0
                        continue
                if i < 3:
                    if findViolation((m[i][j], m[i+1][j], m[i+2][j]), 21):
                        res = 0
                        continue
                if j < 3:
                    if findViolation((m[i][j], m[i][j+1], m[i][j+2]), 21):
                        res = 0
                        continue
        answer.append(res)
    return answer

def solution(places):
    answer = []
    for p in places:
        res = 1
        m = list(zip(*p))
        for i in range(5):
            for j in range(5):
                if i < 4:
                    res *= findViolation((m[i][j], m[i+1][j]), 20)
                if j < 4:
                    res *= findViolation((m[i][j], m[i][j+1]), 20)
                if i < 4 and j < 4:
                    res *= findViolation((m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1]), 21)
                if i < 3:
                    res *= findViolation((m[i][j], m[i+1][j], m[i+2][j]), 21)
                if j < 3:
                    res *= findViolation((m[i][j], m[i][j+1], m[i][j+2]), 21)
        answer.append(res)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOP", "POXXP"], 
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
                ["PXOPX", "OXOXP", "PXPOX", "OXXOP", "PXPOX"], 
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))