lst = []
for i in range(3):
    lst.append(int(input()))
if sum(lst) != 180:
    print("Error")
elif len(set(lst)) == 1:
    print("Equilateral")
elif len(set(lst)) == 2:
    print("Isosceles")
else:
    print("Scalene")
