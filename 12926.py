def solution(s, n):
    c2 = ''
    for c in s:
        if c == ' ':
            o2 = ord(c)
        elif c.isupper():
            o2 = ord(c) + n - 26 if ord(c) + n > ord('Z') else ord(c) + n
        elif c.islower():
            o2 = ord(c) + n - 26 if ord(c) + n > ord('z') else ord(c) + n
        c2 += chr(o2)
    return c2


# one line solution
    return ''.join([chr(ord(i) + (not ord(i)==32)*((n%26) -26*((90<(ord(i)+(n%26))*(ord(i)<91)) + (122<(ord(i)+(n%26)))))) for i in s])


print(solution('AB', 1) == 'BC')
print(solution('z', 1) == 'a')
print(solution('a B z', 4) == 'e F d')


#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.