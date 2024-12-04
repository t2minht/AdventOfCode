import re
'''
p1 sudo code
We only care about numbers attached to symbols
So parse through each line, check for the first instance of a symbol that isn't numeric or a period
Get that j value, check all values i-1, i, i+1 on levels j-1, j, j+1 for smtg numeric
If numberic, check values j-1 and j+1 repeatedly to find the full number
* recursive outside function? check left and right of current value, if numeric, run again, if not, return upper value.
* kinda 2 pointer-y?
once you have full number, add to sum
'''
def findNumber(line, j, layer):
    partNumbers = []
    if layer == "middle":
        index = j-1
        num = ''
        while line[index: index+1:].isnumeric() and index > -1:
            num = line[index: index+1:] + num
            index -= 1
        if num != '':
            # print(num)
            partNumbers.append(int(num))
        index = j+1
        num = ''
        while line[index: index+1:].isnumeric() and index < len(line):
            num = num + line[index: index+1:]
            index += 1
        if num != '':
            # print(num)
            partNumbers.append(int(num))
    else:
        if line[j: j+1:].isnumeric():
            index = j-1
            num = '' + line[j: j+1:]
            while line[index: index+1:].isnumeric() and index > -1:
                num = line[index: index+1:] + num
                index -= 1
            index = j+1
            while line[index: index+1:].isnumeric() and index < len(line):
                num = num + line[index: index+1:]
                index += 1
            if num != '':
                # print(num)
                partNumbers.append(int(num))
        else:
            index = j-1
            num = ''
            while line[index: index+1:].isnumeric() and index > -1:
                num = line[index: index+1:] + num
                index -= 1
            if num != '':
                # print(num)
                partNumbers.append(int(num))
            index = j+1
            num = ''
            while line[index: index+1:].isnumeric() and index < len(line):
                num = num + line[index: index+1:]
                index += 1
            if num != '':
                # print(num)
                partNumbers.append(int(num))
    return partNumbers


file = open("Day3Input.txt")
storedFile = []
sum = 0
for line in file:
    storedFile.append(line)
for i in range(len(storedFile)):
    index = 0
    line = storedFile[i].rstrip()
    symbolList = re.findall("[^0-9.]", line)
    for symbol in symbolList:
        j = line[index::].find(symbol) + index
        index = j + 1
        
        partNumbers = []
        partNumbers.extend(findNumber(line, j, "middle"))
        if i > 0:
            partNumbers.extend(findNumber(storedFile[i-1], j, ""))
        if(i != len(storedFile)-1):
            partNumbers.extend(findNumber(storedFile[i+1], j, ""))
        # print(partNumbers)
        if len(partNumbers) < 2:
            continue
        product = 1
        for x in partNumbers:
            product *= x
        sum += product
    index = 0
print(sum)


# Part 1
'''
def findNumber(line, j, layer):
    sum = 0
    if layer == "middle":
        index = j-1
        num = ''
        while line[index: index+1:].isnumeric() and index > -1:
            num = line[index: index+1:] + num
            index -= 1
        if num != '':
            print(num)
            sum += int(num)
        index = j+1
        num = ''
        while line[index: index+1:].isnumeric() and index < len(line):
            num = num + line[index: index+1:]
            index += 1
        if num != '':
            print(num)
            sum += int(num)
    else:
        if line[j: j+1:].isnumeric():
            index = j-1
            num = '' + line[j: j+1:]
            while line[index: index+1:].isnumeric() and index > -1:
                num = line[index: index+1:] + num
                index -= 1
            index = j+1
            while line[index: index+1:].isnumeric() and index < len(line):
                num = num + line[index: index+1:]
                index += 1
            if num != '':
                print(num)
                sum += int(num)
        else:
            index = j-1
            num = ''
            while line[index: index+1:].isnumeric() and index > -1:
                num = line[index: index+1:] + num
                index -= 1
            if num != '':
                print(num)
                sum += int(num)
            index = j+1
            num = ''
            while line[index: index+1:].isnumeric() and index < len(line):
                num = num + line[index: index+1:]
                index += 1
            if num != '':
                print(num)
                sum += int(num)
    return sum

file = open("Day3Input.txt")
storedFile = []
sum = 0
for line in file:
    storedFile.append(line)
for i in range(len(storedFile)):
    index = 0
    line = storedFile[i].rstrip()
    symbolList = re.findall("[^0-9.]", line)
    for symbol in symbolList:
        j = line[index::].find(symbol) + index
        index = j + 1
        
        sum += findNumber(line, j, "middle")
        if i > 0:
            sum += findNumber(storedFile[i-1], j, "")
        if(i != len(storedFile)-1):
            sum += findNumber(storedFile[i+1], j, "")
    index = 0
print(sum)
'''