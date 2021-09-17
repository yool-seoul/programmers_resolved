import math
def solution(w,h):
    g = math.gcd(w, h)
    return w*h - w - h +g


# 크기 비교 후 swap은 이렇게 쓸 수도 있음.
    (w, h) = (h, w) if h > w else (w, h)


print(solution(11, 3) == 20)
print(solution(22, 6) == 20+20+33+33)
print(solution(7, 3) == 12)
print(solution(14, 6) == 21+21+12+12)
print(solution(3, 5) == 8)
print(solution(5, 3) == 8)
print(solution(4, 5) == 12)
print(solution(5, 4) == 12)
print(solution(8, 12) == 80)
print(solution(12, 8) == 80)
print(solution(1, 5) == 0)
print(solution(5, 1) == 0)
print(solution(3, 3) == 6)
print(solution(2, 2) == 2)
print(solution(1, 1) == 0)