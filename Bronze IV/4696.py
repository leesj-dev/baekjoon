while True:
    n = float(input())
    if n == 0:
        break
    else:
        print("{:.2f}".format(1 + n + pow(n, 2) + pow(n, 3) + pow(n, 4)))
