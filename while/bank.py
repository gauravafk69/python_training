try:
    while True:
        user_input=input("Do you like to create an account?")
        if user_input=="yes":
            print("Welcome to our app")
        elif user_input=="no":
            print("Okay have a good day")
            break
        else:
            print("Invalid input try again")
            break
        useraccount_input=input("Enter your name")
        print("Congratulations",useraccount_input)
        userdetails_input=input("Enter your phone number")
        print("Your phone number has been registered.")
        if userdetails_input=="string":
            print("Invalid phone number try again")
            break
        useraddress_input=input("enter your address")
        print("Your address has been recorded")
        print("Your details has been recorded we will contact you soon.")
        break
except:
    print("Something went wrong.")