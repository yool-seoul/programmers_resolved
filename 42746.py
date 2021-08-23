# 시간초과 솔루션, But logically correct.
def solution2(numbers):
    V = []
    for num in numbers:
        idx = len(V)
        for i in range(len(V)):
            if V[i]+str(num) < str(num)+V[i]:
                idx = i
                break
        V.insert(idx, str(num))

    if V[0] == '0':
        return '0'
    else:
        return ''.join(V)


# best solution
def solution(numbers):
    V = sorted(map(str, numbers), key = lambda x: (str(x)*4)[:4], reverse = True)
    return str(int(''.join(V)))

# one line solution
def solution3(numbers):
    return str(int("".join(sorted(map(str,numbers),key= lambda x : (x*4),reverse = True))))

if __name__ == '__main__':
    S = [[6, 10, 2], [3, 30, 34, 5, 9], [0, 0]]
    R = ["6210", "9534330", "0"]
    
    for s, r in zip(S,R):
        print(solution(s)==r)
