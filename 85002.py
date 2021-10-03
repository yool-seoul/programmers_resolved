def solution(weights, head2head):
    F = []
    for i, h in enumerate(head2head):
        c1 = c2 = c3 = 0
        for j in range(len(h)):
            if h[j] == 'W':
                if weights[i] < weights[j]:
                    c3 += 1
                c1 += 1
            elif h[j] == 'L':
                c2 += 1
        F.append([i+1, weights[i], c1/(c1+c2+0.000000000000000001), c3])
    F.sort(key=lambda x : (x[2], x[3], x[1]), reverse=True)
    return list(list(zip(*F))[0])




print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]) == [3,4,1,2])
print(solution([145,92,86], ["NLW","WNL","LWN"]) == [2,3,1])
print(solution([60,70,60], ["NNN","NNN","NNN"]) == [2,1,3])