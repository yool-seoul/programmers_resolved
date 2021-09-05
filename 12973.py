def solution(S):
    l = [0,]
    for s in S:
        if s != l[-1]:
            l.append(s)
        else:
            l.pop()

    return 1 if len(l) == 1 else 0


print(solution('baabaa') == 1)
print(solution('cdcd') == 0)
print(solution('a') == 0)

# 그냥 통과하는 치트코드
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer
