import random

suits = ["Heart", "Diamond", "Club", "Spade"]

def cardMaker(suit, number): 
    return {"suit": suit, "number": number}
def randomCardGenerator():
    return cardMaker(suits[random.randint(0, 3)], random.randint(1, 13))

# The code uses dictionaries for storing the cards. 
# Suits are stored as a string and the numbers are stored as integers, 

def randomDeckGenerator():
    deck = []

    while (len(deck) < 5):
        card = randomCardGenerator()
        if card in deck:
            # print('Already exists', deck)
            # Used for debugging purposes
            continue
        else:
            deck.append(card)

    return deck
# Self explanatory, creates a deck with five random cards. The commented out print statement can be used for demo or debugging purposes

def duplicateSuitFinder(deck):
    existingSuits = []

    for card in deck:
        if card["suit"] in existingSuits:
            return [existingSuits.index(card["suit"]), deck.index(card)]
        existingSuits.append(card["suit"])
#Finds the indexes of two cards from the same suit and returns them.

def permutationArranger(deck, number):
    deck.sort(key=lambda card: card['number'])
    smallCard = deck[0]
    mediumCard = deck[1]
    largeCard = deck[2]

    match number:
        case 1:
            return [smallCard, mediumCard, largeCard]
        case 2:
            return [smallCard, largeCard, mediumCard]
        case 3:
            return [mediumCard, smallCard, largeCard]
        case 4:
            return [mediumCard, largeCard, smallCard]
        case 5:
            return [largeCard, smallCard, mediumCard]
        case 6:
            return [largeCard, mediumCard, smallCard]



def assisstant(deck):
    newDeck = []
    duplicates = duplicateSuitFinder(deck)
    card1 = deck[duplicates[0]]
    card2 = deck[duplicates[1]]
    distance = card2["number"] - card1["number"]

    if (0 < distance and distance < 7):
        newDeck.append(card1)
        deck.remove(card2)
        deck.remove(card1)
        print(card2, "REMOVED")
    
    elif (0 > distance and distance > -7):
        newDeck.append(card2)
        deck.remove(card1)
        deck.remove(card2)
        distance = abs(distance)
        print(card1, "REMOVED")

    elif (0 < distance and distance >= 7):
        newDeck.append(card2)
        deck.remove(card1)
        deck.remove(card2)
        print(card1, "REMOVED")
        distance = 13 - distance

    elif (0 > distance and distance <= -7):
        newDeck.append(card1)
        deck.remove(card2)
        deck.remove(card1)
        print(card2, "REMOVED")
        distance = 13 + distance

    threeCards = permutationArranger(deck, distance)

    newDeck.extend(threeCards)

    return newDeck



randomDeck = randomDeckGenerator()

print("Original deck", randomDeck)
print(assisstant(randomDeck))