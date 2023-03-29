n = input()
lst = []
for letter in n:
    lst.append(letter)
print("".join(sorted(lst, reverse=True)))
