n = int(input())
b = []

for i in range(n):
    for num in input().split():
        b.append(int(num))
        
maxPass = -1
c = 0

for i in range(0, n*2, 2):
    c -= b[i]
    c += b[i+1]
    if c > maxPass:
        maxPass = c
print(maxPass)
