n = int(input())
groups = list(map(int, input().split()))
groups.sort(reverse=True)

i = 0
j = n-1
counter = 0

while (i <= j):
    counter += 1
    s = 4-groups[i]
    while(groups[j]<=s and i <= j):
        s -= groups[j]
        j -= 1
    i += 1

print(counter)
