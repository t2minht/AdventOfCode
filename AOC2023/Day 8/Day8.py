def p1():
    # file = open("test.txt")
    file = open("Day8Input.txt")
    dir = file.readline().strip()
    file.readline()
    nodeDic = {}
    for line in file:
        pairings = line.strip().split(" = ")
        branch = (pairings[1][1:pairings[1].index(","):], pairings[1][pairings[1].index(" ")+1:len(pairings[1]) -1:])
        nodeDic[pairings[0]] = branch
    nodeCur = 'AAA'
    stepCount = 0
    print(nodeCur)
    while nodeCur != 'ZZZ':
        nextStep = dir[0:1:]
        dir = dir[1::] + dir[0:1]
        next = 0
        if nextStep == "R":
            next = 1
        nodeCur = nodeDic[nodeCur][next]
        stepCount += 1
        print(nodeCur)
    print(stepCount)

def p2():
    # file = open("test.txt")
    file = open("Day8Input.txt")
    dir = file.readline().strip()
    file.readline()
    nodeDic = {}
    nodeCur = []
    for line in file:
        pairings = line.strip().split(" = ")
        branch = (pairings[1][1:pairings[1].index(","):], pairings[1][pairings[1].index(" ")+1:len(pairings[1]) -1:])
        nodeDic[pairings[0]] = branch
        if pairings[0][-1::] == 'A':
            nodeCur.append(pairings[0])
    stepCount = 0
    zCount = 0
    nodeCount = len(nodeCur)
    # print(nodeCur)
    while zCount != nodeCount:
        # print(nodeCur)    
        nextStep = dir[0:1:]
        dir = dir[1::] + dir[0:1]
        next = 0
        if nextStep == "R":
            next = 1
        zCount = 0
        for i in range(nodeCount):
            nodeCur[i] = nodeDic[nodeCur[i]][next]
            if nodeCur[i][-1::] == 'Z':
                zCount+= 1
        stepCount += 1
        if zCount > 2:
            print( zCount)
    print(stepCount)

p2()