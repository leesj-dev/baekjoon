num = list(map(int, input().split(" ")))
original = list(set(num))  # 중복 제거
left = num[:]  # shallow copy
for item in original:
    left.remove(item)  # 중복된 것

if len(original) == 1:
    print(10000 + num[0] * 1000)
elif len(original) == 2:
    print(1000 + left[0] * 100)
else:
    print(original[2] * 100)
