# import
import random

# Initialize cards
cardList = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# variables
run = True
dealerCardList = []
playerCardList = []
stand = False

player2CardList = []

# functions
def giveCard():
    global dealerCard
    global playerCard
    
    dealerCard = random.choice(cardList)
    cardList.remove(dealerCard)
    dealerCardList.append(dealerCard)
    
    playerCard = random.choice(cardList)
    cardList.remove(playerCard)
    playerCardList.append(playerCard)
    
    if sm == 'm':
        player2Card = random.choice(cardList)
        cardList.remove(player2Card)
        player2CardList.append(player2Card)
    
def totalOfCards(l):
    total = 0
    for item in l:
        if len(item) == 3:
            total += 10
        elif item[0] == 'K':
            total += 10
        elif item[0] == 'Q':
            total += 10
        elif item[0] == 'J':
            total += 10
                
        elif item[0] == '2':
            total += 2
        elif item[0] == '3':
            total += 3
        elif item[0] == '4':
            total += 4
        elif item[0] == '5':
            total += 5
        elif item[0] == '6':
            total += 6
        elif item[0] == '7':
            total += 7
        elif item[0] == '8':
            total += 8
        elif item[0] == '9':
            total += 9
                
        elif item[0] == 'A':
            if total + 10 > 21:
                total += 1
            else:
                total += 11
                    
    return total
                
def checkWin():
    dealerTotal = totalOfCards(dealerCardList)
    playerTotal = totalOfCards(playerCardList)
    
    if dealerTotal == 21:
        print('\nDealer Wins!')
        return True
    elif playerTotal == 21:
        print('\nPlayer 1 Wins!')
        return True
    
    elif dealerTotal >21 and playerTotal < 21:
        print('\nDealer bust, Player Wins')
        return True
    elif playerTotal >21:
        print('\nPlayer 1 bust, Dealer Wins')
        return True
    
    ###### add a feauture for bust

def HitStand(input):
    global stand
    dealerTotal = totalOfCards(dealerCardList)
    
    if input == 'h':
        playerCard = random.choice(cardList)
        cardList.remove(playerCard)
        playerCardList.append(playerCard)
        
        if dealerTotal < 17:
            dealerCard = random.choice(cardList)
            cardList.remove(dealerCard)
            dealerCardList.append(dealerCard)
            
    elif input == 's':
        if dealerTotal < 17:
            dealerCard = random.choice(cardList)
            cardList.remove(dealerCard)
            dealerCardList.append(dealerCard)
            stand = True
            
        standd()#checkWin()
        


def printCardsAndTotal(hitstand):
    if hitstand == 's':
        print('\nDealer cards:', dealerCardList)
    else:# print dealer and player cards and total
        print('\nDealer cards:', dealerCardList2) # print dealer and player cards and total
    print('Dealer Total:',totalOfCards(dealerCardList))
    print('player 1 cards:', playerCardList)
    print('player 1 Total:',totalOfCards(playerCardList))
    
    if sm == 'm':
        print('player 2 cards:', player2CardList)
        print('player 2 Total:',totalOfCards(player2CardList))
        
        
    
def hideFirstDealerCard():
    global dealerCardList2
    dealerCardList2 = dealerCardList.copy() # this code hides the first  dealer card
    dealerCardList2.remove(dealerCardList2[0])
    dealerCardList2.insert(0,'#')
    
def standd():
    dealerTotal = totalOfCards(dealerCardList)
    playerTotal = totalOfCards(playerCardList)
    
    if dealerTotal > playerTotal:
        print('Dealer Wins!')
    elif playerTotal > dealerTotal:
        print('Player 1 Wins!')
    else:
        print('Tie')
        

print('Welcome to Blackjack!') # greeting

sm = input('\nDo you want to play (s)Singleplayer or (m)Multiplayer? ')

giveCard() # give dealer and player 2 cards and add to lists
giveCard()

hideFirstDealerCard()
printCardsAndTotal('!s')

    

# running game loop
while run:
    
    hitStandInput = input('\nplayer 1 (h)Hit or (s)Stand: ')
    if sm == 'm':
        hitStandInput2 = input('\nplayer 2 (h)Hit or (s)Stand: ')
    
    
    if hitStandInput == 's':
        HitStand(hitStandInput)
        hideFirstDealerCard()
        
        if sm == '!m':
            run = False
        else:
            if hitStandInput2 == 's' and hitStandInput == 's':
                run = False
                ######
                ########## PPROBELMMMMM WITH SINGLE PLAYER
                
        printCardsAndTotal(hitStandInput)
    else:
        HitStand(hitStandInput)
        hideFirstDealerCard()
      
        
        if checkWin(): # checks if totals of dealer and player are 21,if true break loop
            printCardsAndTotal('s')
            
            break
        else:
            printCardsAndTotal(hitStandInput)
    
        
    
  
    
print('\nThank You For Playing :)')