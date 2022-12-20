lst = sorted(list(map(int, input().split())))

if pow(lst[0], 2) + pow(lst[1], 2) == pow(lst[2], 2):
    print(1)
elif len(set(lst)) == 1:
    print(2)
else:
    print(0)
