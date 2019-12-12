n = int(input())
groups = list(map(int, input().split()))

groups.sort(reverse=True)
taxi = 0
c = 1

for i in range(n):
    if groups[i] == 4:
        taxi += 1
        continue
    else:
        b = 0
        b += groups[i]
        groups[i] = 0
        for x in range(i+1, n):
            if groups[x] == 0:
                continue
            b += groups[x]
            if b > 4:
                b -= groups[x]
                continue
            elif b == 4:
                taxi += 1
                groups[x] = 0
                b = 0
                break
            else:
                groups[x] = 0
                continue
        if b > 0:
            taxi += 1
            continue
    c += 1
print(taxi)
