day = int(input())
lst = list(map(int, input().split()))
cnt = 0
for item in lst:
    if item == day:
        cnt += 1
print(cnt)
