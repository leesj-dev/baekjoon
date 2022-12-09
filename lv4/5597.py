ppl = list(range(1, 31))
attended = []
for i in range(28):
    attended.append(int(input()))
for j in attended:
    ppl.remove(j)
print(min(ppl))
print(max(ppl))
