file = open("Day3Input.txt")
count = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for line in file:
    mid = int(len(line)/2)
    front = line[0:mid]
    back = line[mid:-1]
    for c in front:
        if back.find(c) != -1:
            print(front + " " + back + ": " + c + " " + str(letters.index(c) +1))
            count += letters.index(c) +1
            break
print(count)
