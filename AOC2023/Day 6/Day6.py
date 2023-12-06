"""
def recursiveSearch(currTime, maxTime, distanceToBeat, incVal):
    # print(currTime)
    if(currTime * (maxTime - currTime)) < distanceToBeat:
        return 0
    # print("distance: " + str(currTime * (maxTime - currTime)))
    count=1
    count += recursiveSearch(currTime + incVal, maxTime, distanceToBeat, incVal)

    return count


import time, sys
tme = 0
distance = 0
with open("Day6Input.txt") as file:
    temp = file.readline()
    tme = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
    temp = file.readline()
    distance = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
print("maxTime: " + str(tme))
print("distance: " + str(distance))
sys.setrecursionlimit(50000000)
t0 = time.time()
numberOfPossibleWins = recursiveSearch(int(tme/2), tme, distance, 1) + recursiveSearch(int(tme/2), tme, distance, -1) -1
t1 = time.time()
print(numberOfPossibleWins)
print(t1 - t0)

#p2 - basically trimmed version of p1, but slow for big input
# 11.719378232955933 seconds
"""
import time
tme = 0
distance = 0
with open("Day6Input.txt") as file:
    temp = file.readline()
    tme = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
    temp = file.readline()
    distance = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
numberOfPossibleWins = 0
t0 = time.time()
for j in range(tme):
    # speed = j
    # remaining time = time - j
    distanceTravelled = j * (tme - j)
    if distanceTravelled < distance:
        continue
    if distanceTravelled > distance:
        numberOfPossibleWins+= 1
t1 = time.time()
print(numberOfPossibleWins)
print(t1 - t0)
# """


#p1
"""
import re
times = []
distances = []
with open("Day6Input.txt") as file:
    temp = file.readline()
    times = re.sub(' +', ' ', temp[temp.find(":")+1::]).strip().split(" ")
    temp = file.readline()
    distances = re.sub(' +', ' ', temp[temp.find(":")+1::]).strip().split(" ")
product = 1
for i in range(len(times)):
    time = int(times[i])
    distance = int(distances[i])
    numberOfPossibleWins = 0
    for j in range(time):
        # speed = j
        # remaining time = time - j
        distanceTravelled = j * (time - j)
        if distanceTravelled < distance:
            continue
        if distanceTravelled > distance:
            numberOfPossibleWins+= 1
    product *= numberOfPossibleWins
print(product)

"""