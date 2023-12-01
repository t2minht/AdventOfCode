file = open("Day5Input.txt")
stacks = ["FRW", "PWVDCMHT", "LNZMP", "RHCJ", "BTQHGPC", "ZFLWCG", "CGJZQLVW", "CVTWFRNP", "VSRGHWJ"]
print(stacks)
for line in file:
    splitUp = line.split(" ")
    numCrates = int(splitUp[1])
    startStack = int(splitUp[3])
    endStack = int(splitUp[5])
    stacks[endStack-1] = (stacks[startStack-1][:numCrates]) + stacks[endStack-1]
    stacks[startStack-1] = stacks[startStack-1][numCrates:]
    print(stacks)
tops = ""
for stack in stacks:
    tops += stack[0:1]
print(tops)

# Part 1 Solution
# file = open("Day5Input.txt")
# stacks = ["FRW", "PWVDCMHT", "LNZMP", "RHCJ", "BTQHGPC", "ZFLWCG", "CGJZQLVW", "CVTWFRNP", "VSRGHWJ"]
# print(stacks)
# for line in file:
#     splitUp = line.split(" ")
#     numCrates = int(splitUp[1])
#     startStack = int(splitUp[3])
#     endStack = int(splitUp[5])
#     stacks[endStack-1] = (stacks[startStack-1][:numCrates])[::-1] + stacks[endStack-1]
#     stacks[startStack-1] = stacks[startStack-1][numCrates:]
#     print(stacks)
# tops = ""
# for stack in stacks:
#     tops += stack[0:1]
# print(tops)