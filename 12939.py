def solution(s):
    l = list(map(int, s.split(' ')))
    return f'{min(l)} {max(l)}'
    return 0
#    return [min(l), max(l)]
#    for n in s:

# sort 를 이용해도 깔끔해짐
    il = sorted([int(c) for c in s.split(' ')])
    answer = ' '.join([str(il[0]), str(il[len(il)-1])])

print(solution('1 2 3 4') == '1 4')
print(solution('-1 -2 -3 -4') == '-4 -1')
print(solution('-1 -1') == '-1 -1')