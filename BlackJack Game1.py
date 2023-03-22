#BlackJack Game
'''
basic:
    1. show that you can play the game till completion. show each game is random
    2. show the inputs. gamemode, email, hitstand
    3. show each gamemode is functioning: singleplayer, multiplayer and simulation
advanced:
    1. show the table from excel that each game is saved
    2. show the model analysis and the bar charts
    3. my program is able to show analysis for two different strategies
    
    my strategies:
        1. stand if card value is above 16
        2. based off a chart
'''
# import
import os
import random
import pandas as pd
import matplotlib.pyplot as plt

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
cs = ''

results = {'Strategy':[],'Name':[],'Outcome':[]}
playerWinCount = 0
dealerWinCount = 0
tieCount = 0
bothBustCount = 0
# pandas code
l = ['Winner:']

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
    
    if sm == 's' or sm == 'x': # fix so if tie bellow 21 and eceryone stood print tie
        # check tie
        
        if dealerTotal == 21 and playerTotal == 21:
            #print('\nTie')
            l.append('Tie')
            return True, "Tie"
            
        
        # check blackjack
        
        elif dealerTotal == 21:
            # print('\nDealer Wins!')
            l.append('Dealer')
            return True, 'Dealer Wins!'
            
        elif playerTotal == 21:
            #print('\nPlayer Wins!')
            l.append('Player')
            return True, 'Player Wins!'
            
        
        # check bust
        elif dealerTotal > 21 and playerTotal > 21:
            #print('\nBoth Bust')
            l.append('Both Bust')
            return True, 'Both Bust'
            
        elif dealerTotal >21 and playerTotal < 21:
            #print('\nDealer bust, Player Wins')
            l.append('Player')
            return True, 'Dealer bust, Player Wins'
            
        elif playerTotal >21:
            #print('\nPlayer bust, Dealer Wins')
            l.append('Dealer')
            return True, 'Player bust, Dealer Wins'
            
        
        # check who has greatest value
        if stand:
            if dealerTotal > playerTotal:
                #print('Dealer Wins!')
                l.append('Dealer')
                return True , "Dealer Wins!"
                
            elif playerTotal > dealerTotal:
                #print('Player Wins!')
                l.append('Player')
                return True, 'Player Wins!'
                
            elif playerTotal == dealerTotal:
                #print('Tie!')
                l.append('Tie')
                return True, 'Tie!'
        else:
            l.append('No Win')
            return False, 'No win'
        
    elif sm == 'm': 
        
        # check tie
        if dealerTotal == 21 and playerTotal == 21 and playerTotal2==21:
            #print('\nAll Tie') 
            return True, 'All Tie'
        elif dealerTotal == 21 and playerTotal==21:
            #print('\ndealer and player Tie')
            return True, 'dealer and player Tie'
        elif dealerTotal == 21 and playerTotal2 == 21:
            #print('\ndealer and player 2 Tie')
            return True,'dealer and player 2 Tie'
        elif playerTotal == 21 and playerTotal2 == 21:
            #print('\nplayer and player 2 Tie')
            return True,'player and player 2 Tie'
        
        # check blackjack
        
        elif dealerTotal == 21:
            #print('\nDealer Wins!')
            return True,'Dealer Wins!'
        elif playerTotal == 21:
            #print('\nPlayer Wins!')
            return True,'Player Wins!'
        elif playerTotal2 == 21:
            #print('\nPlayer 2 Wins!')
            return True,'Player 2 Wins!'
            
        # check bust for dealer, player and player 2 
        
        elif dealerTotal > 21 and playerTotal > 21 and playerTotal2 > 21 :
            #print('\nAll Bust')
            return True,'All Bust'
        
        elif dealerTotal > 21 : # fixed issue here when issue where dealer and p1 bust but p1 won,
            if (playerTotal > playerTotal2) and (playerTotal < 22) :
                #print('\nPlayer  Wins')
                return True,'Player  Wins'
            
            elif(playerTotal < playerTotal2) and (playerTotal2 < 22):
                #print('\nPlayer 2 Wins')
                return True,'Player 2 Wins'
            elif playerTotal > 21 and playerTotal2 < 21:
                #print('\nPlayer 2 Wins')
                return True,'Player 2 Wins'
            
            elif playerTotal2 > 21 and playerTotal < 21:
                #print('\nplayer wins')
                return True,'player wins'
            
            elif playerTotal == playerTotal2:
                #print('\nTie between player and player 2')
                return True,'Tie between player and player 2'
        
         
        elif playerTotal > 21 :
            if(dealerTotal > playerTotal2) and dealerTotal < 21:
                #print('\nDealer  Wins')
                return True,'Dealer  Wins'
            elif(dealerTotal < playerTotal2) and playerTotal2 < 21  :
                #print('\nPlayer 2 Wins')
                return True,'Player 2 Wins'
            elif playerTotal2 > 21 and dealerTotal < 21:
                #print('\ndealer Wins')
                return True,'dealer Wins'
            elif dealerTotal == playerTotal2:
                #print('\nTie between dealer and player 2')
                return True,'Tie between dealer and player 2'
            else:
                #print('\nplayer 2 and dealer win')
                return True,'player 2 and dealer win'
            
            
        elif playerTotal2 > 21 :
            if(dealerTotal > playerTotal) :
                #print('\nDealer  Wins')
                return True,'Dealer  Wins'
            elif(dealerTotal < playerTotal) :
                #print('\nPlayer  Wins')
                return True,'Player  Wins'
            elif playerTotal > 21 and dealerTotal < 21:
                #print('\ndealer  Wins')
                return True,'dealer  Wins'
            elif playerTotal == dealerTotal:
                #print('\nTie between player and dealer')
                return True,'Tie between player and dealer'
            else:
                #print('\nplayer 2 and dealer win')
                return True,'player 2 and dealer win'
            
                
        elif dealerTotal > 21 and playerTotal < 21 and playerTotal2 > 21 :
            #print('\nPlayer Wins')
            return True,'Player Wins'
        elif dealerTotal < 21 and playerTotal > 21 and playerTotal2 > 21 :
            #print('\nDealer Wins')
            return True,'Dealer Wins'
        
        
        # check who has greatest value
        if standCount ==3:
            if dealerTotal > playerTotal and dealerTotal > playerTotal2:
                #print('\nDealer Wins!')
                return True,'Dealer Wins!'
            elif playerTotal > dealerTotal and playerTotal > playerTotal2:
                #print('\nPlayer Wins')
                return True,'Player Wins'
            elif playerTotal2 > dealerTotal and playerTotal2 > playerTotal:
                #print('\nPlayer 2 Wins')
                return True,'Player 2 Wins'
            
        
            
        # check tie if everyone stands
        if standCount == 3: # added this myslef, maybe wrong
            if (dealerTotal == playerTotal) and (dealerTotal == playerTotal2):
                #print('\nAll Tie')
                return True,'All Tie'
            
            elif (dealerTotal == playerTotal):
                #print('\nDealer and Player Tie')
                return True,'Dealer and Player Tie'
            elif (dealerTotal == playerTotal2):
                #print('\nDealer and Player 2 Tie')
                return True,'Dealer and Player 2 Tie'
            
            elif (playerTotal == playerTotal2):
                #print('\nplayer and player 2 Tie')
                return True,'player and player 2 Tie'
        else:
            return False, 'No win'   
    else:
        return False, "Invalid function call"
            
   
        
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
            
