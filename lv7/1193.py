x = int(input())
n = 0
cnt = 1
while x > n:
    n += cnt
    cnt += 1
s = n - x + 1
if cnt % 2 == 0:
    print(str(s) + "/" + str(cnt - s))
else:
    print(str(cnt - s) + "/" + str(s))
