lst = []
for i in range(0, int(input())):
    x, y = map(int, input().split())
    lst.append(str(x) + " + " + str(y) + " = " + str(x + y))
for i in range(0, len(lst)):
    print("Case #" + str(i + 1) + ": " + lst[i])
