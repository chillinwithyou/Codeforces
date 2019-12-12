n = int(input())
s = input()

d = 0

for w in s:
    if w == 'D':
        d += 1
if d > n/2:
    print("Danik")
elif d < n/2:
    print("Anton")
else:
    print("Friendship")
