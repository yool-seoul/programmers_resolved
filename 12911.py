def solution(n):
    a = bin(n).count('1')
    while True:
        n += 1
        b = bin(n).count('1')
        if a == b:
            break
    return n


# 재귀호출 방식으로 풀이
    return n if bin(n).count("1") is count else nextBigNumber(n+1, bin(n).count("1") if count is 0 else count)


print(solution(78) == 83)
print(solution(15) == 23)