letters = input().strip('{}').split()
distinct = []

for c in letters:
    if c[0] not in distinct:
        distinct.append(c[0])
print(len(distinct))
