import math

while True:
    n = int(input())
    if n == 0:
        break

    i = 1
    primes = []
    while i < 2 * n:
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
        if n < item <= 2 * n:
            lst.append(item)
    print(len(lst))
