import heapq
def solution(SV, K):
    cnt = 0
    heapq.heapify(SV)

    while True:
        a = heapq.heappop(SV)
        if a < K:
            if len(SV) == 0:
                return -1
            else:
                b = heapq.heappop(SV)
                heapq.heappush(SV, a + b * 2)
                cnt += 1
        else:
            return cnt


if __name__ == '__main__':
    S = [[1,2,3,9,10,12], [0, 0], [1,2], [1,2,3], [7, 1], [3, 4], [4, 4], [3, 3], [1,5], [2,3,7,10,15], [1, 2, 12, 3, 9, 10], [1, 2, 12, 3, 9, 10], [100, 200]]
    K = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 137, 15]
    P = [2, -1, -1, 2, 1, 1, 1, 1, 1, 1, 2, -1, 0] 
    for s, k, p in zip(S, K, P):
        print(solution(s, k)==p)
