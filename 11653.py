n = int(input())
i = 1
primes = []
while True:
    # i가 소수인지 검사
    while i < n:
        i += 1
        flg = True
        for j in primes:
            if i % j == 0:
                flg = False
                break
        if flg is True:
            primes.append(i)
