def matrix():
    matrix = []
    for _ in range(9):
        lst = list(map(int, input().split()))
        matrix.append(lst)
    return matrix


A = matrix()
max_val = []
keys = []
for i in range(len(A)):
    max_val.append(max(A[i]))
    keys.append((i + 1, A[i].index(max(A[i])) + 1))

answer = keys[max_val.index(max(max_val))]
print(max(max_val))
print(answer[0], answer[1])
