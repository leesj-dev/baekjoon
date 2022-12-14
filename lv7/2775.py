def val(a, b):  # python3로 시간초과 남, pypy3 사용할 것
    if a == 0:
        return b
    elif b == 1:
        return 1
    else:
        return val(a, b - 1) + val(a - 1, b)


t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(val(k, n))
