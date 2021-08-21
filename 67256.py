def solution(numbers, hand):
    answer = ''
    L = {1, 4, 7}
    R = {3, 6, 9}
    posL = 10
    posR = 12
    dL = dR = 0
    for num in numbers:
        if num == 0:
            num = 11
        if num in L:
            answer += 'L'
            posL = num
        elif num in R:
            answer += 'R'
            posR = num
        else:
            dL = int(abs(num - posL)/3) + abs(num - posL)%3
            dR = int(abs(num - posR)/3) + abs(num - posR)%3
            
            if dL > dR:
                answer += 'R'
                posR = num
            elif dL < dR:
                answer += 'L'
                posL = num
            else:
                if hand == 'right':
                    answer += 'R'
                    posR = num
                else:
                    answer += 'L'
                    posL = num
    return answer