# Best coding example.
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer



def solution(id_list, report, k):
    A = dict()
    B = dict()
    C = dict()

    for a in id_list:
        A[a] = 0

    for r in set(report):
        a, b = r.split()

        if b not in B:
            B[b] = 0
        B[b] += 1

        if b not in C:
            C[b] = list()
        C[b].append(a)

    for b in B:
        if B[b] >= k:
            for c in C[b]:
                A[c] += 1

    print(list(A.values()))

    return list(A.values())

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2) == [2,1,1,0])
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3) == [0,0])