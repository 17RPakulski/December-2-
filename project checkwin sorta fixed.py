# import
import random

# Initialize cards
cardList = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']

# variables
run = True
dealerCardList = []
playerCardList = []
playerCardList2 = []
playersPlaying = [True,True]
stand = False
standCount = 0
playersB = False

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
                
def checkWin(): # issue where dealer and p1 bust but p1 won(fixed) # in maths copy in back is the outcomes # issue where if dealer and p2 have same total, there is no output
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
        if stand:
            if dealerTotal > playerTotal:
                print('Dealer Wins!')
                return True
            elif playerTotal > dealerTotal:
                print('Player Wins!')
                return True
        
    if sm == 'm': 
        print('reach checkwin sm=m')
        
        # check tie
        if dealerTotal == 21 and playerTotal == 21 and playerTotal2==21:
            print('\nAll Tie') 
            return True
        elif dealerTotal == 21 and playerTotal==21:
            print('\ndealer and player Tie')
            return True
        elif dealerTotal == 21 and playerTotal2 == 21:
            print('\ndealer and player 2 Tie')
            return True
        elif playerTotal == 21 and playerTotal2 == 21:
            print('\nplayer and player 2 Tie')
            return True
        
        # check blackjack
        
        elif dealerTotal == 21:
            print('\nDealer Wins!')
            return True
        elif playerTotal == 21:
            print('\nPlayer Wins!')
            return True
        elif playerTotal2 == 21:
            print('\nPlayer 2 Wins!')
            return True
            
        # check bust for dealer, player and player 2 
        
        elif dealerTotal > 21 and playerTotal > 21 and playerTotal2 > 21 :
            print('\nAll Bust')
            return True
        
        elif dealerTotal > 21 : # fixed issue here when issue where dealer and p1 bust but p1 won,
            if (playerTotal > playerTotal2) and (playerTotal < 22) :
                print('\nPlayer  Wins')
                return True
            
            elif(playerTotal < playerTotal2) and (playerTotal2 < 22):
                print('\nPlayer 2 Wins')
                return True
            elif playerTotal > 21 and playerTotal2 < 21:
                print('\nPlayer 2 Wins')
                return True
            elif playerTotal2 > 21:
                print('\nPlayer 2 Wins')
                return True
            
            elif playerTotal2 > 21 and playerTotal < 21:
                print('\player wins')
                return True
            
                
            
            
        elif playerTotal > 21 :
            if(dealerTotal > playerTotal2) and dealerTotal < 21:
                print('\nDealer  Wins')
                return True
            elif(dealerTotal < playerTotal2) and playerTotal2 < 21  :
                print('\nPlayer 2 Wins')
                return True
            elif playerTotal2 > 21 and dealerTotal < 21:
                print('\ndealer Wins')
                return True
            else:
                print('\nplayer 2 and dealer win')
                return True
            
            
        elif playerTotal2 > 21 :
            if(dealerTotal > playerTotal) :
                print('\nDealer  Wins')
                return True
            elif(dealerTotal < playerTotal) :
                print('\nPlayer  Wins')
                return True
            elif playerTotal > 21 and dealerTotal < 21:
                print('\ndealer  Wins')
                return True
        
            else:
                print('\nplayer 2 and dealer win')
                return True
            
                
        elif dealerTotal > 21 and playerTotal < 21 and playerTotal2 > 21 :
            print('\nPlayer Wins')
            return True
        elif dealerTotal < 21 and playerTotal > 21 and playerTotal2 > 21 :
            print('\nDealer Wins')
            return True
        
        
        # check who has greatest value
        if standCount ==3:
            if dealerTotal > playerTotal and dealerTotal > playerTotal2:
                print('\nDealer Wins!')
                return True
            elif playerTotal > dealerTotal and playerTotal > playerTotal2:
                print('\nPlayer Wins')
                return True
            elif playerTotal2 > dealerTotal and playerTotal2 > playerTotal:
                print('\nPlayer 2 Wins')
                return True
            
        
            
        # check tie if everyone stands
        if standCount == 3: # added this myslef, maybe wrong
            if (dealerTotal == playerTotal) and (dealerTotal == playerTotal2):
                print('\nAll Tie')
                return True
            
            elif (dealerTotal == playerTotal):
                print('\nDealer and Player Tie')
                return True
            elif (dealerTotal == playerTotal2):
                print('\nDealer and Player 2 Tie')
                return True
            
            elif (playerTotal == playerTotal2):
                print('\nplayer and player 2 Tie')
                return True     
        
