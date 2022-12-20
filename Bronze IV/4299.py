a, b = map(int, input().split())
if (a + b) % 2 == 0 and a >= b >= 0:
    c = (a + b) // 2
    d = a - c
    print(max(c, d), min(c, d))
else:
    print(-1)
