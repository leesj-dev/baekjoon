lst = []
for i in range(4):
    lst.append(int(input()))
if len(set(lst)) == 1:
    print("Fish At Constant Depth")
elif lst[0] < lst[1] < lst[2] < lst[3]:
    print("Fish Rising")
elif lst[0] > lst[1] > lst[2] > lst[3]:
    print("Fish Diving")
else:
    print("No Fish")
