a = int(input())
counter = 0
if a % 4 == 0 or a % 7 == 0 or a % 47 == 0 or a % 744 == 0:
    ans = "YES"
else:
    for i in str(a):
        if i == '7' or i == '4':
            ans = "YES"
        else:
            counter += 1
    if counter > 0:
        ans = "NO"
print(ans)
