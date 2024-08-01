my_list = [10,2,3,4,5,7,2]

my_list.sort()

avg = (my_list[0]+my_list[-1]) / 2

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
        

if my_list[index]>avg:
            
    print(f'avg is {avg} lower')

else:

    print (f'avg is {avg} higher')

