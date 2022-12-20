k, w, m = map(int, input().split())
ans = (w - k) // m
if (w - k) % m == 0:
    print(ans)
else:
    print(ans + 1)
