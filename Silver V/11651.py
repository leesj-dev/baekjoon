n = int(input())
coords = {}
for i in range(n):
    x, y = map(int, input().split())
    if y not in coords:
        coords[y] = []
    coords[y].append(x)
for key in sorted(coords.keys()):
    for value in sorted(coords[key]):
        print(value, key)
