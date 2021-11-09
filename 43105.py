def solution(T):
    for i in range(1, len(T)):
        for j in range(len(T[i])):
            if j == 0:
                T[i][j] += T[i-1][j]
            elif j == i:
                T[i][j] += T[i-1][j-1]
            else:
                T[i][j] += max(T[i-1][j-1], T[i-1][j])
    return max(T[-1])


#정확성  테스트
#Test 1 〉	통과 (0.01ms, 10.3MB)
#Test 2 〉	통과 (0.02ms, 10.4MB)
#Test 3 〉	통과 (0.04ms, 10.2MB)
#Test 4 〉	통과 (0.15ms, 10.2MB)
#Test 5 〉	통과 (1.03ms, 10.3MB)
#Test 6 〉	통과 (0.33ms, 10.2MB)
#Test 7 〉	통과 (1.03ms, 10.3MB)
#Test 8 〉	통과 (0.24ms, 10.3MB)
#Test 9 〉	통과 (0.01ms, 10.2MB)
#Test 10 〉	통과 (0.15ms, 10.2MB)
#효율성  테스트
#Test 1 〉	통과 (37.20ms, 14.1MB)
#Test 2 〉	통과 (28.98ms, 13.2MB)
#Test 3 〉	통과 (41.67ms, 14.7MB)
#Test 4 〉	통과 (33.62ms, 14.1MB)
#Test 5 〉	통과 (31.59ms, 13.9MB)
#Test 6 〉	통과 (42.97ms, 14.8MB)
#Test 7 〉	통과 (39.55ms, 14.4MB)
#Test 8 〉	통과 (34.53ms, 13.6MB)
#Test 9 〉	통과 (35.60ms, 14.1MB)
#Test 10 〉	통과 (40.33ms, 14.4MB)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30)