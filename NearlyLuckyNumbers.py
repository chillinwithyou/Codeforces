n = input()
counter = 0

for d in n:
    if d == '4' or d == '7':
        counter += 1
if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")
