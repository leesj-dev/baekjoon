n = int(input())
for i in range(n):
    lt, wt, le, we = map(int, input().split())
    t = lt * wt
    e = le * we
    if e > t:
        print("Eurecom")
    elif e == t:
        print("Tie")
    else:
        print("TelecomParisTech")
