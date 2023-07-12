import random
bot_score = 0
user_score = 0
for a in range(1,20,1):
    user_input = int(input("Enter any number"))
    print("my input is"+str(user_input))
    bot_input = random.randint(0,9)
    print("Bot input is"+str(bot_input))
    if bot_input>user_input:
        bot_score+=10
        print("bot score is"+str(bot_score))
    elif user_input>bot_input:
        user_score+=10
        print("user score is"+str(user_score))
    elif user_input==bot_input:
        user_score+=5
        bot_score+=5
        print("Both scored the same")
    else:
        print("Invalid input")
