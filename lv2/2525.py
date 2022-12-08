h, m = map(int, input().split(" "))
add = int(input())
mins = h * 60 + m + add
mins = mins - 1440 * (mins >= 1440)
print(mins // 60, mins % 60)
