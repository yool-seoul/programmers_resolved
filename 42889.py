def solution(N, stages):
    A = [0] * N 
    F = [0] * (N+1)    # num of failures
    R = [0] * N        # failure rate and index

    for stage in stages:
        F[stage-1] += 1

    for i in range(N):
        R[i] = (i+1, F[i] / sum(F[i:N+1]) if F[i] > 0 else 0)

    R.sort(key=lambda x: x[1], reverse=True)   # sort by failure rate
    A, _ = zip(*R)

    return list(A)

# another solution

def solution2(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5])
print(solution(4, [4,4,4,4,4]) == [4,1,2,3])
print(solution(3, [1, 1, 1, 1, 1]) == [1, 2, 3])


# Test Result
#테스트 1 〉	통과 (0.01ms, 10.2MB)
#테스트 2 〉	통과 (0.08ms, 10.2MB)
#테스트 3 〉	통과 (1.84ms, 10.5MB)
#테스트 4 〉	통과 (6.57ms, 10.9MB)
#테스트 5 〉	통과 (16.37ms, 15MB)
#테스트 6 〉	통과 (0.13ms, 10.4MB)
#테스트 7 〉	통과 (0.67ms, 10.2MB)
#테스트 8 〉	통과 (7.03ms, 10.9MB)
#테스트 9 〉	통과 (16.68ms, 15.1MB)
#테스트 10 〉	통과 (6.75ms, 10.9MB)
#테스트 11 〉	통과 (6.95ms, 10.8MB)
#테스트 12 〉	통과 (10.71ms, 11.4MB)
#테스트 13 〉	통과 (11.32ms, 11.4MB)
#테스트 14 〉	통과 (0.02ms, 10.3MB)
#테스트 15 〉	통과 (4.88ms, 10.6MB)
#테스트 16 〉	통과 (2.48ms, 10.4MB)
#테스트 17 〉	통과 (4.54ms, 10.6MB)
#테스트 18 〉	통과 (2.54ms, 10.5MB)
#테스트 19 〉	통과 (0.53ms, 10.3MB)
#테스트 20 〉	통과 (3.50ms, 10.4MB)
#테스트 21 〉	통과 (7.13ms, 10.9MB)
#테스트 22 〉	통과 (18.95ms, 18.4MB)
#테스트 23 〉	통과 (14.10ms, 11.6MB)
#테스트 24 〉	통과 (14.79ms, 11.7MB)
#테스트 25 〉	통과 (0.01ms, 10.2MB)
#테스트 26 〉	통과 (0.01ms, 10.3MB)
#테스트 27 〉	통과 (0.01ms, 10.2MB)

