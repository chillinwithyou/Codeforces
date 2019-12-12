a = input().split('+')
a.sort()

s = a[0]
if len(a) > 1:
    for i in range(1, len(a)):
        s = s+'+'+a[i]
print(s)
