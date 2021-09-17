from itertools import combinations as cb
def solution(relation):
    R = list(map(list, zip(*relation)))
    L = list(range(len(R)))
    M = []
    print(L)
    for i in L:
        for j in list(cb(L, i+1)):
            run = True
            for m in M:
                if len(set(m) - set(j)) == 0:
                    run = False
            if run:
                A = list(zip(*(R[k] for k in j)))
                if len(set(A)) == len(A):
                    M.append(j)
    return len(M)



print(solution(
    [["100","ryan","music","2"],["200","apeach","math","2"],
    ["300","tube","computer","3"],["400","con","computer","4"],
    ["500","muzi","music","3"],["600","apeach","music","2"]]) == 2)