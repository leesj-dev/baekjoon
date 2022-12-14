def val(a, b):  # recursive function
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
