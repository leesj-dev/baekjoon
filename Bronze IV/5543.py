lst = []
for i in range(5):
    lst.append(int(input()))

print(
    min(
        [
            lst[0] + lst[3],
            lst[0] + lst[4],
            lst[1] + lst[3],
            lst[1] + lst[4],
            lst[2] + lst[3],
            lst[2] + lst[4],
        ]
    )
    - 50
)
