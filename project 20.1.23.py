import random 

c = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

dealerCards = []
playerCards = []
total = 0
# Greet user
print('Hello, Welcome to BlackJack')

print('------------------')

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
    if user == 'h':
        dealerCard = random.choice(c)
        c.remove(dealerCard)
        dealerCards.append(dealerCard)

        playerCard = random.choice(c)
        c.remove(playerCard)
        playerCards.append(playerCard)
        



for i in range(2):
    dealerCard = random.choice(c)
    c.remove(dealerCard)
    dealerCards.append(dealerCard)

    playerCard = random.choice(c)
    c.remove(playerCard)
    playerCards.append(playerCard)



print('Dealers cards:', dealerCards)
dealerTotal = ftotal(dealerCards)
print(dealerTotal)

print('------------------')

print('Players cards:', playerCards)
playerTotal = ftotal(playerCards)
print(playerTotal)

print('------------------')

print('Hit or Stand?')
userhs = input('Enter (h) or (s): ')













