num = []

nums = []

for i in range(4):
    num.append(int(input()))

d = int(input())

counter = int(d)

if 1 in num:
    print(d)
else:
    for i in range(1, d+1):
        if i % num[0] != 0 and i % num[1] != 0 and i % num[2] != 0 and i % num[3] != 0:
            counter -= 1
    print(counter)
