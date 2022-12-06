file = open("Day6Input.txt")
line = file.readline()
counter = 0
string = ""
stringLength = 14       #change stringLength for diff problems  P1=4  P2=14
for s in line:
    string = string + s
    counter+= 1
    if(len(string) == stringLength):
        index = 0
        isMarker = True
        while index < stringLength:
            if(string[index+1:].find(string[index]) != -1):
                isMarker = False
                break
            index+=1
        if(isMarker):
            print(string + " - " + str(counter))
            break
        string = string[1:]
            
