k, n, w = map(int, input().split())

b = [i*k for i in range(1, w+1)]

a = sum(b)-n

if sum(b) > n:
    print(a)
else:
    print(0)
