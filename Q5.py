my_list = []  # Desired amount

length=len(my_list)

if length == 0:

    print("list is empty")

else:

    if (len(my_list)) % 2 == 1 :

        index = int((len(my_list)-1) / 2)

        print(f"middle is {my_list[index]}")

    else:
            
        index = int((len(my_list)) / 2)

        middle_avg = ( my_list[index] + my_list[index-1] ) / 2

        print(f"Middle Avg is {middle_avg} ")
