n = int(input())
for i in range(n):
    num, a, b, c = map(int, input().split())
    if a + b + c >= 55 and a >= 11 and b >= 8 and c >= 12:
        score = "PASS"
    else:
        score = "FAIL"
    print(num, a + b + c, score)
