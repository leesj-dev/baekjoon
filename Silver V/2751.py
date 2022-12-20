# PyPy3
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
for item in sorted(lst):
    print(item)
