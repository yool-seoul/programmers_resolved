# 문제에서 제시한 이분탐색을 사용한 방법
# 추정 시간값/ 각 심사관별 심사시간 = 심사관당 맡을 수 있는 입국자 수
import time

def solution(n, times):
    v_min = n//len(times)
    v_max = min(times)*n
    while v_min < v_max:
        v_mid = (v_min + v_max) // 2
        s = sum([v_mid // times[i] for i in range(len(times))])
        if s < n:
            v_min = v_mid+1
        else:
            v_max = v_mid
    return v_min
#Test 1 〉	통과 (0.01ms, 10.2MB)
#Test 2 〉	통과 (0.08ms, 10.2MB)
#Test 3 〉	통과 (4.53ms, 10.2MB)
#Test 4 〉	통과 (191.22ms, 14.8MB)
#Test 5 〉	통과 (501.22ms, 17.8MB)
#Test 6 〉	통과 (448.81ms, 18MB)
#Test 7 〉	통과 (539.87ms, 17.7MB)
#Test 8 〉	통과 (722.06ms, 17.8MB)
#Test 9 〉	통과 (0.03ms, 10.3MB)


# 잘못된 이분탐색을 쓴 경우, 특정 케이스에서 시간이 무지하게 걸림.
def solution1(n, times):
    T = sorted(times)
    v_min = n//len(T)
    v_max = min(T)*n

    while True:
        est = (v_min + v_max) // 2
        s = sum([est // T[i] for i in range(len(times))])
 
        if s < n:
            v_min = v_min+1 if v_min == est else est
        elif s > n:
            v_max = v_max-1 if v_max == est else est
        else:  # s == n
            v_max = est
            if v_min == est:
                return est


#Test 1 〉	통과 (0.02ms, 10.2MB)
#Test 2 〉	통과 (0.11ms, 10.3MB)
#Test 3 〉	통과 (4.53ms, 10.3MB)
#Test 4 〉	통과 (250.91ms, 15.7MB)
#Test 5 〉	통과 (598.21ms, 19MB)
#Test 6 〉	실패 (시간 초과)
#Test 7 〉	통과 (602.25ms, 18.9MB)
#Test 8 〉	통과 (815.62ms, 18.9MB)
#Test 9 〉	실패 (시간 초과)



# 가장 단순한 방법. 시간초과 걸림
def solution2(n, times):
    Q = [0] * len(times)
    T = [0] * len(times)
    for i in range(len(times)):
        T[i] = Q[i] + times[i]
 
    while n:
        i = T.index(min(T))
        Q[i] += times[i]
        T[i] = Q[i] + times[i]
        n -= 1
    return max(Q)



print(solution(10, [1,2,3,4,5,6,7,8,9,10]) == 5)
print(solution(6, [7, 10]) == 28)
print(solution(9, [10,1]) == 9)
print(solution(2, [1, 1]) == 1)
print(solution(2, [2, 2]) == 2)
print(solution(5, [1]) == 5)