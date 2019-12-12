commands = {'H', 'Q', '9', '+'}
p = input()
p = set(p)
if commands.intersection(p):
    if p.intersection({'+'}):
        if len(p.intersection(commands)) == 1:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
else:
    print("NO")
