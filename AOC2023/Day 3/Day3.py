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
# def findNumber(line, j):
#     a = j -1
#     b = j +1
#     print("|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789|123456789")
#     print(line.rstrip())
#     print(j)
#     print(line[j:j+1:])
#     if line[j:j+1:].isnumeric():
#         if a < 0 or b > len(line):
#             return -2
#         if line[a:a+1:].isnumeric() and line[b:b+1:].isnumeric():
#             return  
#         if line[a:a+1:].isnumeric():
#             return findNumber(line, a)
#         return findNumber(line, b)
#     return -1


file = open("test.txt")
storedFile = []
for line in file:
    storedFile.append(line)
for i in range(len(storedFile)):
    index = 0
    line = storedFile[i].rstrip()
    symbolList = re.findall("[^0-9.]", line)
    # print(line)
    for symbol in symbolList:
        print(symbol)
        j = line[index::].find(symbol) + index
        index = j + 1
        if(i != 0):
            if storedFile[i-1][j:j+1:] != ".":
                print(re.findall('\d+', storedFile[i-1][j-1:j+1:]))
            elif storedFile[i-1][-1:j:] != ".":
                num = re.findall('\d+', storedFile[i-1][j-3:j:])
                print(num[len(num)-1])
        #     print(re.findall('\d+', storedFile[i-1][j-3:j+4:]))
        #     print(re.findall('\d+', line[j-3:j+4:]))
        # if(i != len(storedFile)-1):
        #     print(re.findall('\d+', storedFile[i+1][j-3:j+4:]))
    index = 0


        

    # while re.search("[^0-9.]", line[index]):
    #     symbol = line.find("")
