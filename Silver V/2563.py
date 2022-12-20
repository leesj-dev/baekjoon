n = int(input())
total = set()
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            total.add((j, k))
print(len(total))
