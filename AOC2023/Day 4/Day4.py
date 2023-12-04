file = open("Day4Input.txt")
numWins = {}
numCards = {}
index = 1
for line in file:
    numbers = line.split("|")
    numbers[0] = numbers[0][numbers[0].find(":")+2::].rstrip()
    numbers[1] = numbers[1][1::].rstrip()
    winners = numbers[0].split()
    scratchCards = numbers[1].split()
    matching = set(winners).intersection(scratchCards)
    numWins[index] = len(matching)
    numCards[index] = 1
    index+= 1
totalCards = 0
for i in range(1, len(numWins)+1):
    count = numCards[i]
    wins = numWins[i]
    for j in range(i+1, wins+i+1):
        numCards[j] = numCards[j] + count
    totalCards += count
print(totalCards)


#Part 1
"""
file = open("Day4Input.txt")
sum = 0
for line in file:
    numbers = line.split("|")
    numbers[0] = numbers[0][numbers[0].find(":")+2::].rstrip()
    numbers[1] = numbers[1][1::].rstrip()
    winners = numbers[0].split()
    scratchCards = numbers[1].split()
    matching = set(winners).intersection(scratchCards)
    # print(int(pow(2, len(matching)-1)))
    sum += int(pow(2, len(matching)-1))
print(sum)
"""