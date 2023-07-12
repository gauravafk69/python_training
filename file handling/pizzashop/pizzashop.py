my_file=open('pizza.txt','w')
a=my_file.write()
print(a)
my_file.close()
user_name=input("Enter your name or enter no to exit")
if user_name=="no":
    print("Have a good day.")
print(user_name,"Welcome to our pizza shop!")
pizzashop_menu={
    "cat pizza": 2000,
    "dog pizza": 5000,
    "human eye pizza": 1000,
    "chatpate pizza":5500,
    "mouse pizza": 3300
    }
total_amount=0.0
while True:
    item=input("Enter your order")
    if item=="done":
        break
    if item in pizzashop_menu:
        print(pizzashop_menu[item])
        price=pizzashop_menu[item]
        total_amount += price
        print(f"Added{item} to the basket. Price: {price}")
    else:
        print("Invalid item. Please try again")
print("Total bill amount", total_amount)
toppings={
    "eye": 200,
    "tail": 500,
    "neck": 100,
    "finger":500,
    "nail": 300
    }
total_bill=0.0
while True:
    item=input("Would would like to add toppings? If not enter done to exit.")
    if item=="done":
        break
    if item in toppings:
        print(toppings[item])
        price=toppings[item]
        total_bill += price
        print(f"Added{item} to the basket. Price: {price}")
    else:
        print("Invalid item. Please try again")
print("Total bill amount", total_bill)
final_amount=total_bill+total_amount
print("Your final amount is",final_amount)

