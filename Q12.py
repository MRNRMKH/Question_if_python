while True:

    flag = 0
    username = input('Enter username name: ')
    password = input('Enter password: ')

 
    if username == password :
        print('password username its SAME ')
        flag=1
    if len(password) < 8 :
        print('pls enter minmum 8 character')
        flag=1
    if len(password) >= 20 :
        print('maximum password length is 20 character')
        flag=1
    if len(username) <= 4 :
        print('minmum user name length 4 character')
        flag=1
    if flag == 0:
        print('correct password and user saved :)')
        break
