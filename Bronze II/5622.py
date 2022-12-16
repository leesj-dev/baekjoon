time = 0
for substr in input():
    if ord(substr) <= 82:
        time += (ord(substr) - 56) // 3
    elif ord(substr) == 83:
        time += 8
    elif 84 <= ord(substr) <= 86:
        time += 9
    else:
        time += 10
print(time)
