a = []
for i in range(5):
    a.append(input().split())

x, y = 1, 1

for row in a:
    for column in row:
        if column == '1':
            print(abs(x-3)+(abs(y-3)))
            break
        x += 1
    x -= 5
    y += 1
