a, b = map(int, input().split())
damage = a * (100 - b) / 100
print("0" if damage >= 100 else "1")
