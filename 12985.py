def solution(n, a, b):
    for i in range(1, n):
        a = (a+1)//2
        b = (b+1)//2
        if a == b:
            return i
    return 0


# one line coding
    return ((a-1)^(b-1)).bit_length()
# a, b 를 xor 취하는 과정에서 ab 사이의 거리가 가까우면 상위비트는 차이가 나지 않겠죠? 
# 거꾸로 ab 사이의 거리가 멀면 상위비트가 차이 날 거고요. 
# 그래서 xor 연산 결과의 길이를 리턴해주면 라운드가 나오는 아이디어인것으로 보여요.

print(solution(8, 4, 7) == 3)
print(solution(10, 2, 3) == 2)
print(solution(2, 1, 3) == 0)