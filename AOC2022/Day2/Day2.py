file = open("Day2Input.txt")
score = 0
for line in file:
    theirHand = ord(line[0]) - ord('A') +1
    if line[2] == 'X':
        score += ((theirHand +1) % 3) +1
    elif line[2] =='Y':
        score += theirHand + 3
    else:
        score += theirHand%3 + 7
print(score)

# Part 1 Solution
# file = open("Day2Input.txt")
# score = 0
# for line in file:
#     theirHand = ord(line[0]) - ord('A') +1
#     yourHand = ord(line[2]) - ord('X') +1
#     score += yourHand
#     if(theirHand == 1 and yourHand == 3) or ((yourHand < theirHand) and not (yourHand == 1 and theirHand == 3)):
#         continue
#     if theirHand == yourHand:
#         score += 3
#     if(yourHand > theirHand) or (yourHand == 1 and theirHand == 3):
#         score += 6
# print(score)