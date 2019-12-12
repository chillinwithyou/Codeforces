a = input().lower()
b = input().lower()
got = 0

for i in range(len(a)):
    if a[i] < b[i]:
        got = -1
        break
    elif a[i] > b[i]:
        got = 1
        break
print(got)
