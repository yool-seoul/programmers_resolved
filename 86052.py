from itertools import product
def solution(grid):
    w, h = len(grid[0]), len(grid)
    STATE = {'R':1, 'L':-1, 'S':0}
    DIR = [(1,0), (0,1), (-1,0), (0,-1)]
    ANS = []
    route_history = set()

    for (i, j, d) in product(*[range(h), range(w), range(4)]):
        if (i, j, d) in route_history:
            continue
        route = set()
        i0, j0, d0 = i, j, d
        while (i, j, d) not in route:
            route.add((i, j, d))
            route_history.add((i, j, d))
            d = (d + STATE[grid[i][j]]) % 4
            dx, dy = DIR[d]
            i = (i+dx)%h; j = (j+dy)%w
        
        if (i, j, d) == (i0, j0, d0):
            ANS.append(len(route))
    return sorted(ANS)

#Test 1 〉	통과 (0.18ms, 10.3MB)
#Test 2 〉	통과 (0.45ms, 10.4MB)
#Test 3 〉	통과 (0.50ms, 10.3MB)
#Test 4 〉	통과 (24.69ms, 15.5MB)
#Test 5 〉	통과 (53.07ms, 17.2MB)
#Test 6 〉	통과 (66.52ms, 18.8MB)
#Test 7 〉	통과 (1298.56ms, 139MB)
#Test 8 〉	통과 (859.80ms, 116MB)
#Test 9 〉	통과 (790.64ms, 110MB)
#Test 10 〉	통과 (875.71ms, 127MB)
#Test 11 〉	통과 (1190.73ms, 133MB)

def solution2(grid):
    w, h = len(grid[0]), len(grid)
    STATE = {'R':1, 'L':-1, 'S':0}
    DIR = [(1,0), (0,1), (-1,0), (0,-1)]
    L1 = []
    route_history = set()
    for i in range(h):
        for j in range(w):
            for d in [0, 1, 2, 3]:
                if (i, j, d) in route_history:
                    continue
                route = []
                while True:
                    if (i, j, d) not in route:
                        route.append((i, j, d))
                        route_history.add((i, j, d))
                        d = (d + STATE[grid[i][j]]) % 4
                        dx, dy = DIR[d]
                        i = (i+dx)%h; j = (j+dy)%w
                    else:
                        if (i, j, d) == route[0]:
                            L1.append(len(route))
                        break
    return sorted(L1)

#Test 1 〉	통과 (0.49ms, 10.3MB)
#Test 2 〉	통과 (2.89ms, 10.3MB)
#Test 3 〉	통과 (4.05ms, 10.3MB)
#Test 4 〉	통과 (4168.90ms, 15.1MB)
#Test 5 〉	통과 (7599.04ms, 16MB)
#Test 6 〉	통과 (8077.60ms, 16.4MB)
#Test 7 〉	실패 (시간 초과)
#Test 8 〉	실패 (시간 초과)
#Test 9 〉	통과 (773.74ms, 114MB)
#Test 10 〉	통과 (908.32ms, 134MB)
#Test 11 〉	통과 (1108.41ms, 140MB)

def solution3(grid):
    w, h = len(grid[0]), len(grid)
    STATE = {'R':1, 'L':-1, 'S':0}
    DIR = [(1,0), (0,1), (-1,0), (0,-1)]    # right --> down --> left --> up 의 'R' 방향 순서
    L1, L2 = [], []
    route_history = set()
    for i in range(h):
        for j in range(w):
            for d in [0, 1, 2, 3]:
                if (i, j, d) in route_history:
                    continue
                route = set()
                while True:
                    if (i, j, d) not in route:
                        route.add((i, j, d))
                        route_history.add((i, j, d))
                        d = (d + STATE[grid[i][j]]) % 4
                        dx, dy = DIR[d]
                        i = (i+dx)%h; j = (j+dy)%w
                    else:
                        break
                if route not in L1:
                    L1.append(route)
                    L2.append(len(route))
    return sorted(L2)

#Test 1 〉	통과 (0.22ms, 10.3MB)
#Test 2 〉	통과 (0.47ms, 10.3MB)
#Test 3 〉	통과 (0.52ms, 10.4MB)
#Test 4 〉	통과 (38.82ms, 17.5MB)
#Test 5 〉	통과 (70.19ms, 23.5MB)
#Test 6 〉	통과 (64.82ms, 24.8MB)
#Test 7 〉	통과 (3060.83ms, 211MB)
#Test 8 〉	통과 (1016.13ms, 207MB)
#Test 9 〉	실패 (시간 초과)
#Test 10 〉	실패 (시간 초과)
#Test 11 〉	실패 (시간 초과)


print(solution(["SL","LR"]) == [16])
print(solution(["S"]) == [1,1,1,1])
print(solution(["R","R"]) == [4,4])