# BFS 알고리즘 조금 더 최적화. 맵에서 이미 검토끝난 값을 0으로 채우는 시점을 약간 앞당김.
# 이를 통해서 불필요한 비교연산을 조금 줄였음.
from collections import deque 
def solution(maps):
    mx = len(maps[0]) -1
    my = len(maps) -1
    path = deque()
    path.append((0, 0, 1))
    maps[0][0] = 0

    while path:
        (x, y, p) = path.popleft()
        if x == mx and y == my:
            return p
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0 <= x+dx <= mx and 0 <= y+dy <= my:
                if maps[y+dy][x+dx]:
                    path.append((x+dx, y+dy, p+1))
                    maps[y+dy][x+dx] = 0
    return -1



# BFS (Breadth-First Search)
# 왜인지 모르겠으나, 효율성에 걸림.
def solution3(maps):
    mx = len(maps[0]) -1
    my = len(maps) -1
    path = deque()
    path.append((0, 0, 1))

    while len(path):
        (x, y, p) = path.popleft()
        maps[y][x] = 0
        if x == mx and y == my:
            return p
        if x < mx and maps[y][x+1]:                
            path.append((x+1, y, p+1))
        if y < my and maps[y+1][x]:
            path.append((x, y+1, p+1))
        if x > 0 and maps[y][x-1]:
            path.append((x-1, y, p+1))
        if y > 0 and maps[y-1][x]:
            path.append((x, y-1, p+1))
    return -1





# 재귀호출 DFS 방식은 구현은 쉽지만 효율적이진 않음.
def move(MAP, x, y, path):
    MAP[x+y*5] = 0
    path += 1
    if x == 4 and y == 4:
        return path

    P = [100, 100, 100, 100]
    if x < 4 and MAP[x+1+y*5]:
        P[0] = move(MAP.copy(), x+1, y, path)
    if x > 0 and MAP[x-1+y*5]:
        P[1] = move(MAP.copy(), x-1, y, path)
    if y < 4 and MAP[x+y*5+5]:
        P[2] = move(MAP.copy(), x, y+1, path)
    if y > 0 and MAP[x+y*5-5]:
        P[3]= move(MAP.copy(), x, y-1, path)
    
    return min(P)

def solution2(maps):
    ret = move(sum(maps, []), 0, 0, 0)
    return -1 if ret == 100 else ret




print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) == 11)
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) == -1)