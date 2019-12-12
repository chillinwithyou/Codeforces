n, t = map(int, input().split())
s = list(input())

for i in range(t):
    j = 1
    while j < n:
        if s[-j] == 'G' and s[-j-1] == 'B':
            s[-j] = 'B'
            s[-j-1] = 'G'
            j += 2
        else:
            j += 1
print("".join(s))
