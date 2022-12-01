# Question 16(a)
# Name and School: Robert Pakulski, Athlone Community College 

import random
boolean = True

l = ['A','B','C']
while boolean:
    s_name= input("Enter your surname:      ")    
    f_name= input("Enter your first name:      ")
    age = int(input('Enter your age:       '))
    eircode = input('Enter your eircode:     ')
    vacTrial = input("Do you agree to enrol in a vaccine trial?\nType 'Yes' or 'No'        ")


    if age >= 50:
        vaccine = 'ADENO'
    elif age >= 12:
        vaccine = 'MRNA'
    else:
        vaccine = 'NO'


    if int(eircode[-1]) % 2 == 0:
        vc = 'Eastwood'
    else:
        vc = 'Northfield'
     

    print("Hello", f_name, s_name + ',','you are', age,'years old and your Eircode is', eircode+'.')
    print('You must attend', vc,'for your vaccine')
    print('You are now enrolled in the trial to recieve Super Vaccine', random.choice(l))
    print(f_name+',','you will recieve the', vaccine,'vaccine')
    
    userEnd = input("If you have finished entering people's details type 'END', otherwise press RETURN: ")
    if userEnd == 'END':
        boolean = False
    else:
        pass
    
    
    
    
    



List1 = [4 ,5 ,9 ,8 ,10 ,17 ,99 ,77]
List2.copy(List1)


# i knoq i need to search for the lowest number and put it in marker and add to the second list but i dont have time





