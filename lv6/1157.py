char = input().upper()
alphabets, count = [], []
for id in range(65, 91):
    alphabets.append(chr(id))
    count.append(char.count(chr(id)))
if len([key for key, value in enumerate(count) if value == max(count)]) == 1:
    print(alphabets[count.index(max(count))])
else:
    print("?")
