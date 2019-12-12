n = int(input())
order = list(map(int, input().split()))

lowest = 101
highest = 0
x, y = 0, 0
counter = 0

for i in range(n):
    if order[i] > highest:
        highest = order[i]
        x = i
    if order[i] <= lowest:
        lowest = order[i]
        y = i

while x > 0:
    counter += 1
    tmp, order[x-1] = order[x-1], highest
    order[x] = tmp
    x -= 1
    if x == y:
        y += 1
while y < n-1:
    counter += 1
    tmp, order[y+1] = order[y+1], lowest
    order[y] = tmp
    y += 1
print(counter)
