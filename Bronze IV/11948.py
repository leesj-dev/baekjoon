lst = []
for i in range(4):
    lst.append(int(input()))
e, f = int(input()), int(input())
print(sum(lst) - min(lst) + max(e, f))
