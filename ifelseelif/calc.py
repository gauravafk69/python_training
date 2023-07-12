# indentation

opt=input("Which operator do u want?")
a=int(input("enter first number"))
b=int(input("enter second number"))
if opt=="+":
    c=(a+b)
    print(c)
elif opt=="-":
    c=(a-b)
    print(c)
elif opt=="*":
    c=(a*b)
    print(c)
elif opt=="/":
    c=(a/b)
    print(c)
else:
    print("invalid operator try again")