# import
import random

# Initialize cards
cardList = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# variables
run = True
dealerCardList = []
playerCardList = []
stand = False




player ={}
numplayers = 4
for i in range(numplayers):
    player["player "+str(i)] = []

print(player)
# functions
def giveCard(numplayers):
    global player
    global dealerCard
    global playerCard
    numcards=2
    for i in range(numplayers):
     for j in range(numcards):
         
        dealerCard = random.choice(cardList)
        cardList.remove(dealerCard)
        player["player "+str(i)].append(dealerCard)


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

'''
def checkWin(l):
    dealerTotal = totalOfCards(dealerCardList)
    playerTotal = totalOfCards(playerCardList)
    
    if dealerTotal == 21:
        print('\nDealer Wins!')
        return True
    elif playerTotal == 21:
        print('\nPlayer Wins!')
        return True
    
    elif dealerTotal >21 and playerTotal < 21:
        print('\nDealer bust, Player Wins')
        return True
    elif playerTotal >21:
        print('\nPlayer bust, Dealer Wins')
        return True
        
'''



#print(checkWin(totalCheck))

giveCard(numplayers)

totalCheck = []
for i in range(numplayers):
    totalCheck.append(totalOfCards(player["player "+str(i)]))
    
print(totalCheck)
#checkWin(totalCheck)



def checkWin(i):
    count = 0
    for z in i:
        #dealerTotal = totalOfCards(dealerCardList)
        #playerTotal = totalOfCards(playerCardList)
        
        if z == 21:
            print('\nPlayer ' + str(count) + ' Wins!')
            return True
        
        count += 1
        #elif z == 21:
            #print('\nPlayer Wins!')
            #return True
        
        #elif dealerTotal >21 and playerTotal < 21:
            #print('\nDealer bust, Player Wins')
            #return True
        #elif playerTotal >21:
            #print('\nPlayer bust, Dealer Wins')
            #return True

print('here')
print(checkWin(totalCheck))













print(player)