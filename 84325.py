def solution(table, languages, preference):
    depts = dict()    # Contents, Game, Hardware, Portal, SI  
    score = []
    for t in table:
        a = t.split(' ')
        depts[a[0]] = dict(zip(a[1:], [5, 4, 3, 2, 1]))

    for dept in depts:
        s = 0
        for l, p in zip(languages, preference):
            v = depts[dept].get(l)
            s += (v * p) if v != None else 0
        score.append((s, dept))

    score.sort(key=lambda x: (-x[0], x[1]))   # sort by score and name
    _, B = zip(*score)

    return B[0]

# simpler code
def solution2(table, languages, preference):
    depts = dict()    # Contents, Game, Hardware, Portal, SI  
    score = []
    for t in table:
        a = t.split(' ')
        depts[a[0]] = dict(zip(a[1:], [5, 4, 3, 2, 1]))
        s = 0
        for l, p in zip(languages, preference):
            v = depts[a[0]].get(l)
            s += (v * p) if v != None else 0
        score.append((s, a[0]))

    score.sort(key=lambda x: (-x[0], x[1]))   # sort by score and name
    _, B = zip(*score)
    return B[0]

# best solution
def solution3(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) +  (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key = lambda item: [-item[1], item[0]])[0][0]

# one line solution
solution4 = lambda t, l, p: sorted((sum(p[l.index(u)] * (i - 5) if u in l else 0 for i, u in enumerate(v)), k) for k, *v in (b.split() for b in t))[0][1]



T = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
    "GAME C++ C# JAVASCRIPT C JAVA"]
L = ["PYTHON", "C++", "SQL"]
P = [7, 5, 5]
R = "HARDWARE"
print(solution2(T, L, P) == R)

L = ["JAVA", "JAVASCRIPT"]
P = [7, 5]
R = "PORTAL"
print(solution4(T, L, P) == R)