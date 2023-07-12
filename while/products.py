products={
    "apple":20,
    "ball":30,
    "dog":20
}
total_amount=0
while True:
    item=input("What do u want?")
    if item=="done":
        break
    if item in products:
        print(products[item])
        price=products[item]
        total_amount+=price
        print(f"added {item} to the basket and your your bill is {price}")
    else:
        print("invalid")
print(f"Your total bill amount is {total_amount} ")
