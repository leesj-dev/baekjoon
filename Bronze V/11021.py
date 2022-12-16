lst = []
for i in range(0, int(input())):
    lst.append(str(sum(map(int, input().split()))))
for i in range(0, len(lst)):
    print("Case #" + str(i + 1) + ": " + lst[i])
