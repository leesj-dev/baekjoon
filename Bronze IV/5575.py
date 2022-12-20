for i in range(3):
    lst = list(map(int, input().split()))
    sec = lst[3] * 3600 + lst[4] * 60 + lst[5] - lst[0] * 3600 - lst[1] * 60 - lst[2]
    print(sec // 3600, (sec % 3600) // 60, sec % 60)
