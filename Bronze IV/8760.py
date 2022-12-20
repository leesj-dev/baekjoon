n = int(input())
for i in range(n):
    w, k = map(int, input().split())
    if w % 2 and k % 2:
        print(w * (k - 1) // 2 + (w - 1) // 2)
    else:
        print(w * k // 2)
