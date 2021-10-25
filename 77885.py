def solution2(numbers):
    R = []
    for n in numbers:
        n1 = n
        n2 = 1
        while True:
            if n1 % 4 == 3:
                n1 //= 2
                n2 *= 2
            else:
                R.append(n+n2)
                break
    return R



# the best code
def solution(numbers):
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) +val +1)
    return answer


print(solution([2,7]) == [3,11])
