a, b = map(int, input().split())

years = 0

while True:
    if a > b:
        break
    a *= 3
    b *= 2
    years += 1
print(years)
