n = int(input())
m = list(map(int, input().split()))
counter = 0
maxSeq = 0
curr = m[0]

for i in range(1, n):
    if m[i] >= m[i-1]:
        counter += 1
    else:
        if counter > maxSeq:
            maxSeq = counter
        counter = 0
    if counter > maxSeq:
        maxSeq = counter
print(maxSeq+1)
