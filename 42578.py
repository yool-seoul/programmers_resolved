def solution(clothes):
    D = dict()
    for c in clothes:
        if c[1] in D:
            D[c[1]] += 1
        else:
            D[c[1]] = 1
    m = 1
    for d in list(D.values()):
        m *= (d+1)
    return m-1

# Dict 의 각 값들을 카운팅하는 별도함수 사용하면 이렇게 구현할 수 있음.
def solution2(clothes):
    from collections import Counter
    cnt = Counter([kind for name, kind in clothes])
    m = 1
    for d in list(cnt.values()):
        m *= (d+1)
    return m-1

print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5)
print(solution2([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3)