celsius=int(input("enter any number"))
def convert_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
fahrenheit_convert=convert_fahrenheit(celsius)
print("The temperature is",fahrenheit_convert,"F") 