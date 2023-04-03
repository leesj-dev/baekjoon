arr = []
for n in range(int(input())):
    arr.append(list(input()))
chk = list(zip(*arr))
for item in chk:
    if len(set(item)) == 1:
        print(item[0], end="")
    else:
        print("?", end="")

"""숏코딩
for i in list(zip(*[list(input()) for _ in range(int(input()))])):
    print(i[0] if len(set(i)) == 1 else "?", end="")
"""
