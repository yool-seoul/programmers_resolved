def solution2(mylist):
    R = []
    for l in mylist:
        R += l
    return R

# the compact solution
def solution(mylist):
    return sum(mylist, [])

print(solution([[1], [2]]) == [1, 2])
print(solution([['A', 'B'], ['X', 'Y'], ['1']]) == ['A', 'B', 'X' ,'Y', '1'])