score = []
for i in range(2):
    t, f, s, p, c = map(int, input().split())
    score.append(6 * t + 3 * f + 2 * s + 1 * p + 2 * c)
print(score[0], score[1])
