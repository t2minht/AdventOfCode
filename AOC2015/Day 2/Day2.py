# file = open("test.txt")
def p1():
    file = open("Day2Input.txt")
    totalSqFt = 0
    for line in file:
        dimensions = line.strip().split("x")
        sides = [int(dimensions[0]) * int(dimensions[1]), int(dimensions[0]) * int(dimensions[2]), int(dimensions[2]) * int(dimensions[1])]
        sides.sort()
        totalSqFt += 2*sides[0] + 2*sides[1] + 2*sides[2] + sides[0]
    print(totalSqFt)
def p2():
    file = open("Day2Input.txt")
    totalSqFt = 0
    for line in file:
        dimensions = line.strip().split("x")
        sides = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]
        sides.sort()
        totalSqFt += (2 * sides[0] + 2*sides[1]) + (sides[0] * sides[1] * sides[2])
    print(totalSqFt)
p2()