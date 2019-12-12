a = input()
b = []

for alpha in a:
    if alpha not in b:
        b.append(alpha)
print(len(b))
