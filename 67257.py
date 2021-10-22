import re
def solution(expression):
    FF = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    p = re.compile('[-+*]')
    M = list()

    for F in FF:
        O = p.findall(expression)
        N = p.split(expression)
        for f in F:     # order of function
            while True:            
                try:
                    i = O.index(f)
                except:
                    break
                eq = str(N.pop(i)) + str(O.pop(i)) + str(N.pop(i))
                N.insert(i, eval(eq))
        M.append(abs(N[0]))
    return max(M)


# best solution

3
4
5
6
7
8
9
10
11
12
13
def solution2(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)




print(solution("100-200*300-500+20") == 60420)
print(solution("50*6-3*2") == 300)