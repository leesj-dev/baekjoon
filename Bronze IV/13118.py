lst = list(map(int, input().split()))
x = int(input().split()[0])
print(lst.index(x) + 1 if x in lst else 0)
