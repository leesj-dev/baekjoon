n = int(input())
for i in range(n):
    rep, char = input().split()
    result = ""
    for j in range(len(char)):
        result += char[j] * int(rep)
    print(result)
