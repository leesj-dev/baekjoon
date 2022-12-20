lst = []
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    lst.append(n)
print(sum(lst) // 5)
