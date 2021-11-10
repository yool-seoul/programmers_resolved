def solution(genres, plays):
    A = {}
    for i, (key, val) in enumerate(zip(genres, plays)):
        if key not in A:
            A[key] = list()
            A[key].append((-1, 0))
        A[key].append((i, val))

    L = []
    for V in A.values():
        V.sort(key=lambda x: x[1], reverse=True)
        s = sum([v for _, v in V])
        L.append((s, V[0][0], V[1][0]))
    L.sort(key=lambda x: x[0], reverse=True)
    
    K = []
    for (_, v1, v2) in L:
        K.append(v1)
        if v2 >= 0:
            K.append(v2)
    return K


# 비슷한 풀이법. 좀 더 심플한 코드
def solution2(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer



print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0])
print(solution(["classic", "jazz", "jazz", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 3, 0, 1, 2])
