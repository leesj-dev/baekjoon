a, b = map(int, input().split())
if a % 2 and b % 2:
    print(min(a, b))
else:
    print(0)
