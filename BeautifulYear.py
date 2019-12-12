n = int(input())
a = []
while True:
    n += 1
    for i in str(n):
        if i not in a:
            a.append(i)
    if len(a) == 4:
        break
    a = []
print(n)
