total_amount=0
for a in range(1,3,1):
    products={"mobile":200000,"airpods":25000,"macbook":195000,"ipad":150000,"vision":350000}
    user_input=input("which product do you like to purchase?")
    print("You purchased" +str(user_input))
def mobile():
    total_amount+=200000
    return total_amount
def airpods():
    total_amount+=25000
    return total_amount
def macbook():
    total_amount+=195000
    return total_amount
def ipad():
    total_amount+=150000
    return total_amount
def vision():
    total_amount+=350000
    return total_amount

if user_input=="mobile":
    print("Your total amount is"+str(total_amount))
elif user_input=="airpods":
     print("Your total amount is"+str(total_amount))
elif user_input=="macbook":
     print("Your total amount is"+str(total_amount))
elif user_input=="ipad":
     print("Your total amount is"+str(total_amount))
elif user_input=="vision":
    print("Your total amount is"+str(total_amount))
else:
    print("Invalid input try again")