def solution(scores):
    answer = ''
    arr = ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A', 'A']

    for i, score in enumerate(zip(*scores)):
        avg = (sum(score) - score[i]) / (len(score) - 1) if score[i] in (min(score), max(score)) and score.count(score[i]) == 1 else sum(score) / len(score)
        answer += arr[int(avg/10)]
    return answer


print(f'sol1: {solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])}')
print(f'sol2: {solution([[50,90],[50,87]])}')
print(f'sol3: {solution([[70,49,90],[68,50,38],[73,31,100]])}')