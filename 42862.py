def solution(n, lost, reserve):
    st = [1 for i in range(n+2)]

    for j in reserve:
        st[j] = 2

    lost2 = lost.copy()
    for i in lost:
        if st[i] == 2:     # 체육복 2개인 학생이 도난 당함.
            st[i] = 1
            lost2.remove(i)

    lost2.sort()
    for i in lost2:
        if st[i-1] == 2:
            st[i-1] = st[i] = 1
        elif st[i+1] == 2:
            st[i+1] = st[i] = 1
        else:
            st[i] = 0

    return n - st.count(0)

# another solution
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    _reserve.sort()
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


print(solution2(5, [1, 4, 3, 2], [4,2,3]) == 4)
print(solution2(5, [4, 2], [5, 3, 1]) == 5)
print(solution2(5, [2, 4], [3]) == 4)
print(solution2(3, [3], [1]) == 2)
print(solution2(3, [1,2], [2,3]) == 2)
print(solution2(5, [2,4], [3,1]) == 5)
print(solution2(5, [2, 4], [1, 3]) == 5)