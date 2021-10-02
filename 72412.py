from itertools import product
def findPos(arr, num):
    print(arr, num)
    start = pos = 0
    end = len(arr)-1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == num:
            pos = middle
            end = middle - 1
        elif arr[middle] > num:
            end = middle - 1
        else:
            start = pos = middle + 1
    print(pos)
    return pos

def solution(info, query):
    IDX = {'java': 1, 'python': 2, 'cpp': 3, 'backend': 1, 'frontend': 2, 
           'junior': 1, 'senior': 2, 'pizza': 1, 'chicken': 2, '-': 0}
    MASK = list(product(*[[0, 1], [0, 1], [0, 1], [0, 1]]))

    M = [0] * 108   # 4 X 3 X 3 X 3, the num of all combinations
    for i in range(len(M)):
        M[i] = list()

    for p in info:
        P = p.split(' ')
        for i in range(len(MASK)):
            idx = IDX[P[0]]*3*3*3*MASK[i][0] + IDX[P[1]]*3*3*MASK[i][1] \
                + IDX[P[2]]*3*MASK[i][2] + IDX[P[3]]*MASK[i][3]
            M[idx].append(int(P[4]))
    S = []
    for q in query:
        Q = q.replace(' and', '').split(' ')
        idx = IDX[Q[0]]*3*3*3 + IDX[Q[1]]*3*3 + IDX[Q[2]]*3 + IDX[Q[3]] 
#        n = sum(1 for i in M[idx] if i >= int(Q[4]))
#        S.append(n)
        pos = findPos(sorted(M[idx]), int(Q[4]))
        S.append(len(M[idx])-pos)
                
    return S





# 비트연산으로 속도는 빨라졌으나, 효율성 통과하기엔 부족
def solution3(info, query):
    S = []
    N = []
    M = {'java': 0x80000000, 'python': 0x40000000, 'cpp': 0x20000000,
         'backend': 0x10000000, 'frontend': 0x08000000, 'junior': 0x04000000,
         'senior': 0x02000000, 'pizza':  0x01000000, 'chicken':0x00800000}
    B = [0xE0000000, 0x18000000, 0x06000000, 0x01800000]

    for p in info:
        P = p.split(' ')
        n = M[P[0]] | M[P[1]] | M[P[2]] | M[P[3]] | int(P[4])
        N.append(n)
    
    for q in query:
        c = 0
        Q = q.replace(' and', '').split(' ')
        n = sum([B[i] if Q[i] == '-' else M[Q[i]] for i in range(4)]) + int(Q[4])
        for p in N:
            if not ~n & p & 0xFF800000:
                if n & 0x007FFFFF <= p & 0x007FFFFF:
                    c+=1
        S.append(c)
    return S




#Test 1 〉	통과 (0.26ms, 10.5MB)
#Test 2 〉	통과 (0.27ms, 10.5MB)
#Test 3 〉	통과 (0.40ms, 10.5MB)
#Test 4 〉	통과 (1.75ms, 10.5MB)
#Test 5 〉	통과 (4.12ms, 10.5MB)
#Test 6 〉	통과 (10.92ms, 10.5MB)
#Test 7 〉	통과 (4.66ms, 10.6MB)
#Test 8 〉	통과 (65.76ms, 11.5MB)
#Test 9 〉	통과 (66.53ms, 13.3MB)
#Test 10 〉	통과 (65.62ms, 13.8MB)
#Test 11 〉	통과 (4.31ms, 10.5MB)
#Test 12 〉	통과 (11.62ms, 10.7MB)
#Test 13 〉	통과 (4.77ms, 10.8MB)
#Test 14 〉	통과 (38.09ms, 11.9MB)
#Test 15 〉	통과 (38.46ms, 12MB)
#Test 16 〉	통과 (4.46ms, 10.5MB)
#Test 17 〉	통과 (11.34ms, 10.7MB)
#Test 18 〉	통과 (39.14ms, 11.9MB)

#테스트 1 〉	통과 (0.08ms, 10.4MB)
#테스트 2 〉	통과 (0.11ms, 10.5MB)
#테스트 3 〉	통과 (0.47ms, 10.4MB)
#테스트 4 〉	통과 (3.64ms, 10.4MB)
#테스트 5 〉	통과 (12.85ms, 10.5MB)
#테스트 6 〉	통과 (27.61ms, 10.4MB)
#테스트 7 〉	통과 (13.49ms, 10.6MB)
#테스트 8 〉	통과 (61.09ms, 10.9MB)
#테스트 9 〉	통과 (58.54ms, 10.9MB)
#테스트 10 〉	통과 (59.13ms, 11MB)
#테스트 11 〉	통과 (12.32ms, 10.5MB)
#테스트 12 〉	통과 (28.10ms, 10.5MB)
#테스트 13 〉	통과 (14.42ms, 10.6MB)
#테스트 14 〉	통과 (55.13ms, 10.6MB)
#테스트 15 〉	통과 (58.59ms, 10.6MB)
#테스트 16 〉	통과 (13.38ms, 10.4MB)
#테스트 17 〉	통과 (29.71ms, 10.6MB)
#테스트 18 〉	통과 (74.84ms, 10.6MB)


#  정확성 테스트 통과, 유효성 테스트 실패
def solution2(info, query):
    S = []
    for q in query:
        Q = q.replace(' and', '').split(' ')
        n = 0
        for p in info:
            P = p.split(' ')
            s = sum([1 if P[i] == Q[i] or Q[i] == '-' else 0 for i in range(4)])
            if s == 4 and int(P[4]) >= int(Q[4]):
                n += 1
        S.append(n)
    return S




print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["cpp and frontend and senior and pizza 200",
                "java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150",
                "- and - and - and - 50",
                "- and - and - and - 0",
                "- and - and - and - 1500"]) == [0,1,1,1,1,2,4,6,6,0])

#a = [1, 2, 2, 3, 3, 3, 4, 5, 6, 10, 100, 100, 101, 102, 103, 200]
a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
b = 1
c = findPos(a,  b)
print(len(a), c, len(a) - c)