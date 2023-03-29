alphabets = [chr(i) for i in range(97, 123)]
ans = [0] * 26
for letter in input():
    ans[alphabets.index(letter)] += 1
for item in ans:
    print(item, end=" ")
