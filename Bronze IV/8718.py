x, k = map(int, input().split())
if x >= 7 * k:
    print(7000 * k)
elif x >= 3.5 * k:
    print(3500 * k)
elif x >= 1.75 * k:
    print(1750 * k)
else:
    print(0)  # 이걸 넣어야만 답이 성립. 문제 오류 같음
