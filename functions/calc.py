opt=input("Enter your input you twat")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
def sum(a,b):
    c=a+b
    return c 
def subtract(a,b): 
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    c=a/b
    return c
if opt=="+":
    print(sum(a,b))
elif opt=="-":
    print(subtract(a,b))
elif opt=="/":
    print(divide(a,b))
elif opt=="*":
    print(multiply(a,b))
else:
    print("You have entered wrong input you son of a nasty bitch.")