def solution(rows, columns, queries):
    answer = []
    l = list(range(rows*columns+1))

    for q1, q2, q3, q4 in queries:
        row = q3 - q1
        col = q4 - q2
        idx = (q1 - 1)*columns + q2
        min = tmp = l[idx]

        for i in range(row*2+col*2-1):
            if i < row:
                idx2 = idx + columns    # dir 1
            elif i < row + col:
                idx2 = idx + 1          # dir 2
            elif i < row + col + row:
                idx2 = idx - columns    # dir 3
            else:
                idx2 = idx - 1          # dir 4

            l[idx] = l[idx2]
            idx = idx2
            min = l[idx2] if l[idx2] < min else min

        l[idx] = tmp
        answer.append(min)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))
print(solution(10, 10, [[3, 3, 3, 3]]))