lst = []
for i in range(0, int(input())):
    lst.append(str(sum(map(int, input().split()))))
print("\n".join(lst))
