from itertools import product 

def solution(numbers, target):
    _arr = []
    for n in numbers:
        _arr.append([n, -n])
    
    return sum([sum(a) == target for a in list(product(*_arr))])

# recursive coding
def solution2(numbers, target):
    if not numbers:
        return 1 if target == 0 else 0
    else:
        return solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0])

# another product solution
def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)



if __name__ == '__main__':

    S = [[1, 1, 1, 1, 1]]
    T = [3]
    R = [5]
    for s, t, r in zip(S,T,R):
        print(solution2(s, t)==r)
