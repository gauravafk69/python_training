# For loops 
# for z in range(1,10,1{start, end , gap})
# print(z)
# z is variable 

# for g in range(1,30,3):
#     print("hello")


for c in range(1,100,1):
    opt = input("Which operation do you want?")
    a=int(input("Enter first number"))
    b=float(input("Enter second number"))
    if opt=='+':
        c = a+b
        print(c)
    elif opt == "-":
        c = a-b
        print(c)
    elif opt == "/":
        c = a/b
        print(c)
    elif opt == "*":
        c = a*b
        print(c)
    else:
        print("Invalid shutup")
