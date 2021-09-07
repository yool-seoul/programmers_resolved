# enumerate 쓰지 않는다. len() 호출 최소화 한다. 리스트에 값 할당 횟수도 최소화한다.
#이 코드로 효율성 통과!
def solution(prices):
    L = len(prices)
    answer =[0] * L
    for i in range(L):
        for j in range(i+1, L):
            if prices[i] > prices[j]:
                break
        answer[i] = j-i
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.48ms, 10.3MB)
# 테스트 4 〉	통과 (0.50ms, 10.3MB)
# 테스트 5 〉	통과 (0.65ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.30ms, 10.3MB)
# 테스트 8 〉	통과 (0.34ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.68ms, 10.3MB)


# 로직은 맞지만, O(N^2) list 구조에서 enumerate 함수가 시간을 의외로 많이 잡아먹음.
def solution2(prices):
    answer = [0] * len(prices)
    for i, p in enumerate(prices):
        for j, n in enumerate(prices[i+1:]):
            if n < p:
                break
        answer[i] = j+1
    answer[i] = 0
    return answer

# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.1MB)
# 테스트 3 〉	통과 (0.79ms, 10.3MB)
# 테스트 4 〉	통과 (1.05ms, 10.2MB)
# 테스트 5 〉	통과 (1.38ms, 10.2MB)
# 테스트 6 〉	통과 (0.04ms, 10.1MB)
# 테스트 7 〉	통과 (0.46ms, 10.2MB)
# 테스트 8 〉	통과 (0.64ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.1MB)
# 테스트 10 〉	통과 (1.40ms, 10.3MB)


print(solution([1,2,3,2,3]) == [4,3,1,1,0])
print(solution([90001,90002,90003,29000,90003]) == [3,2,1,1,0])
 