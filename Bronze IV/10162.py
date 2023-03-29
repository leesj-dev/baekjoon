a, b, c = 0, 0, 0
t = int(input())
if t % 10 != 0:
    print(-1)
else:
    while t >= 300:
        t -= 300
        a += 1
    while t >= 60:
        t -= 60
        b += 1
    while t > 0:
        t -= 10
        c += 1
    print(a, b, c)
