# import
import random

# Initialize cards
cardList = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# variables
run = True
dealerCardList = []
playerCardList = []
playerCardList2 = []
stand = False


# functions
def giveCard(sm):
    global dealerCard
    global playerCard
    global playerCard2
    
    dealerCard = random.choice(cardList)
    cardList.remove(dealerCard)
    dealerCardList.append(dealerCard)
    
    playerCard = random.choice(cardList)
    cardList.remove(playerCard)
    playerCardList.append(playerCard)
    
    if sm == 'm':
        playerCard2 = random.choice(cardList)
        cardList.remove(playerCard2)
        playerCardList2.append(playerCard2)
        
    
    
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
    playerTotal2 = totalOfCards(playerCardList2)
    
    if sm == 's':
        # check tie
        
        if dealerTotal == 21 and playerTotal == 21:
            print('\nTie')
            return True
        
        # check blackjack
        
        elif dealerTotal == 21:
            print('\nDealer Wins!')
            return True
        elif playerTotal == 21:
            print('\nPlayer Wins!')
            return True
        
        # check bust
        elif dealerTotal > 21 and playerTotal > 21:
            print('\nBoth Bust')
            return True
        elif dealerTotal >21 and playerTotal < 21:
            print('\nDealer bust, Player Wins')
            return True
        elif playerTotal >21:
            print('\nPlayer bust, Dealer Wins')
            return True
        
        # check who has greatest value
        ########################################### check stand
        elif dealerTotal > playerTotal:
            print('Dealer Wins!')
        elif playerTotal > dealerTotal:
            print('Player Wins!')
        
    if sm == 'm': ########################## Check this
        
        # check tie
        
        if dealerTotal == 21 and playerTotal == 21 and playerTotal2 == 21:
            print('\nTie')
            return True
        
        # check blackjack
        
        if dealerTotal == 21:
            print('\nDealer Wins!')
            return True
        elif playerTotal == 21:
            print('\nPlayer Wins!')
            return True
        elif playerTotal2 == 21:
            print('\nPlayer 2 Wins!')
            
        # check bust for dealer, player and player 2
        
        elif dealerTotal > 21:
            print('\nDealerBust')
            return True
        elif playerTotal > 21:
            print('\nPlayer Bust!')
            return True
        elif playerTotal2 > 21:
            print('\nPlayer 2 Bust!')
            return True
        
        # check who has greatest value
        elif dealerTotal > playerTotal and dealerTotal > playerTotal2:
            print('\nDealer Wins!')
            return True
        elif playerTotal > dealerTotal and playerTotal > playerTotal2:
            print('\nPlayer Wins')
            return True
        elif playerTotal2 > dealerTotal and playerTotal2 > playerTotal:
            print('\nPlayer 2 Wins')
            return True
        
        
        
        '''
        elif dealerTotal >21 and playerTotal < 21:
            print('\nDealer bust, Player Wins')
            return True
        elif playerTotal >21:
            print('\nPlayer bust, Dealer Wins')
            return True
        '''
        
    
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
    print('player cards:', playerCardList)
    print('player Total:',totalOfCards(playerCardList))
    
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
        print('Player Wins!')
    else:
        print('tie')
            
print('Welcome to Blackjack!') # greeting
sm = input(' S or M ')
giveCard(sm) # give dealer and player 2 cards and add to lists
giveCard(sm)
hideFirstDealerCard()
    
printCardsAndTotal('!s')

# running game loop
while run:
    
    hitStandInput = input('\n(h)Hit or (s)Stand: ')
    
    if hitStandInput == 's':
        HitStand(hitStandInput)
        hideFirstDealerCard()
        run = False
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