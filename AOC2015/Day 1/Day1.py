def p1():
    with open("Day1Input.txt") as file:
        line = file.readline()
        floor = 0
        for s in line:
            if s == "(":
                floor += 1
            else:
                floor -= 1
        print(floor)

def p2():
    with open("Day1Input.txt") as file:
        line = file.readline()
        floor = 0
        index = 1
        for s in line:
            if s == "(":
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                break
            index += 1
        print(index)