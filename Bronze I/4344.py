n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]
    cnt = 0
    for j in range(1, len(lst)):
        if lst[j] > avg:
            cnt += 1
    print("{:.3f}%".format(cnt / lst[0] * 100))
