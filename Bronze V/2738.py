n, m = map(int, input().split())
lst1, lst2 = [], []
for lst in [lst1, lst2]:
    for i in range(n):
        lst.append(list(map(int, input().split())))
for i in range(n):
    for pair in zip(lst1[i], lst2[i]):
        print(sum(pair), end=" ")
    print("")
