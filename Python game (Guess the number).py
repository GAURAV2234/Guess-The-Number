## Code to guess random number B/W 1 to 10

import random

guess= False
print("This is a game where a number is selected between 1 and 10 and you have to guess it,\nif you guess it correct you win otherwise you will be given 4 more turns \n")
for i in range(5):
    a=int(input("Enter your guess:"))
    b=random.randint(1,10)
    print(b)
    if a==b:
       guess=True
       break	
    else:        
        continue
if guess:
    print("You guessed it right")
else:
    print("You lost the game")
