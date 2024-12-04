def handType(hand):
    cards = {}
    numJokers = 0
    for card in hand:
        if card == 'J':
            numJokers+= 1
            continue
        if card in cards:
            cards.update({card:cards[card] +1})
        else:
            cards[card] = 1
    val = 0
    highest = ""
    for card in cards:
        if cards[card] > val:
            val = cards[card]
            highest = card
    if highest == "":
        cards["J"] = 5
    else:
        cards[highest] += numJokers
    if(len(cards) == 1):
        return 6
    values = list(cards.values())
    values.sort(reverse=True)
    if(len(cards) == 2):
        if values[0] == 4:
            return 5
        return 4
    if(len(cards) == 3):
        if values[0] == 3:
            return 3
        return 2
    if(len(cards) == 4):
        return 1
    return 0

def cardValue(card):
    match card:
        case "T":
            return 10
        case "J":
            return 1
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _ :
            return int(card)

# file = open("test.txt")
file = open("Day7Input.txt")
handTypes = {}
handBet = {}
for line in file:
    hand = line[:line.find(" "):]
    bet = int(line[line.find(" ")+1::].strip())
    handValue = handType(hand)
    handList = [cardValue(card) for card in hand]
    if handValue in handTypes:
        handTypes[handValue].append(handList)
    else:
        handTypes[handValue] = [handList]
    handBet[str(handList)] = bet
for key in handTypes:
    handTypes[key].sort()

total = 0
rank = 1
listOfHandValues = list(handTypes.keys())
listOfHandValues.sort()
for hands in listOfHandValues:
    for hand in handTypes[hands]:
        bet = handBet[str(hand)]
        total += rank * bet
        rank+= 1
print(total)

# Part 1
"""
def handType(hand):
    cards = {}
    for card in hand:
        if card in cards:
            cards.update({card:cards[card] +1})
        else:
            cards[card] = 1
    if(len(cards) == 1):
        return 6
    values = list(cards.values())
    values.sort(reverse=True)
    if(len(cards) == 2):
        if values[0] == 4:
            return 5
        return 4
    if(len(cards) == 3):
        if values[0] == 3:
            return 3
        return 2
    if(len(cards) == 4):
        return 1
    return 0

def cardValue(card):
    match card:
        case "T":
            return 10
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _ :
            return int(card)

file = open("Day7Input.txt")
handTypes = {}
handBet = {}
for line in file:
    hand = line[:line.find(" "):]
    bet = int(line[line.find(" ")+1::].strip())
    handValue = handType(hand)
    # print(handValue)
    handList = [cardValue(card) for card in hand]
    if handValue in handTypes:
        handTypes[handValue].append(handList)
    else:
        handTypes[handValue] = [handList]
    handBet[str(handList)] = bet
for key in handTypes:
    handTypes[key].sort()

total = 0
rank = 1
listOfHandValues = list(handTypes.keys())
listOfHandValues.sort()
for hands in listOfHandValues:
    for hand in handTypes[hands]:
        bet = handBet[str(hand)]
        total += rank * bet
        rank+= 1
print(total)
"""