def solution(n, words):
    D = dict()
    c = ''
    for i, w in enumerate(words):
        if w in D or (w[0] != c and i):
            return [i%n+1, i//n+1]
        else:
            D[w] = 1
            c = w[-1]
    return [0, 0]


# best code
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3,3])
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0,0])
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1,3])