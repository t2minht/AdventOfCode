file = open("inputs/Day1Input.txt")
maxCal = 0
curCal = 0
for line in file:
    if line == "\n":
        maxCal = max(maxCal, curCal)
        curCal = 0
        continue
    curCal += int(line)
print(maxCal)
file.close()