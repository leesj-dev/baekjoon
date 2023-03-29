def get(a, b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1


r, c, n = map(int, input().split())
print(get(r, n) * get(c, n))
