n = int(input())
friends = list(map(int, input().split()))

result = [i for i in range(n)]
i = 0

for friend in friends:
    result[friend-1] = str(i+1)
    i += 1

print(" ".join(result))
