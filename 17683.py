def solution(m, musicinfos):
    res = '(None)'
    max = 0
    for music in musicinfos:
        music = music.split(',', 4)

        a = music[0].split(':')
        t1 = int(a[0]) * 60 + int(a[1])
        b = music[1].split(':')
        t2 = int(b[0]) * 60 + int(b[1])
        t = t2 - t1
        
        for c1, c2 in zip(['C#', 'D#', 'F#', 'G#', 'A#'], ['1', '2', '3', '4', '5']):
            music[3] = music[3].replace(c1, c2)
            m = m.replace(c1, c2)

        mstr = ''
        while t > len(mstr):
            mstr += music[3]
        mstr = mstr[:t]

        if mstr.find(m) >= 0 and t > max:
            max = t
            res = music[2]

    return res


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]) == "HELLO")
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]) == "FOO")
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]) == "WORLD")