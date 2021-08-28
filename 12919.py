def solution(seoul):
    for i, name in enumerate(seoul):
        if name == 'Kim':
            return f'김서방은 {i}에 있다'

# one line solution
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    return f"김서방은 {seoul.index('Kim')}에 있다"
    return ('김서방은 %d에 있다' %seoul.index('Kim'))

print(solution(['Jane', 'Kim']) == '김서방은 1에 있다')
