import random 

c = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

dealerCards = []
playerCards = []
total = 0
# Greet user
print('Hello, Welcome to BlackJack')

def ftotal(l):
    global total
    for item in l:
        if item[0] == 'A' and (total + 11)< 21:
            total += 11
            
        elif item[0] == 'A' and (total + 11)> 21:
            total += 1
        
        elif item[0] == 'K' or item[0] == 'Q' or item[0] == 'J':
            total += 10
            
        else:
            total += int(item[0])

for i in range(2):
    dealerCard = random.choice(c)
    c.remove(dealerCard)
    dealerCards.append(dealerCard)


'''
    playerCard = random.choice(c)
    c.remove(playerCard)
    playerCards.append(playerCard)
'''


print('Dealers cards:', dealerCards)
dealerTotal = ftotal(dealerCards)
print(dealerTotal)



#print('Players cards:', playerCards)

