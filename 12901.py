def solution(a, b):
    w = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    d = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    n = sum([d[i] for i in range(1, a)]) + b
    return w[(n+4)%7]

print(solution(5, 24) == 'TUE')