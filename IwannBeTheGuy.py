n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
passed = True

print("====a====", a[0]+1)
for i in range(1, a[0]+1):
    c.append(a[i])
print("====b=====", b[0]+1)
for i in range(1, b[0]+1):
    c.append(b[i])

for i in range(1, n+1):
    if (not(i in c)):
        passed = False
        print("Oh, my keyboard!")
        break

if passed:
    print("I become the guy.")
