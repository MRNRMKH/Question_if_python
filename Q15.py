word=input('enter word: ')


if len(word) != 1:
    print('pls enter ONE char')
else:
    if word.isalpha():

        if word.lower() in [ 'a', 'e', 'i', 'o', 'u']:
            print('seda dar')
        else:
            print('be seda')

    else:
        print('hatman bayad az hroofe alpha estefade shavad')