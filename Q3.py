user_input = int(input('enter price : '))

if user_input>=0:
    if user_input > 1000:
        print(" Too Expensive :) ")
    elif 1000>= user_input >500:
        print(" Expensive ;) ")
    elif 500>= user_input >100:
        print(' Normal :| ')
    elif 100>=user_input>0:
        print(' cheap :( ')
    else:
        print(" Bruhhh ")
else:
    print(" The Price Cannot be Negative :/ ")
