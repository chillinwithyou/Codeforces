a = input()
check = 'hello'
index = 0

for i in range(len(a)):
    if a[i] == check[index]:
        index += 1
    if index >= 5:
        break

if index >= 5:
    print("YES")
else:
    print("NO")
