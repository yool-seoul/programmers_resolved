from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    S = deque()
    for w in truck_weights:
        while sum(S) + w > weight:
            if len(S) < bridge_length:
                S.append(0)
            else:
                S.popleft()
                cnt += 1
        while (S and S[0] == 0) or len(S) == bridge_length:
            S.popleft()
            cnt += 1
        S.append(w)
    return cnt + len(S) + bridge_length





print(solution(2, 10, [7,4,5,6]) == 8)
print(solution(100, 100, [10]) == 101)
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110)
print(solution(5, 5, [2,2,2,2,1,1,1,1,1]) == 19)
print(solution(1, 2, [1,1,1]) == 4)
print(solution(4, 2, [1,1,1,1]) == 10)
print(solution(3, 3, [1,1,1]) == 6)