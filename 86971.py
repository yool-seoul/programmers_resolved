def solution(n, wires):
    D = []
    for i in range(n-1):
        WIRES = wires.copy()
        (w1, w2) = WIRES.pop(i)
        L = {w1}
        R = {w2}
        while WIRES:
            (w1, w2) = WIRES.pop(0)
            if w1 in L:         L.add(w2)
            elif w2 in L:       L.add(w1)
            elif w1 in R:       R.add(w2)
            elif w2 in R:       R.add(w1)
            else:
                WIRES.append([w1, w2])
        D.append(abs(len(L) - len(R)))
    return min(D)



# the shortest coding
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]) == 3)
print(solution(4, [[1,2],[2,3],[3,4]]) == 0)
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]) == 1)