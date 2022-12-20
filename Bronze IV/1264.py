vowels = ["a", "e", "i", "o", "u"]
while True:
    sen = input().lower()
    if sen == "#":
        break
    else:
        n = 0
        for letter in sen:
            if letter in vowels:
                n += 1
    print(n)
