operation = input("Enter your input")
a_value=int(input("enter first number"))
b_value=int(input("enter second number"))
# a_parameter and b _parameter ma j rakhda ni huncha
def add(a_parameter,b_parameter): 
    sum=a_parameter+b_parameter
    return sum

def subtract(a_parameter,b_parameter):
    sub=a_parameter-b_parameter
    return sub
def divide(a_parameter,b_parameter):
    division=a_parameter/b_parameter
    return division
def multiply(a_parameter,b_parameter):
    multiple=a_parameter*b_parameter
    return multiple

# if haru def ko tala rakhne 
if operation=='+':
    name="something"
    print(add(a_value,b_value))
elif operation=="-":
    print(subtract(a_value,b_value))
elif operation=="/":
    print(divide(a_value,b_value))
elif operation=="*":
    print(multiply(a_value,b_value))
else:
    print("invalid input")
print(name)