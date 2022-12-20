import math

m, n = map(int, input().split())
i = 1
primes = []
while i < n:
    i += 1
    flg = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flg = False
            break
    if flg is True:
        primes.append(i)

lst = []
for item in primes:
    if m <= item <= n:
        lst.append(item)

for item in lst:
    print(item)
