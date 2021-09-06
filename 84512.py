def solution(word):
    w = ('A', 'E', 'I', 'O', 'U')
    t = (781, 156, 31, 6, 1)    # list of sigma of 5^4, 5^3, ..., 5^0
    return sum([w.index(c) * t[i] + 1 for i, c in enumerate(word)])


# index 를 찾는 다른 방식으로, 튜플 선언없이 문자열로 가능.
# "AEIOU".index(c) 

print(solution('AAAAE') == 6)
print(solution('AAAE') == 10)
print(solution('I') == 1563)
print(solution('EIO') == 1189)