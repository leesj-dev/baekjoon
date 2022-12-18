lst = [pow(item, 2) for item in map(int, input().split())]
print(sum(lst) % 10)
