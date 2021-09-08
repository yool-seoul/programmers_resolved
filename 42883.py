# 효율을 생각해보자, 단 하나의 숫자만 줄인다고 했을 때, 10자리 수가 9자리 수가됨. 
# 이때는 제일 앞자리를 더 큰수로 쓰는게 좋지 않겠나? 
# 따라서 앞자리부터 무조건 작다면 날려보자. k 만큼을 날리자. 
# 마지막까지 갔는데도 날려야 할 것이 모자른다면, 뒷자리부터 잘라내자.
def solution(number, k):
    i = 0
    while k and i+1 < len(number):
        if number[i] < number[i+1]:
            number = number[:i] + number[i+1:]  # remove number[i]
            i = i-1 if i != 0 else 0
            k -= 1
        else:
            i += 1
    return number[:-k] if k != 0 else number

#테스트 1 〉	통과 (0.01ms, 10MB)
#테스트 2 〉	통과 (0.01ms, 10.2MB)
#테스트 3 〉	통과 (0.03ms, 10.3MB)
#테스트 4 〉	통과 (0.07ms, 10MB)
#테스트 5 〉	통과 (0.26ms, 10.2MB)
#테스트 6 〉	통과 (16.59ms, 10.2MB)
#테스트 7 〉	통과 (86.72ms, 10.6MB)
#테스트 8 〉	통과 (474.38ms, 11MB)
#테스트 9 〉	통과 (54.73ms, 12.9MB)
#테스트 10 〉	실패 (시간 초과)
#테스트 11 〉	통과 (0.00ms, 10.3MB)
#테스트 12 〉	통과 (0.00ms, 10.1MB)


# 효율을 생각하지 않는 로직. 틀리진 않았음.
def solution2(number, k):
    S = list(number)
    while k:
        max = [0, 0]
        for i in range(len(S)):
            s = S[i]
            S[i] = ''
            n = int(''.join(S))
            if max[0] < n:
                max = [n, i]
            S[i] = s
        del S[max[1]]
        k -= 1
    return str(int(''.join(S)))


#테스트 1 〉	통과 (0.03ms, 10.2MB)
#테스트 2 〉	통과 (0.12ms, 10.3MB)
#테스트 3 〉	통과 (4.00ms, 10.4MB)
#테스트 4 〉	통과 (700.87ms, 10.3MB)
#테스트 5 〉	통과 (3650.52ms, 10.3MB)
#테스트 6 〉	실패 (시간 초과)
#테스트 7 〉	실패 (시간 초과)
#테스트 8 〉	실패 (시간 초과)
#테스트 9 〉	실패 (시간 초과)
#테스트 10 〉	실패 (시간 초과)
#테스트 11 〉	통과 (0.02ms, 10.3MB)
#테스트 12 〉	통과 (0.02ms, 10.3MB)

print(solution('1924', 2) == '94')
print(solution('1231234', 3) == '3234')
print(solution('4177252841', 4) == '775841')
print(solution('00000', 3) == '00')
print(solution('79', 1) == '9')
print(solution('8', 0) == '8')
#print(solution('8', 1) == '')      # 여기선 에러나지만 굳이 예외처리 하지 않겠음.
