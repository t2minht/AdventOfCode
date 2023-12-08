def mapFormat(map):
    for line in map:
        print(line)
    print("")
def p1():
    with open("Day3Input.txt") as file:
        houseCount = 1
        line = file.readline()
        tracker = ["x"]
        xMaxLength = 1
        xOrigin = 0
        yOrigin = 0
        xCur = 0
        yCur = 0
        backgroundChar = "_"
        for dir in line:
            # print(str(xCur) + " " + str(yCur))
            # mapFormat(tracker)
            match dir:
                case '^':       # up
                    if yCur == 0:
                        temp = ""
                        for i in range(xMaxLength):
                            temp += backgroundChar
                        tracker.insert(0, temp)
                        yOrigin += 1
                    else:
                        yCur -= 1
                case 'v':       # down
                    if yCur == len(tracker) -1:
                        temp = ""
                        for i in range(xMaxLength):
                            temp += backgroundChar
                        tracker.append(temp)
                    yCur += 1
                case '>':       # left
                    if xCur == xMaxLength -1:
                        for i in range(len(tracker)):
                            tracker[i] = tracker[i] + backgroundChar
                        xMaxLength += 1
                    xCur += 1
                case '<':         # right
                    if xCur == 0:
                        for i in range(len(tracker)):
                            tracker[i] = backgroundChar + tracker[i]
                        xOrigin += 1
                        xMaxLength += 1
                    else:
                        xCur -= 1
            if tracker[yCur][xCur:xCur+1:] == backgroundChar:
                houseCount +=1
                tracker[yCur] = tracker[yCur][:xCur:] + "x" + tracker[yCur][xCur+1::]    
        # print(str(xCur) + " " + str(yCur))
        mapFormat(tracker)
        print(houseCount)
            
def p2():
    with open("Day3Input.txt") as file:
        houseCount = 1
        line = file.readline()
        tracker = ["x"]
        xMaxLength = 1
        xOther = 0
        yOther = 0
        xCur = 0
        yCur = 0
        backgroundChar = " "
        santa = "x"
        robo = "_"
        charCur = santa
        switchRobo = True
        for dir in line:
            # print(str(xCur) + " " + str(yCur))
            # mapFormat(tracker)
            match dir:
                case '^':       # up
                    if yCur == 0:
                        temp = ""
                        for i in range(xMaxLength):
                            temp += backgroundChar
                        tracker.insert(0, temp)
                        yOther += 1
                    else:
                        yCur -= 1
                case 'v':       # down
                    if yCur == len(tracker) -1:
                        temp = ""
                        for i in range(xMaxLength):
                            temp += backgroundChar
                        tracker.append(temp)
                    yCur += 1
                case '>':       # left
                    if xCur == xMaxLength -1:
                        for i in range(len(tracker)):
                            tracker[i] = tracker[i] + backgroundChar
                        xMaxLength += 1
                    xCur += 1
                case '<':         # right
                    if xCur == 0:
                        for i in range(len(tracker)):
                            tracker[i] = backgroundChar + tracker[i]
                        xOther += 1
                        xMaxLength += 1
                    else:
                        xCur -= 1
            if tracker[yCur][xCur:xCur+1:] == backgroundChar:
                houseCount +=1
            tracker[yCur] = tracker[yCur][:xCur:] + charCur + tracker[yCur][xCur+1::] 
            tempX = xCur
            tempY = yCur
            xCur = xOther
            yCur = yOther
            xOther = tempX
            yOther = tempY   
            if switchRobo:
                charCur = robo
            else:
                charCur = santa
            switchRobo = not switchRobo
        # print(str(xCur) + " " + str(yCur))
        mapFormat(tracker)
        print(houseCount)
p1()
p2()
#^>v<^>v<^^>>v<