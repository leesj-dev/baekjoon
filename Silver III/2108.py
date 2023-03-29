import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

# 산술평균
print(round(sum(lst) / n))

# 중앙값
print(lst[(n - 1) // 2])

# 최빈값
modes = Counter(lst).most_common()
if len(modes) == 1:
    print(modes[0][0])
else:
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])

# 범위
print(lst[-1] - lst[0])
