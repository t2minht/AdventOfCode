file = open("Day2Input.txt")
sum = 0
for line in file:
    minCubes = {"red": 0, "green": 0, "blue": 0}
    line = line[line.find(": ")+2::]
    while len(line) > 0:
        a = line.find(",")
        b = line.find(";")
        end = 0
        if (a == -1 and b == a):
            end = len(line)
        elif b == -1 or a == -1:
            end = a if a > b else b
        else:
            end = b if a > b else a
        currentSpot = line[:end:].rstrip()
        s = currentSpot.split(" ")
        currentMin = minCubes[s[1]]
        if int(s[0]) > minCubes[s[1]] :
            minCubes[s[1]] = int(s[0])
        line = line[(end+2)::]
    power = (minCubes["red"]) * (minCubes["green"]) * (minCubes["blue"])
    sum+= power
print(sum)

# Part 1

# file = open("Day2Input.txt")
# sum = 0
# gameNum = 1
# colorCap = {"red": 12, "green": 13, "blue": 14}
# for line in file:
#     line = line[line.find(": ")+2::]
#     workingGame = True
#     while len(line) > 0:
#         a = line.find(",")
#         b = line.find(";")
#         end = 0
#         if (a == -1 and b == a):
#             end = len(line)
#         elif b == -1 or a == -1:
#             end = a if a > b else b
#         else:
#             end = b if a > b else a
#         currentSpot = line[:end:].rstrip()
#         s = currentSpot.split(" ")
#         cap = colorCap[s[1]]
#         if int(s[0]) > cap :
#             workingGame = False
#             break
#         line = line[(end+2)::]
#     sum = sum + gameNum if workingGame else sum
#     gameNum+= 1
# print(sum)