# builtin module
import random
computer_score= 0
user_score=0
for a in range(1,5,1):
    user_input=int(input("ENTER ANY NUMBER"))
    print("My number is "+str(user_input))
    computer_input=random.randint(0,9)
    print("Computer input is "+str(computer_input))
    if computer_input>user_input:
        computer_score+=10
        print("Computer score is "+str(computer_score))
       
    elif user_input>computer_input:
        user_score+=10
        print("User score is "+str(user_score))

    elif user_input==computer_input:
        user_input+=0
        computer_input+=0
        print("both score the same")
    else:
        print("Invalid")

        
    