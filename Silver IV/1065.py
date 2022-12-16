n = int(input())
numbers = 0
for i in range(1, n + 1):
    i_str = str(i)
    diff = set()
    for j in range(len(i_str) - 1):
        diff.add(int(i_str[j + 1]) - int(i_str[j]))
    if len(diff) == 1 or len(i_str) == 1:
        numbers += 1
print(numbers)
