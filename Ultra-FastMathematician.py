a = input()
b = input()

for i in range(len(a)):
    if a[i] == '1' and b[i] == '1':
        print('0', end='')
    elif a[i] == '0' and b[i] == '0':
        print('0', end='')
    else:
        print('1', end='')
