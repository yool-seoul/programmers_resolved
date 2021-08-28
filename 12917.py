def solution(s):
    return ''.join(sorted(list(s), reverse=True))

# sorted 가 list 로 파라미터를 변환 후 동작하는 함수임. 굳이 list 한 번 더 써줄 필요 없음.
    return ''.join(sorted(s, reverse=True))

print(solution('Zbcdefg') == 'gfedcbZ')