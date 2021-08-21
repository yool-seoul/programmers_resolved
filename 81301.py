def solution(s):
    dic = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, word in enumerate(dic):
        s = s.replace(word, str(num))
    return int(s)

print(solution('one4seveneight'))
print(solution('23four5six7'))
print(solution('2three45sixseven'))
print(solution('123'))


# 다른 풀이법

def solution(s):
    dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for key, value in dic.items():
        s = s.replace(key, value)
    return int(s)