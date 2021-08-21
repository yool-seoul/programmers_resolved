def solution(new_id):
    res = ''
    for c in new_id.lower():
        if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') or c == '.' or c == '-' or c == '_':
            res += c
    while '..' in res:
        res = res.replace('..', '.')
    res = res.strip('.')[0:15].strip('.')
    res = 'a' if len(res) == 0 else res
    while len(res) < 3:
        res += res[-1]

    return res

print(solution("...!@BaT#*..y.abcdefghijklm가나나다ㄱㄴㄷ"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

# Best Solution
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st