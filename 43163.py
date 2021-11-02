def solution(begin, target, words):
    if target not in words:
        return 0

    WORDS = set(words)
    W1 = {begin}
    step = 0
    while True:
        found = False
        W2 = set()
        for w1 in list(W1):
            if w1 == target:
                return step
            
            for w0 in WORDS:
                #if len(w0)-1 == sum([1 if a == b else 0 for a, b in zip(list(w1), list(w0))]):
                if 1 == sum([a!=b for a, b in zip(list(w1), list(w0))]):
                    W2.add(w0)
                    found = True
        if found:
            W1 = W2
            WORDS -= W1
            step += 1
        else:
            return 0



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)