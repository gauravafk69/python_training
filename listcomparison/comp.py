my_list=[]
for a in range(1,4,1):
    user_input=int(input("Enter any number"))
    my_list.append(user_input)
for a in range(1,4,1):
    print(my_list)
    if (my_list[0]>my_list[1]) and (my_list[0]>my_list[2]):
        print("my_list[0] is greater:",my_list[0])
    elif (my_list[1]> my_list[0]) and (my_list[1]>my_list[2]):
        print("my_list[1] is greater:",my_list[1])
    elif (my_list[2]> my_list[0]) and (my_list[2]>my_list[1]):
        print("my_list[3] is greater:",my_list[2])
    else:
        print("invalid")
