def findDest(dest, route, tickets):
    for i in range(len(tickets)):
        if i not in route:
            if tickets[i][0] == dest:
                route.append(i)
                route = findDest(tickets[i][1], route, tickets)
    
    if len(route) == len(tickets):
        return route
    else:
        route.pop()
        return route

def solution1(tickets):
    R = []
    tickets.sort()
    route = findDest('ICN', [], tickets)
    for r in route:
        R.append(tickets[r][0])
    R.append(tickets[route[-1]][1])

    return R

# 재귀호출없이 풀어보기
from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())

    return p[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "JFK"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "SFO", "ATL", "ICN", "JFK"])
