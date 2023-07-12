celsius=int(input("enter the temperature in celsius"))
def convert_temp():
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print ("Your temperature in fahrenheit is",convert_temp())