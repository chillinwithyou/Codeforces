n, m = map(int, input().split())
points = n*m
counter = 0

while points > 0:
    points -= (n+m-1)
    n -= 1
    m -= 1
    counter += 1
if counter % 2 > 0:
    print("Akshat")
else:
    print("Malvika")
