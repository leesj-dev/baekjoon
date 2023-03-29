a, b = map(int, input().split())
c = int(input())
print(a + b - 2 * c if a + b >= 2 * c else a + b)

# 통장 잔고를 합치지 못한다는 전제가 있다면, 아래 코드가 정확함.
"""
a, b = sorted(map(int, input().split()))
c = int(input())
if b >= c:
    b -= c
    if max(a, b) >= c:
        print(a + b - c)
    else:
        print(a + b + c)
else:
    print(a + b)
"""
