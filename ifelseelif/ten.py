opt = input("Which operations would you like?")
a=int(input("Enter the first number"))
b=int(input("Enyer the second nnumber"))
if opt=="+":
    c=a+b
    print(c)
elif opt=="*":
    c=a*b
    print(c)
elif opt=="/":
    c=a/b
    print(c)
elif opt=="-":
    c=a-b
    print(c)
else:
    print("You have entered invbalid operation try again.")
