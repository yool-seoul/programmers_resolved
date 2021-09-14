
def solution(dirs):
    visit = set()
    x = y = 0
    for d in dirs:
        if d == 'U' and y < 5:
            visit.add((x, y, x, y+1))   # 항상 (작은좌표, 큰좌표) 조합을 사용.
            y += 1            
        elif d == 'D' and y > -5:
            visit.add((x, y-1, x, y))
            y -= 1
        elif d == 'R' and x < 5:
            visit.add((x, y, x+1, y))
            x += 1
        elif d == 'L' and x > -5:
            visit.add((x-1, y, x, y))
            x -= 1
    return len(visit)


# 뭔가 오류가 있는데 디버깅 완벽하지 않음.
def solution2(dirs):
    MAP = [0] * 220
    px = py = 5
    for d in dirs:
        if d == 'U' and py > 0:
            py -= 1
            MAP[px*10+py+110] = 1
        elif d == 'D' and py < 10:
            MAP[px*10+py+110] = 1
            py += 1
        elif d == 'L' and px > 0:
            px -= 1
            MAP[px*10+py] = 1
        elif d == 'R' and px < 10:
            MAP[px*10+py] = 1
            px += 1
#        print(px, py, MAP.count(1))
    return MAP.count(1)



print(solution("ULURRDLLU") == 7)
print(solution("LULLLLLLU") == 7)
print(solution('L') == 1)
print(solution('LR') == 1)
print(solution('LRLRL') == 1)
print(solution('LRLRLRLRUDUDUDUD') == 2)
print(solution('ULULULULULULULULULUL') == 10)
print(solution('LURDLURDLURDLURD') == 4)
print(solution('UUUUUUUUUU') == 5)
print(solution('UUDUUDUUDUUD') == 5)
print(solution('UUDUUDUUDUUDUUD') == 5)
print(solution('DDDDDDDDDD') == 5)
print(solution('DDUDDUDDUDDU') == 5)
print(solution('DDDDDDDDDDDLLR') == 7)
print(solution('LLLLRLRLRLL') == 5)
print(solution('UUUUDUDUDUUU') == 5)
print(solution("LURDLURDLURDLURDRULD") == 7)
print(solution("RRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUULU") == 11)
print(solution('RDLUULDR') == 8)
print(solution('RDLUULDRRULDDLUR') == 12)
print(solution('RRRRRRLLLLLLL') == 7)
print(solution('RDRDRDRDRDRDRDRDRDRD') == 10)


#1, 4, 5, 6, 13, 16, 17, 18, 20