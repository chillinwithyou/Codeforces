n = int(input())

encountered = False
sentence = []

for i in range(n):
    if not encountered:
        sentence.append("I hate")
        encountered = True
    else:
        sentence.append("I love")
        encountered = False
print(" that ".join(sentence), end=" it")

        
