for _ in range(int(input())):
    a, b = map(int, input().split())
    b = b % 4 + (b % 4 == 0) * 4
    ans = a ** b
    print(ans % 10 + (ans % 10 == 0) * 10)