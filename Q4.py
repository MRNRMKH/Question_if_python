user_input_one=int(input('Enter First Number : '))
user_input_tow=int(input('Enter Second Number : '))

user_action=input('Choose one from (Plus[p],Multiply[mu],Minus[mi]) : ')
user_choice={'p' : 'Plus',
             'mu': 'Multiply',
             'mi': 'Minus'}

if user_action in user_choice:

    if user_action =='p':
        result=user_input_one + user_input_tow 
    elif user_action =='mu':
        result=user_input_one * user_input_tow 
    elif user_action =='mi':
        result=user_input_one - user_input_tow
else:
    print('Invalid')

print(f"{user_input_one} {user_choice[user_action]} {user_input_tow} = {result}") 