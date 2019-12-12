string = input()
change = False
lowerCase = 0
upperCase = 0 

if string[0].islower():
    change = True
    if string[1:len(string)].isupper():
        string = string[0].upper()+string[1:len(string)].lower()
    else:
        for alpha in string[1:len(string)]:
            if alpha.islower():
                string = string
                break
elif len(string) == 1:
    if string.islower():
        string = string.upper()
    else:
        string = string.lower()
else:
    if string.isupper():
        string = string[0].upper() + string[1:len(string)].lower()
print(string)

