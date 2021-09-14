def solution(files):
    F = []
    for f in files:
        idx = [0, len(f)]
        for i, c in enumerate(f):
            if not idx[0] and c.isdigit():
                idx[0] = i
            elif idx[0] and not c.isdigit():
                idx[1] = i
                break
        print(idx)
        F.append([f[0:idx[0]].upper(), int(f[idx[0]:idx[1]]), f])
    F = sorted(F, key=lambda x: (x[0], x[1]))
    return [f[2] for f in F]

# 정규식 이용
import re
def solution2(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

# 또는
def solution3(files):
    r = re.compile('([a-zA-Z- .]+)([0-9]+)')
    return sorted(files,key=lambda x: (r.findall(x)[0][0].lower(),int(r.findall(x)[0][1]),files.index(x)))



print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == 
               ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]) ==
               ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
print(solution(["F-15b", "F-15a"]) == ["F-15b", "F-15a"])