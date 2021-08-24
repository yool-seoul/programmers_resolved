def solution(s):
    i = len(s)//2 - (1 if len(s)%2 == 0 else 0)
    return s[i:len(s)//2+1]

# other solution
def solution2(s):
    return s[(len(s)-1)//2:len(s)//2+1]


print(solution2('abcde') == 'c')
print(solution2('qwer') == 'we')
print(solution2('appzal e') == 'za')

