n = int(input())
counter = 0
for i in range(n):
    x, y = map(int, input().split())
    if y - x >=2 :
        counter += 1
print(counter)
