n = int(input())
coords = {}
for i in range(n):
    x, y = map(int, input().split())
    if x not in coords:
        coords[x] = []
    coords[x].append(y)
for key in sorted(coords.keys()):
    for value in sorted(coords[key]):
        print(key, value)
