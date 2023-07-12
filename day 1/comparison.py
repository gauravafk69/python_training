a=[]
for i in range(1,4,1):
    user_input=int(input("Enter any number"))
    a.append(user_input)
    print(a)
if a[0]>a[1] and a[0]>a[2]:
    print(a[0], "greater than others.")
elif a[1]>a[0] and a[1]>a[2]:
    print(a[1], "greater than others.")
elif a[2]>a[1] and a[2]>a[0]:
    print(a[2], "greater than others.")
else:
    print("invalid output")