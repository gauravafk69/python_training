opt=input("operations")
a=int(input("enter"))
b=int(input("enter"))
for i in range(1,3,1):
    def sum():
        c=a+b
        return c
    def sub():
        c=a-b
        return c
    def mul():
        c=a*b
        return c
    def div():
        c=a/b
        return c
if opt=="+":
    print(sum())
elif opt=="-":
    print(sub())
elif opt=="*":
    print(mul())
elif opt=="/":
    print(div())
else:
    print("Invalid")