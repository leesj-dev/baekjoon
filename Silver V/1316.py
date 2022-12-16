n = int(input())
cnt = 0
for i in range(n):
    letter = input()
    single = ""
    for i in range(len(letter) - 1):
        if letter[i + 1] != letter[i]:
            single += letter[i]
    single += letter[len(letter) - 1]
    if len(single) == len({i for i in letter}):
        cnt += 1
print(cnt)