def isValid(userEmail):
    if '@' in userEmail and '.' in userEmail:
        if userEmail.index('@') > 0:
            if userEmail.index('@') < userEmail.index('.'):
                return True
    else:
        return False
      
      
def isValidStrategy(s):
    if s in ['0','1','2']:
        return True
    else:
        return False
    
def isValidHs(i):
    if i in ['h','s']:
        return True
    else:
        return False
      
print('Welcome to Blackjack!') # greeting




input_validation = ['S','M','X']
sm = input('\n("s")Singleplayer or ("m")Multiplayer or ("x")Simulation: ')
while sm.upper() not in input_validation:
    print("Please select a valid option")
    sm = input('\n("s")Singleplayer or ("m")Multiplayer or ("x")Simulation: ')

booll = True

if sm == 's': # if singleplayer
    while booll: # run loop till email is valid
        userEmail = input('\nPlayer: Enter Your Email: ') # input email 1
        if isValid(userEmail):
            print('Email Input Successful')
            booll = False # break loop
        else:
            print('Email must contain "@" and "."') # repeats loop
     
    _selection = input("""\n
    Please select one of these options:
    Strategy 1: Only stand if total >=17     ('1')
    Strategy 2: Hit on combinations in table ('2')
    No Strategy:                             ('0')
    Enter Strategy: """)
   
    while not isValidStrategy(_selection):
        print('Please input a valid strategy')
        _selection = input("""\n
        Please select one of these options:
        Strategy 1: Only stand if total >=17     ('1')
        Strategy 2: Hit on combinations in table ('2')
        No Strategy:                             ('0')
        Enter Strategy: """)



