products={
    "iphone 14 pro max": 200000,
    "macbook": 195000,
    "airpods": 50000,
    "ipad": 145000,
    "vision": 300000
    }
total_bill=0.0
while True:
    item=input("Enter the item name")
    if item=="done":
        break
    if item in products:
        print(products[item])
        price=products[item]
        total_bill += price
        print(f"Added{item} to the cart. Price: {price}")
    else:
        print("Invalid item. Please try again")
print("Total bill amount", total_bill)