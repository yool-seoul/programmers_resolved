def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        answer += (num if sign else -1 * num)
    return answer


# Best solution
def solution2(absolutes, signs):
    return sum(num if sign else -1 * num  for num, sign in zip(absolutes, signs))


print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))