booll2 = True
if sm == 'm':
    while booll:
        userEmail = input('\nPlayer: Enter Your Email: ') # input email 1
        if isValid(userEmail):
            print('\nEmail Input Successful')
            booll = False # break loop 1
        else:
            print('\nEmail must contain "@" and "."') # repeats loop
    
    while booll2: # run loop till email is valid
        userEmail2 = input('\nPlayer 2: Enter Your Email: ') # input email 2
        if isValid(userEmail2):
            print('\nEmail Input Successful')
            booll2 = False # break loop 2
        else:
            print('\nEmail must contain "@" and "."') # repeats loop
    







if sm == 'x':
    strat = int(input('\nChoose strategy 1 or 2: '))

giveCard(sm) # give dealer and player 2 cards and add to lists
giveCard(sm)
hideFirstDealerCard()
    
printCardsAndTotal('!s')
'''
if sm == 'x':
    if dealerTotal == playerTotal:
        print('tie')
        run = False
'''
# running game loop
gameCounter = 0

def strategy_select(stra):
    global cs
    if stra == 1:
        cs = '1'
        if playerTotal >= 17: # "player" means second computer
            hitStandInput = 's'
                    
        else:
            hitStandInput = 'h'
                    
                    
    elif stra == 2: # strat 2
        cs = '2'

        if playerTotal < 12:
            hitStandInput = 'h'
            
        elif playerTotal == 12:
            if dealerCardList[-1][0] in ["6","5","4"] :
                hitStandInput = 's'
                
                
            else:
                hitStandInput = 'h'
        
        elif playerTotal >=13 and playerTotal < 17:
            if dealerCardList[-1][0] in ["6","5","4","3","2"] :
                hitStandInput = 's' #stand if playertotal >= 13 and dealerCardList shows number 2-6
                
                
            else:
                hitStandInput = 'h'
                
        else:
            hitStandInput = 's' # stand if player total >=17
            
        return hitStandInput
    
