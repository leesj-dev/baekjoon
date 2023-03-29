import sys

n = int(sys.stdin.readline())
lst = [0] * 10001
for i in range(n):
    lst[int(sys.stdin.readline())] += 1
for i in range(0, len(lst)):
    if lst[i] > 0:
        for j in range(0, lst[i]):
            print(i)
