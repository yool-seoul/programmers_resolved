from itertools import combinations as cb
def solution(orders, course):
    R = []
    for c in course:
        A = dict()
        S = []
        for o in orders:
            S += cb(sorted(o), c)

        for s in set(S):
            for o in orders:
                if set(s) - set(o) == set():
                    k = ''.join(s)
                    A[k] = A.get(k, 0) + 1
        if A:
            ma = max(A.values())
            for k, v in A.items():
                if v == ma and v > 1:
                    R.append(k)
    return sorted(R)



# collection 을 쓸 경우
import collections
import itertools

def solution2(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"])
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]) == ["WX", "XY"])
