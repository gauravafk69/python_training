products={
    "apple":0.9,
    "orange":0.7,
    "banana":0.1,
    "peach":0.25
}
total_amount=0
while True:
    item=input("Enter your prod")
    if item=="done":
        break
    if item in products:
        print(products[item])
        price=products[item]
        total_amount+=price
        print(f'{item} added. total price is{price}')
    else:
        print("invalid")

print(f"Dear customer your total amount is {total_amount}")




    

