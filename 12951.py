def solution(s):
    f = True
    W = ''
    for w in s:
        w = w.lower()
        w = w.upper() if f else w
        f = True if w == ' ' else False
        W += w
    return W


# 내장함수 이용
    return ' '.join([word.capitalize() for word in s.split(" ")])

print(solution("3people unFollowed me") == "3people Unfollowed Me")
print(solution("for the last week") == "For The Last Week")
