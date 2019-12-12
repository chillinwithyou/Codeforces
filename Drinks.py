n = int(input())
drinks = list(map(int, input().split()))

drinks = sum(drinks)

print(format(drinks/n, '.12f'))
