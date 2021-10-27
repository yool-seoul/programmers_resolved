from itertools import combinations as cb
def solution(line):
    X = []
    Y = []
    for (a1, b1, c1), (a2, b2, c2) in cb(line, 2):
        if a1*b2 != a2*b1:
            x = (b1*c2 - b2*c1)/(a1*b2 - a2*b1)
            y = (a1*c2 - a2*c1)/(a2*b1 - a1*b2)
        else:
            continue
        
        if x.is_integer() and y.is_integer():
            X.append(int(x))
            Y.append(int(y))
            
    w = max(X) - min(X) + 1
    h = max(Y) - min(Y) + 1

    L = [['.' for row in range(w)] for col in range(h)]
    for x, y in zip(X, Y):
        L[max(Y)-y][x-min(X)] = '*'
    
    R = []
    for li in L:
        R.append(str(''.join(li)))

    return R




print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]) == 
                ["....*....", ".........", ".........", "*.......*", ".........", 
                ".........", ".........", ".........", "*.......*"])
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]) == ["*.*"])
print(solution([[1, -1, 0], [2, -1, 0]]) == ["*"])
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]) == ["*"])