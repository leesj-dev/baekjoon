x = int(input())
y = int(input())
if y > 0:
    ans = 1
    if x < 0:
        ans += 1
else:
    ans = 3
    if x > 0:
        ans += 1
print(ans)
