def solution(cacheSize, cities):
    Q = []
    C = 0
    for city in cities:
        CITY = city.upper()
        if CITY in Q:
            C += 1
            Q.remove(CITY)
        else:
            C += 5

        Q.append(CITY)
        if len(Q) > cacheSize:
            Q.pop(0)
    return C


# deque 에는 maxlen 이 있음.
def solution2(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time



print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "la"]) == 50)
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21)
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60)
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16)
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25)