a, b = map(int, input().strip().split(' '))

# my solution
[print(''.join('*' for j in range(a))) for i in range(b)]

# best solution
print(('*'*a +'\n')*b)
