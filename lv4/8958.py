n = int(input())
for i in range(n):
    string = input()
    score = 0
    cnt = 1
    for j in range(len(string)):
        if string[j] == "O":
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)
