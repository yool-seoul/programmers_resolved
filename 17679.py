def solution(m, n, board):
    s = 0
    B = list(map(list, zip(*board)))

    while True:
        L = []
        for i in range(1, n):
            for j in range(1, m):
                if B[i][j] != ' ' and B[i-1][j-1] == B[i-1][j] == B[i][j-1] == B[i][j]:
                    L.append((i, j))
        if not L:
            break

        for i, j in L:
            B[i-1][j-1] = B[i-1][j] = B[i][j-1] = B[i][j] = ''

        s += sum([b.count('') for b in B])

        for i in range(n):
            B[i] = [x for x in B[i] if x != '']
            while len(B[i]) < m:
                B[i].insert(0, ' ')
    
    return s



print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15)
