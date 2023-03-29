n = input()
print(sum(map(int, list(n.replace("10", "")))) + 10 * n.count("10"))