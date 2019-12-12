ops = []
n = int(input())
x = 0

for i in range(n):
    ops.append(input())

for op in ops:
    if '-' in op:
        x -= 1
    elif '+' in op:
        x += 1

print(x)
