X = int(input())
S = 0
for i in range(0, int(input())):
    a, b = map(int, input().split(" "))
    S += a * b
print("Yes" if X == S else "No")
