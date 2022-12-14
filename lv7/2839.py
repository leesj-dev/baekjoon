n = int(input())
kg_3 = 0
for i in range(5):
    if n % 5 == 0:
        print(kg_3 + n // 5)
        break
    elif n < 0:
        print(-1)
        break
    else:
        n -= 3
        kg_3 += 1
