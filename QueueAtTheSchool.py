nStuds, t = map(int, input().split())
studs = list(input())
boys = []

for i in range(nStuds):
    if studs[i] == 'B':
        if (i+t) in boys:
            boys.append(i+t-1)
        else:
            boys.append(i+t)
    print(boys)
if 'G' in studs:
    studs = list('G'*nStuds)
for boy in boys:
    while boy > nStuds - 1:
        boy -= 1
    studs[boy] = 'B'
 
print("".join(studs))
