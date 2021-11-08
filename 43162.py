# 성능빠르고 직관적인 코드
def solution1(n, computers):
    G = [{0}]
    for i in range(n):
        for j in range(i, n):
            if computers[i][j]:
                new = True
                for k in range(len(G)):
                    if i in G[k]:
                        G[k].add(j)
                        new = False
                        break
                if new:
                    G.append({i})

    i, j = 0, 1
    while True:
        k = len(G)
        if k == 1:
            return 1

        if (G[i] & G[j]):
            G[i] = G[i] | G[j]
            del G[j]
            i, j = 0, 1
            continue
        
        if j+1 < k:
            j += 1
        elif i+2 < k:
            i += 1
            j = i+1
        else:
            break

    return len(G)


# the simplest code
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))



# 일부 테스트 케이스(3번 같은 경우)를 통과하지 못함. 직관적이지만 오류가 있는 코드.
def solution2(n, computers):
    G = [{0}]
    for i in range(n):
        for j in range(i, n):
            if computers[i][j]:
                new = True
                for k in range(len(G)):
                    if i in G[k]:
                        G[k].add(j)
                        new = False
                        break
                if new:
                    G.append({i, j})
    return len(G)


print(solution(1, [[1]]) == 1)
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)
print(solution(5, [[1,1,0,0,1], [1,1,0,0,0], [0,0,1,1,0],[0,0,1,1,1],[1,0,0,1,1]]) == 1)
print(solution(5, [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]) == 5)
print(solution(5, [[1,1,0,0,1], [1,1,0,0,0], [0,0,1,0,0],[0,0,0,1,1],[1,0,0,1,1]]) == 2)