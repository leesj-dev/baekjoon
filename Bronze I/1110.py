m = int(input())
n = m
i = 0
while True:
    k = (n % 10) * 10 + (n // 10 + n % 10) % 10
    i += 1
    if k == m:
        print(i)
        break
    else:
        n = k
