# 입력 받기
m = int(input())
n = int(input())

# m 이하의 소수 list 만들기
i = 1
primes = []
while i < n:
    i += 1
    flg = True
    for j in range(2, i):
        if i % j == 0:
            flg = False
            break
    if flg is True:
        primes.append(i)

lst = []
for item in primes:
    if m <= item <= n:
        lst.append(item)

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))
