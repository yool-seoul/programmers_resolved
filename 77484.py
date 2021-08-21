def solution(lottos, win_nums):
    answer = [0, 0]
    c = z = 0
    for i in range(6):
        z += 1 if lottos[i] == 0 else 0
        c += 1 if lottos[i] in win_nums else 0
    answer[0] = 7 -c -z -(7 -c -z)//7
    answer[1] = 7 -c -(7 -c)//7
    return answer