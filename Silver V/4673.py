sums = list(range(10000))
for n in range(10000):
    lst = [n]
    while True:  # str형으로 변환한 후 다 더하는 게 더 간단함.
        lst.append(n % 10)
        quotient = n // 10
        n = quotient
        if quotient < 10:
            lst.append(n)
            break
    if sum(lst) in sums:
        sums.remove(sum(lst))
for item in sums:
    print(item, sep="\n")
