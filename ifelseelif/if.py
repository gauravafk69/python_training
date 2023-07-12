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