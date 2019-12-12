s = input()
upper = 0
lower = 0

for c in s:
    if c.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(s.upper())
elif upper < lower:
    print(s.lower())
else:
    print(s.lower())
