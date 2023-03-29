t = int(input())
lst = list(map(int, input().split()))
cnt = 0
for item in lst:
    if item == t:
        cnt += 1
print(cnt)
