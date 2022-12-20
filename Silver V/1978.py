# 소수 list 만들기
i = 1
primes = []
while i < 1000:
    i += 1
    flg = True
    for j in range(2, i):
        if i % j == 0:
            flg = False
            break
    if flg is True:
        primes.append(i)

# 입력 받고 출력하기
n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for item in lst:
    if item in primes:
        cnt += 1
print(cnt)
