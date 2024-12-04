def part1(listA, listB):
    listA.sort()
    listB.sort()
    sum = 0
    for x in range(0, len(listA)):
        sum += abs(int(listA[x]) - int(listB[x]))
    print(sum)    

def part2(listA, listB):
    setA = {1}
    setA.update(listA)
    sum = 0
    for x in setA:
        sum += int(x) * listB.count(x)
    print(sum)    

file = open("Day1Input.txt")
listA = []
listB = []
for line in file:
    line = line.strip().split("   ")
    listA.append(line[0])
    listB.append(line[1])
part2(listA, listB)