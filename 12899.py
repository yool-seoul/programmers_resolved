def solution(n):
    val = [1, 2, 4]
    m = 1
    v = 0
    while n > 0:
        v += val[(n-1)%3] * m
        n = int((n-1)/3)
        m *= 10

    return str(v)

# 문자열 풀이법
def solution2(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

if __name__ == '__main__':
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 40]
    R = ['1', '2', '4', '11', '12', '14', '21', '22', '24', '41', '1111']
    for s, r in zip(S,R):
        print(solution2(s)==r)
