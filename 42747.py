def solution(citations):
    for i in reversed(range(len(citations))):
        if i < sum([1 for c in citations if c > i]):
            return i+1
    return 0

#sorting 한 뒤에 카운팅 하은 방법도 사용가능.
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3,0,6,1,5]) == 3)