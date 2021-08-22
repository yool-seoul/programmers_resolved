def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        if pb[i+1].startswith(pb[i]):
            return False
    return True


if __name__ == '__main__':
    PB = [["119", "97674223", "1195524421"], ["123","456","789"], ["12","123","1235","567","88"], ['121212'], ['12', '132', '134', '11']]
    R = [False, True, False, True, True]
    for pb, r in zip(PB, R):
        print(solution(pb)==r)

