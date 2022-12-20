h, m, s = map(int, input().split())
d = int(input())
sec = h * 3600 + m * 60 + s + d
hr = sec // 3600
while hr >= 24:
    hr -= 24
print(hr, (sec % 3600) // 60, sec % 60)
