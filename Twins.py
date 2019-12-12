n = int(input())
coins = list(map(int, input().split()))
amount = 0
coins.sort(reverse=True)

for i in range(n):
    amount += coins[i]
    if amount > sum(coins)/2:
        break
print(i+1)
