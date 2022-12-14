t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    x = (n - 1) // h + 1
    if x < 10:
        x = "0" + str(x)
    else:
        x = str(x)
    if n % h == 0:
        y = str(h)
    else:
        y = str(n % h)
    print(y + x)
