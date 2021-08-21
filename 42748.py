def solution(array, commands):
    answer = []
    for a, b, c in commands:
        new = array[a-1:b]
        new.sort()
        num = new[c-1]
        answer.append(num)
    return answer