while run:
 
    if sm == 's':
        hitStandInput = input('\n("h")Hit or ("s")Stand: ')
        
        while not isValidHs(hitStandInput):
            print('Please input a valid option')
            hitStandInput = input('\n("h")Hit or ("s")Stand: ')
        
        else:
            print('unsuccessful, please try again') # repeats loop
        
        if hitStandInput == 's':
            stand = True
            while totalOfCards(dealerCardList) < 17:
                Hit(0) # COMPUTER DEALS ITSELF A CARD
            t,p =checkWin()
            print(p)
            
            
            results['Strategy'].append(_selection)
            results['Name'].append(userEmail)
                
            if(l[-1] == "Player"):
                results['Outcome'].append('Win')
            elif (l[-1] == "Dealer"):
                results['Outcome'].append('Loss')
            elif (l[-1] == "Tie"):
                results['Outcome'].append('Tie')
            else:
                results['Outcome'].append('Both Bust')
                                
                                
            run = False
            printCardsAndTotal(hitStandInput)
        else:
            Hit(1)
            if totalOfCards(dealerCardList) < 17:
                Hit(0) # COMPUTER DEALS ITSELF A CARD
                print('dealer hit')
            
            hideFirstDealerCard()
          #check here
            t,p=checkWin()
            
            if t: 
                printCardsAndTotal('s')
                print(p)
                
                
                results['Strategy'].append(_selection)
                results['Name'].append(userEmail)
                
                if(l[-1] == "Player"):
                    results['Outcome'].append('Win')
                elif (l[-1] == "Dealer"):
                    results['Outcome'].append('Loss')
                elif (l[-1] == "Tie"):
                    results['Outcome'].append('Tie')
                else:
                    results['Outcome'].append('Both Bust')
                    
                
                
                
                break
            else:
                printCardsAndTotal(hitStandInput)
                
                
                
                
                
    elif sm =='m':
        for i in range(1,3):
            if(playersPlaying[i-1]):
                if((i ==1 and totalOfCards(playerCardList) <= 21) or (i ==2 and totalOfCards(playerCardList2) <= 21)) :              
                    hitStandInput = input(f'\nPlayer{i} : (h)Hit or (s)Stand: ')
                        
                    while not isValidHs(hitStandInput):
                        print('Please input a valid option')
                        hitStandInput = input('\n("h")Hit or ("s")Stand: ')
        
                
                        
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
                            
                            t,p = checkWin()
                            print(p)
                            
                            
                            
                            '''
                            results['Strategy'].append('None')
                            results['Name'].append('Player')
                            results['Outcome'].append()
                                '''
                                
                                
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
                          t,p=checkWin()
                          print(p)
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
                        t,p = checkWin()
                        print(p)
                        run = False
                        
                        
    elif sm == 'x':
        testRun = 0
        while testRun < 1000:
            complete = False
                  
            playerTotal = totalOfCards(playerCardList)# computer 2
            dealerTotal = totalOfCards(dealerCardList)
            #hitStandInput = input('\n("h")Hit or ("s")Stand: ')
            
            hitStandInput=strategy_select(strat)
                        
            if hitStandInput == 's':
                stand = True
                while totalOfCards(dealerCardList) < 17:
                    Hit(0) # COMPUTER DEALS ITSELF A CARD
                t,p =checkWin()
                #run = False
                printCardsAndTotal(hitStandInput)
                print(p)
                results['Strategy'].append(' ' + cs)
                results['Name'].append('Player')
                results['Outcome'].append(l[-1])

                
            else: #hit
                while not complete:
                   # if strat == 1:
                        Hit(1)
                        playerTotal = totalOfCards(playerCardList)
                        hitStandInput=strategy_select(strat)
                        if (hitStandInput == 'h'):
                            if totalOfCards(dealerCardList) < 17:
                                Hit(0) # COMPUTER DEALS ITSELF A CARD
                                print('dealer hit')
                        else:
                            complete = True
                            stand = True
                            while totalOfCards(dealerCardList) < 17:
                                Hit(0) # COMPUTER DEALS ITSELF A CARD
                            t,p = checkWin()
                            if t:
                            #run = False
                                printCardsAndTotal('s')
                                print(p)
                                results['Strategy'].append(' ' + cs)
                                results['Name'].append('Player')
                                results['Outcome'].append(l[-1])
                                

                    
                    
                    
                    
            testRun += 1
            cardList = ['AH','AC','AD','AS','KH','KC','KD','KS','QH','QC','QD','QS','JH','JC','JD','JS','2H','2C','2D','2S','3H','3C','3D','3S','4H','4C','4D','4S','5H','5C','5D','5S','6H','6C','6D','6S','7H','7C','7D','7S','8H','8C','8D','8S','9H','9C','9D','9S','10H','10C','10D','10S']
            dealerCardList = []
            playerCardList = []
            playerCardList2 = []
            playersPlaying = [True,True]
            stand = False
            standCount = 0
            playersB = False
            giveCard(sm) # give dealer and player 2 cards and add to lists
            giveCard(sm)
            hideFirstDealerCard()
    
            printCardsAndTotal('!s')
                
        run =False
        
        
    
        

    
    
print('\nThank You For Playing :)')



# pandas code


    
df = pd.DataFrame(results,columns=['Strategy','Name','Outcome'])


if sm == 's':
    if os.path.isfile("singleplayer.csv"):
        df.to_csv("singleplayer.csv",mode = 'a', index = False, header = False)
    else:
        df.to_csv("singleplayer.csv",mode = 'a', index = False)
        
if sm == 'm':
    df.to_csv("multiplayer.csv",mode = 'a', index = False)
    
if sm == 'x':
    if os.path.isfile("simulation.csv"):
        df.to_csv("simulation.csv",mode = 'a', index = False, header = False)
    else:
        df.to_csv("simulation.csv",mode = 'a', index = False)
        


if sm == 'x':
    data = {'Player':playerWinCount, 'Dealer':dealerWinCount,'Tie':tieCount,'Both Bust':bothBustCount}

    types = list(data.keys())
    number = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    plt.bar(types, number, color ='maroon',width = 0.75)


    plt.ylabel("Number")
    plt.title("Bar Chart")
