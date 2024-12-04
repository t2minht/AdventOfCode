def prep(fileName):
    maps = {}
    with open(fileName) as file:
        seeds = file.readline().split(": ")
        seedLine = seeds[1].rstrip().split(" ")
        temp = []
        for i in seedLine:
            temp.append(int(i))
        seeds = []
        for i in range(0,len(temp),2):
            # seeds.append((temp[i], temp[i+1]))
            for j in range(temp[i], temp[i] + temp[i+1]):
                print(j)
                seeds.append(j)
        maps["seeds"] = seeds

        file.readline()
        
        title = ""
        codes = []
        for line in file:
            if line == '\n':
                maps[title] = codes
                title = ""
                codes = []
                continue
            if title == "":
                title = line.rstrip()[:-1:]
                continue
            numbers = line.rstrip().split(" ")
            start = int(numbers[1])
            end = start + int(numbers[2]) - 1
            valStart = int(numbers[0])
            codes.append(((start, end),valStart))
        maps[title] = codes
    return maps

maps = prep("Day5Input.txt")

seeds = maps["seeds"]

print(seeds)
for pair in maps:
    if pair == "seeds":
        continue
    seeds = convert(seeds, maps[pair])
seeds.sort()
print(seeds[0])

# Part One
'''
def prep(fileName):
    maps = {}
    with open(fileName) as file:
        seeds = file.readline().split(": ")
        maps["seeds"] = seeds[1].rstrip().split(" ")

        file.readline()
        
        title = ""
        codes = []
        for line in file:
            if line == '\n':
                maps[title] = codes
                title = ""
                codes = []
                continue
            if title == "":
                title = line.rstrip()[:-1:]
                continue
            numbers = line.rstrip().split(" ")
            start = int(numbers[1])
            end = start + int(numbers[2]) - 1
            valStart = int(numbers[0])
            codes.append(((start, end),valStart))
        maps[title] = codes
    return maps

def convert(seeds, codes):
    newSeeds = []
    print(codes)
    for i in seeds:
        added = False
        for j in codes:
            start = j[0][0]
            end = j[0][1]
            if i >= start and i <= end:
                diff = i - start
                newSeeds.append(j[1] + diff)
                added = True
                break
        if not added:
            newSeeds.append(i)
    print(newSeeds)
    return newSeeds

maps = prep("Day5Input.txt")

seeds = []
for i in maps["seeds"]:
    seeds.append(int(i))

print(seeds)
for pair in maps:
    if pair == "seeds":
        continue
    seeds = convert(seeds, maps[pair])
seeds.sort()
print(seeds[0])
'''