def solution(num):
    cnt = 0
    while True:
        if num == 1:
            return cnt
        elif cnt >= 500:
            return -1
        else:
            num = (num / 2) if (num % 2 == 0) else (num * 3 + 1)
            cnt += 1

# 여기서 억지로 홀수/짝수를 한 라인으로 표현할 필요는 없을듯...

print(solution(6) == 8)
print(solution(16) == 4)
print(solution(626331) == -1)
