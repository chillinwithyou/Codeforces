n = int(input())
nums = list(map(int, input().split()))

odd = []
even = []

for i in range(n):
    if nums[i] % 2 > 0:
        odd.append(i)
    else:
        even.append(i)
if len(even) > len(odd):
    print(odd[0]+1)
else:
    print(even[0]+1)
