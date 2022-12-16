h, m = map(int, input().split())
mins = h * 60 + m - 45
if mins < 0:
    mins += 1440
print(mins // 60, mins % 60)
