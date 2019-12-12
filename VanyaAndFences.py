n, h = map(int, input().split())
friends = list(map(int, input().split()))

width = 0

for f in friends:
    if f <= h:
        width += 1
    else:
        width += 2
print(width)
