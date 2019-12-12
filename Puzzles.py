n, nP = map(int, input().split())
puzzles = list(map(int, input().split()))

i = 0
smallest = 100000000000000000

puzzles.sort()

#print(puzzles)

for i in range(nP):
    try:
        #print(puzzles[i], puzzles[i+n-1])
        answer = puzzles[i+n-1] - puzzles[i]
        #print(answer)
        if smallest > answer:
            smallest = answer
    except:
        break
print(smallest)

