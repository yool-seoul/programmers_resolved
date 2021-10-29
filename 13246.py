from collections import Counter
my_str = input().strip()
cnt = Counter(my_str)
m = max(cnt.values())
print(''.join(sorted([k for k, v in cnt.items() if v == m])))