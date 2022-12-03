file = open("Day2Input.txt")
# scores = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]      #P1 Array
scores = ["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"]        #P2 Array
score = 0
for line in file:
    score += scores.index(line[0:3])+1
print(score)