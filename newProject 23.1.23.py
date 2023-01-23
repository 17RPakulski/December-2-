import random 

#initialise all cards
c = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# Greet user
print('Hello, Welcome to BlackJack')

# initialize variables
dealerCards = []
playerCards = []
userhs = ''
dealerTotal = 0
playerTotal = 0

# functions
def ftotal(l):
    total = 0
    for item in l:
        if total == 21:
            print('Win')
        elif item[0] == 'A' and (total + 11)< 21:
            total += 11           
        elif item[0] == 'A' and (total + 11)> 21:
            total += 1       
        elif item[0] == 'K' or item[0] == 'Q' or item[0] == 'J' or len(item) == 3:
            total += 10        
        else:
            total += int(item[0])            
    return total  

def hitStand(user):
    #print('------------------\n')
    if user == 'h':
        dealerCard = random.choice(c)
        c.remove(dealerCard)
        dealerCards.append(dealerCard)
        
        playerCard = random.choice(c)
        c.remove(playerCard)
        playerCards.append(playerCard)
        
    else:
        if dealerTotal > playerTotal:
            print('Dealer Wins!')
        elif dealerTotal == playerTotal:
            print('Tie!')
            print(dealerTotal,playerTotal)
        else:
            print('You Win!')
    
    
def printCardsTotal():
    print('Dealers cards:', dealerCards)
    dealerTotal = ftotal(dealerCards)
    print(dealerTotal)
    print('------------------')
    print('Players cards:', playerCards)
    playerTotal = ftotal(playerCards)
    print(playerTotal)     
    print('------------------')
    
def giveCards():
    dealerCard = random.choice(c)
    c.remove(dealerCard)
    dealerCards.append(dealerCard)

    playerCard = random.choice(c)
    c.remove(playerCard)
    playerCards.append(playerCard)

def askHitStandInput():
    global userhs
    print('Hit or Stand?')
    userhs = input('Enter (h) or (s): ')

# game
giveCards()
giveCards()
printCardsTotal()
askHitStandInput()
hitStand(userhs)
printCardsTotal()





