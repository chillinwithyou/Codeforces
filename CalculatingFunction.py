import math

n = int(input())

def f(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return -int(math.ceil(n/2))

print(f(n))
