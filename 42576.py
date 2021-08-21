def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]


# 효율성이 좋지 못한 방법, But 코드는 간단
def solution2(participant, completion):
    for p in completion:
        participant.remove(p)
    return participant[0]
#        participant[participant.index(p)] = ''
#    return max(participant)

# best solution
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))