grades = ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F"))
score = int(input())
for i in range(0, len(grades)):
    if grades[i][0] <= score:
        print(grades[i][1])
        break
