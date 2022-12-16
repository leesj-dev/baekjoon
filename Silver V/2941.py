croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()
for item in croatian:
    string = string.replace(item, "*")
print(len(string))
