def part1(data):
    safetyCounter = 0
    for line in data:
        l = line.strip()
        line = line.strip().split(" ")
        trend = 0
        safe = True
        freeSpace = False
        for i in range(0, len(line)-1):
            a = int(line[i])
            b = int(line[i+1])
            if a < b:
                if trend == -1:
                    # print(l + " " + str(a) + " " + str(b) + " wrong direction")
                    safe = False
                    break
                trend = 1
            if a > b:
                if trend == 1:
                    # print(l + " " + str(a) + " " + str(b) + " wrong direction")
                    safe = False
                    break
                trend = -1
            if abs(a - b) < 1 or abs(a-b) > 3:
                # print(l + " " + str(a) + " " + str(b) + "  value error")
                safe = False
                break
        if safe:
            # print(l + " " + "Safe")
            safetyCounter+=1
    print(safetyCounter)

def part2(data):
    print()

file = open("Day2Input.txt")
part1(file)
part2(file)
