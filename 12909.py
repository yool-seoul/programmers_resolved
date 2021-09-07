def solution(s):
    v = 0
    for c in s:
        v += 1 if c == '(' else -1
        if v < 0:
            return False
    return True if v == 0 else False


print(solution("()()") == True)
print(solution("(())()") == True)
print(solution(")()(") == False)
print(solution("(()(") == False)

