n = int(input())
lst = list(map(int, input().split()))
print(sum(lst) * 100 / max(lst) / n)
