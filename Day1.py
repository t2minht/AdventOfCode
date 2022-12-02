file = open("inputs/Day1Input.txt")
maxCal1 = 0
maxCal2 = 0
MaxCal3 = 0
curCal = 0
for line in file:
    if line == "\n":
        if(max(maxCal1, curCal) != maxCal1):
            maxCal3 = maxCal2
            maxCal2 = maxCal1
            maxCal1 = curCal
        elif(max(maxCal2, curCal) != maxCal2):
            maxCal3 = maxCal2
            maxCal2 = curCal
        elif(max(maxCal3, curCal) != maxCal3):
            maxCal3 = curCal
        curCal = 0
        continue
    curCal += int(line)
print("1: \t" + str(maxCal1))
print("2: \t" + str(maxCal2))
print("3: \t" + str(maxCal3))
print("Total: " + str(maxCal1 + maxCal2 + maxCal3))
file.close()

# Part 1 Solution
# file = open("inputs/Day1Input.txt")
# maxCal = 0
# curCal = 0
# for line in file:
#     if line == "\n":
#         maxCal = max(maxCal, curCal)
#         curCal = 0
#         continue
#     curCal += int(line)
# print(maxCal)
# file.close()