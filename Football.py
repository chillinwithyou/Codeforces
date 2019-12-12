players = input()
zero = 0
one = 0
answer = "NO"
same = 0
encountered = False

curr = players[0]

for i in range(1, len(players)):
    if curr == players[i]:
        if not encountered:
            same+=2
            encountered = True
        else:
            same += 1
    else:
        same = 0
        encountered = False
    curr = players[i]
    if same == 7:
        answer = "YES"
        break
print(answer)
