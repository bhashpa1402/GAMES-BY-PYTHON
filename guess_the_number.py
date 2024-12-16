print(">>---------- GAME START ----------<<")
max_range = int(input("Give the Maximum range of Generation : "))

import random

target = random.randint(1,max_range) # for generating target number

while True:
    userChoice = input("Guess the target or Quit(Q): ")
    
    # Quit or Exit Option
    if userChoice == 'Q':
        break
    
    userChoice = int(userChoice)  
      
    if (userChoice == target):
        print("Sucess : Correct Guess!!")
        break
    elif (userChoice > target):
        print("Your  nuber was  too big. Take a Smaller guess")
    else:
        print("Your  nuber was  too small. Take a bigger guess")
        

print("<<---------- GAME OVER ---------->>")