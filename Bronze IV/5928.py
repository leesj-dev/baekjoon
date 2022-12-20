d, h, m = map(int, input().split())
ans = (d - 11) * 1440 + (h - 11) * 60 + m - 11
print(ans if ans >= 0 else -1)
