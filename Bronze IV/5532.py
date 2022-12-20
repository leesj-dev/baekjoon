def days(arg1, arg2):
    day = arg1 // arg2
    if arg1 % arg2 != 0:
        day += 1
    return day


lst = []
for i in range(5):
    lst.append(int(input()))
a = days(lst[1], lst[3])
b = days(lst[2], lst[4])
print(lst[0] - max(a, b))
