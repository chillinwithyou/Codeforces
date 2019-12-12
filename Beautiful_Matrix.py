a = input().split()
b = input().split()
c = input().split()
d = input().split()
e = input().split()

x, y = 0, 0

for i in range(25):
    if i < 5:
        curr = a[i]
        y = 1
        x = i + 1
    elif i < 10:
        y = 2
        x = i+1-5
        curr = b[i-5]
    elif i < 15:
        y = 3
        x = i+1-10
        curr = c[i-10]
    elif i < 20:
        y = 4
        x = i+1-15
        curr = d[i-15]
    else:
        y = 5
        x = i+1-20
        curr = e[i-20]

    if curr == '1':
        if x != 3 or y != 3:
            print(abs(x-3)+(abs(y-3)))
            break
        else:
            print(0)
