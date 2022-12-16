n = int(input())
cnt = 1
threshold = 1
while threshold < n:
    threshold += 6 * cnt
    cnt += 1
print(cnt)
