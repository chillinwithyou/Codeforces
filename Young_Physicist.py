n = int(input())
f = []
x, y, z = 0, 0, 0
for i in range(n):
    f.append(list(map(int, input().split())))
for i in range(n):
    x += f[i][0]
    y +=f[i][1]
    z += f[i][2]
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
