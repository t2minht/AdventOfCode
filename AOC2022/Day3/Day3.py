file = open("Day3Input.txt")
count = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = []
for line in file:
    lines.insert(0, line)
    if len(lines) == 3:
        for c in lines[0]:
            if lines[1].find(c) != -1 and lines[2].find(c) != -1:
                count += letters.index(c) +1
                break
        lines = []
print(count)


#Part 1 Solution
# file = open("Day3Input.txt")
# count = 0
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for line in file:
#     mid = int(len(line)/2)
#     front = line[0:mid]
#     back = line[mid:-1]
#     for c in front:
#         if back.find(c) != -1:
#             count += letters.index(c) +1
#             break
# print(count)
