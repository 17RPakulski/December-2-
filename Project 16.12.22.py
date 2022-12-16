import random 

c = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# Greet user
print('Hello, Welcome to BlackJack')

# single player or Multiplayer
'''ADD LATER:
s_m = int(input('Would you like to play Single-Player or Multi-Player?\n\n1: Single-player     2: Multi-Player\nEnter Single-Player or Multi-Player: '))

if s_m == 1:
    print('-------------------------')
    p1 = input('Player 1 Name: ')
else:
    print('-------------------------')
    p1 = input('Player 1 Name: ')
    p2 = input('Player 2 Name: ')
'''

dealerCard = random.choice(c)
c.remove(dealerCard)