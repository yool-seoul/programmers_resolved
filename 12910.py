def solution(arr, divisor):
    answer = []
    for n in arr:
        if n%divisor == 0:
            answer.append(n)

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)


# one line coding
def solution2(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]


print(solution([5, 9, 7, 10], 5) == [5, 10])
print(solution([2, 36, 1, 3], 1) == [1, 2, 3, 36])
print(solution([3,2,6], 10) == [-1])