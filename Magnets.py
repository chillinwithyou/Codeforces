n = int(input())
magnets = []

for i in range(n):
    magnets.append(input())

counter = 1

for i in range(1, n):
    if magnets[i] != magnets[i-1]:
        counter += 1
print(counter)
