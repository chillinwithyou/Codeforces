import math

n, index = map(int, input().split())

odd = (n-1+2)/2
even = n/2

if index <= odd:
    answer = (2*index)-1
else:
    answer = 2*(index-int(odd))

print(answer)
