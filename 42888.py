def solution(record):
    answer = []
    u1 = dict()
    u2 = list()

    for row in record:
        cmd = row.split(' ')
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            u1[cmd[1]] = cmd[2]
        if cmd[0] == 'Enter' or cmd[0] == 'Leave':
            u2.append([cmd[0], cmd[1]])

    for c, u in u2:
        c2 = '들어왔' if c == 'Enter' else '나갔'
        answer.append(f'{u1[u]}님이 {c2}습니다.')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


# 2줄 코딩

def solution2(record):
    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]

