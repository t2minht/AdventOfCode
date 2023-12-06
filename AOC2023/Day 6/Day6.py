import re
time = 0
distance = 0
with open("Day6Input.txt") as file:
    temp = file.readline()
    time = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
    temp = file.readline()
    distance = int(temp[temp.find(":")+1::].strip().replace(" ", ""))
numberOfPossibleWins = 0
for j in range(time):
    # speed = j
    # remaining time = time - j
    distanceTravelled = j * (time - j)
    if distanceTravelled < distance:
        continue
    if distanceTravelled > distance:
        numberOfPossibleWins+= 1
print(numberOfPossibleWins)


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