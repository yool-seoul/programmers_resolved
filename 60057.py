def solution(s):
    answer = []
    if len(s) <= 1:
        return len(s)

    for i in range(1, len(s)//2+1):
        ss = ''
        cnt = 1
        j = 0

        while j < len(s):
            k = j+i
            while k < len(s):
                s1 = s[j:j+i]
                s2 = s[k:k+i]
                
                if s1 == s2:    # matched
                    cnt += 1
                else:           # not matched
                    ss += (str(cnt) if cnt > 1 else '') + s1
                    cnt = 1
                
                if k+i >= len(s):  # remains
                    ss += (str(cnt) if cnt > 1 else '') + s2
                
                j = k
                k += i
            j += i
        answer.append(len(ss))
                    
    return min(answer)

print(solution('') == 0)

print(solution('aabbaccc') == 7)
print(solution('ababcdcdababcdcd') == 9)
print(solution('abcabcdede') == 8)
print(solution('abcabcabcabcdededededede') == 14)
print(solution('xababcdcdababcdcd') == 17)


# Best solution
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
