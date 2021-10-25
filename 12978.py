def solution(N, road, K):
    R = [K+1]*(N+1)
    R[1] = 0
    R2 = R.copy()
    while True:
        for p1, p2, w in road:
            R2[p1] = min(R2[p1], R2[p2]+w)
            R2[p2] = min(R2[p2], R2[p1]+w)
        if R == R2:
            break    
        R = R2.copy()
    return sum(1 for p in R if p <= K)

# 아래 방식으로는 missed 되는 것이 있음.
def solution2(N, road, K):
    R = [K+1]*(N+1)
    R[1] = 0
    road = [[p2, p1, w] if p1 > p2 else [p1, p2, w] for p1, p2, w in road ]
    road.sort(key=lambda x: (x[0], x[1]))
    print(road)
    for p1, p2, w in road:
        R[p1] = min(R[p1], R[p2]+w)
        R[p2] = min(R[p2], R[p1]+w)
    print(R)
    return sum(1 for p in R if p <= K)


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3) == 4)
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4) == 4)
print(solution(6, [[1,2,1],[1,3,3],[2,3,1],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4) == 4)
print(solution(6, [[1,2,1],[3,5,2],[3,4,3],[5,6,1],[1,3,3],[2,3,1],[3,5,3]], 4) == 4)
print(solution(6, [[1,2,1],[3,5,2],[3,4,3],[5,6,1],[4,3,3],[5,3,1],[3,5,3]], 4) == 2)
print(solution(1, [], 1) == 1)
print(solution(7, [[1,2,1],[2,3,1],[3,4,1],[4, 5, 1],[5,6,1],[7,1,1], [5, 7, 1]], 2) == 5)