num=int(input("Enter any number"))
def check_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
if check_prime(num):
    print("it is a prime number")
else:
    print("it is not a prime number.")


