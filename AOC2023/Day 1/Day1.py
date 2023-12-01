file = open("Day1Input.txt")
sum = 0
alphaNum = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
number_dict = {
    'on': 1,
    'tw': 2,
    'th': 3,
    'fo': 4,
    'fi': 5,
    'si': 6,
    'se': 7,
    'ei': 8,
    'ni': 9
}
for line in file:
    # print("-----")
    # print(line)
    # for i in range(1, 10):
    #     while(line.find(alphaNum[i]) != -1):
    #         index = line.find(alphaNum[i])
    #         line = line[:index:] + str(i) + line[(index+1)::]
    for i in range(len(line[:-1:])):
        if line[i::].startswith(alphaNum):
            line = line[:i:] + str(number_dict[line[i:i+2:]]) + line[(i+1)::]
        

    # print(line[:-1:])
    x = ""
    for c in line[:-1:]:
        if c.isnumeric() :
            x = c
            break
    # print(line[-2::-1])
    for c in line[-2::-1]:
        if c.isnumeric() :
            x += c
            break
    sum += int(x)
    # print(x)
    # print(sum)
    # print("-----")
print(sum)


# Just Part 1

# file = open("test.txt")
# sum = 0
# for line in file:
#     x = 0
#     for c in line:
#         if c.isnumeric() :
#             x = int(c) * 10
#             break
#     for c in line[::-1]:
#         if c.isnumeric() :
#             x += int(c) 
#             break
#     print(x)
#     sum += x *1
# print(sum)
