user_input=int(input("Enter any num"))
def check_prime():
    if user_input<2:
        return False
    for i in range(2,user_input):
        if user_input%i==0:
            return False
    return True
if check_prime():
    print(user_input,"is prime number.")
else:
    print(user_input,"is not a prime number")

