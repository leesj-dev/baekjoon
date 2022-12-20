n = int(input())
for i in range(n):
    string = input()
    out = ""
    for j in range(len(string) - 1):
        if string[j] != string[j + 1]:
            out += string[j]
    out += string[len(string) - 1]
    print(out)
