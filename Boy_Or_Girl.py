a = input()
b = []

for alpha in a:
    if alpha not in b:
        b.append(alpha)
if len(b) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
