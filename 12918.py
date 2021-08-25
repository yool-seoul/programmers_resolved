def solution(s):
    return s.isdecimal() and (len(s) == 4 or len(s) == 6)


# 더 파이썬 다운 코드
def solution2(s):
    return s.isdecimal() and len(s) in (4, 6)

# 흥미로운 접근
def solution3(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6 

# 정규식 이용
# ^와 $는 문자열의 처음과 끝을 의미. \d는 숫자를 의미, {4}|{6}은 숫자가 4번 혹은 6번 반복을 의미함.
import re
def solution4(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))

print(solution('a234') == False)
print(solution('1234') == True)
print(solution2('12345') == False)
print(solution3('123456') == True)
print(solution4('1234567') == False)