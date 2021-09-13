def solution(skill, skill_trees):
    v = 0
    for sk in skill_trees:
        old = -2
        v += 1
        for s in skill:
            new = sk.find(s)
            if (old > new and new != -1) or (old == -1 and new != -1):
                v -= 1
                break
            old = new
    return v



print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2)