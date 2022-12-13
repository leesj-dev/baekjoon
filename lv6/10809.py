letter = input()
letter_list = [letter[j] for j in range(len(letter))]
for id in range(97, 123):
    if chr(id) in letter_list:
        print(letter_list.index(chr(id)), end=" ")
    else:
        print(-1, end=" ")
