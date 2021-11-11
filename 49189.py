from collections import defaultdict
from collections import deque
def solution(n, edge):
    D = defaultdict(list)
    for a, b in edge:
        D[a].append(b)
        D[b].append(a)
    
    S = [20000] * (n+1)
    S[0] = S[1] = 0
    Q = deque();    
    Q.append(1)
    while Q:
        idx = Q.popleft()
        for v in D[idx]:
            if S[v] > S[idx] + 1:
                S[v] = S[idx] + 1
                Q.append(v)
    return S.count(max(S))

#Test 1 〉	통과 (0.01ms, 10.3MB)
#Test 2 〉	통과 (0.02ms, 10.2MB)
#Test 3 〉	통과 (0.04ms, 10.3MB)
#Test 4 〉	통과 (0.24ms, 10.2MB)
#Test 5 〉	통과 (0.98ms, 10.6MB)
#Test 6 〉	통과 (2.68ms, 10.8MB)
#Test 7 〉	통과 (24.39ms, 17.5MB)
#Test 8 〉	통과 (40.20ms, 20.8MB)
#Test 9 〉	통과 (35.80ms, 20.5MB)

# T/C 8 번만 시간초과
def solution2(n, edge):
    S = [0] * n
    S[0] = 0
    while True:
        changed = False
        for a, b in edge:
            if S[b-1] > S[a-1]+1:
                S[b-1] = S[a-1]+1
                changed = True
            elif S[a-1] > S[b-1]+1:
                S[a-1] = S[b-1]+1
                changed = True
        if not changed:
            break
    return S.count(max(S))


# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
print(solution(5, []), 4)
print(solution(5, [[1,2]]), 3)
print(solution(5, [[1,1]]), 4)

