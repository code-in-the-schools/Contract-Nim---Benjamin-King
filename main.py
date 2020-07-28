numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
Score = 0

isPlayer1 = True
#Player1 = True
#Player2 = False
#def Function1(): #You want value you cna use to be returned. Might I sugest True be Player 1 and False be Player 2?

 #if 1 == isPlayer1:
   #return Player1
 #else:
    #return Player2


#Function1()

def Function2(): #This function is confusing, try reading it out ogically 
 if numbers != Score :
   fun = int(input('Enter either one or two ')) 
   NewScore = int(Score + fun)
   print(NewScore)
 else:
    print("0")
# thanks
 
Function2() # Dont forget the "()"

running = True

#Dont forget your while loop :) 


score = 0
fun = int(input('Enter either one or two ')) 
NewScore = int( 0 + fun)



PlayerChoice = int(input('Choose either Player 1 or 2'))

def player1():
 for i in range(1):
   if PlayerChoice == 1:
    print (' You Have Chosen Player1')
   else:
     print()



def player2():
 for i in range(1):
   if PlayerChoice == 2:
    print ('You Have Chosen Player2')
   else:
     print()

player2()

while running:
 if 1 == PlayerChoice:
   pass
 else:
   pass
 if Score == 20:
   running = False