def Hit(go):
    if go == 0:
            
            dealerCard = random.choice(cardList)
            cardList.remove(dealerCard)
            dealerCardList.append(dealerCard)
            
    if go == 1:
            playerCard = random.choice(cardList)
            cardList.remove(playerCard)
            playerCardList.append(playerCard)
            
    if go == 2:
            playerCard2 = random.choice(cardList)
            cardList.remove(playerCard2)
            playerCardList2.append(playerCard2)




def printCardsAndTotal(hitstand):
    if hitstand == 's':
        print('\nDealer cards:', dealerCardList)
    else:# print dealer and player cards and total
        print('\nDealer cards:', dealerCardList2) # print dealer and player cards and total
    print('Dealer Total:',totalOfCards(dealerCardList))
    print('player cards:', playerCardList)
    print('player Total:',totalOfCards(playerCardList))
    
    if sm == 'm':
        print('player 2  cards:', playerCardList2)
        print('player 2 Total:',totalOfCards(playerCardList2))
    
def hideFirstDealerCard():
    global dealerCardList2
    dealerCardList2 = dealerCardList.copy() # this code hides the first  dealer card
    dealerCardList2.remove(dealerCardList2[0])
    dealerCardList2.insert(0,'#')
            
print('Welcome to Blackjack!') # greeting

''' #commented so multiplayer will always be chosen
sm = input('("s")Singleplayer or ("m")Multiplayer: ')
'''
sm = 'm'
giveCard(sm) # give dealer and player 2 cards and add to lists
giveCard(sm)
hideFirstDealerCard()
    
printCardsAndTotal('!s')

# running game loop
while run:
 
    if sm == 's':
        hitStandInput = input('\n("h")Hit or ("s")Stand: ')
        if hitStandInput == 's':
            stand = True
            while totalOfCards(dealerCardList) < 17:
                Hit(0) # COMPUTER DEALS ITSELF A CARD
            checkWin()
            run = False
            printCardsAndTotal(hitStandInput)
        else:
            Hit(1)
            if totalOfCards(dealerCardList) < 17:
                Hit(0) # COMPUTER DEALS ITSELF A CARD
                print('dealer hit')
            
            hideFirstDealerCard()
          
            
            if checkWin(): 
                printCardsAndTotal('s')
                
                break
            else:
                printCardsAndTotal(hitStandInput)
    elif sm =='m':
        for i in range(1,3):
            if(playersPlaying[i-1]):
                if((i ==1 and totalOfCards(playerCardList) <= 21) or (i ==2 and totalOfCards(playerCardList2) <= 21)) :              
                    hitStandInput = input(f'\nPlayer{i} : (h)Hit or (s)Stand: ')
                        
                    if hitStandInput == 's':
                        #HitStand(hitStandInput,i)
                        playersPlaying[i-1]=False
                   # checkWin()
                   # run = False
                        printCardsAndTotal(hitStandInput)
                        if(playersPlaying[0] == False and playersPlaying[1] == False):
                            while totalOfCards(dealerCardList) < 17:
                                Hit(0) # COMPUTER DEALS ITSELF A CARD
                                print('dealer hit')
                                printCardsAndTotal('s')
                            standCount = 3
                            
                            checkWin()
                            run = False
                            
                    
                    else:
                    
                        Hit(i)
                        #check if players are bust and if so quit game
                        if(totalOfCards(playerCardList) > 21 and totalOfCards(playerCardList2) > 21):
                            playersB = True
                        if(i ==2):
                            if totalOfCards(dealerCardList) < 17:
                                Hit(0) # COMPUTER DEALS ITSELF A CARD
                        printCardsAndTotal('s')
                        
                        #hideFirstDealerCard()
                        if playersB:
                          checkWin()
                          run = False    
                        '''
                        if checkWin(): # checks if totals of dealer and player are 21,if true break loop
                            printCardsAndTotal('s')
                            
                            break
                        else:
                            printCardsAndTotal(hitStandInput)
                     '''
                        
                else:
                    if (playersPlaying[0] == False and totalOfCards(playerCardList2) > 21) or  (playersPlaying[1] == False and totalOfCards(playerCardList) > 21):
                        while totalOfCards(dealerCardList) < 17:
                                Hit(0) # COMPUTER DEALS ITSELF A CARD
                        printCardsAndTotal('s')
                        
                        #hideFirstDealerCard()
                        checkWin()
                        run = False
                            
                        
        
        
    
        

    
    
print('\nThank You For Playing :)')