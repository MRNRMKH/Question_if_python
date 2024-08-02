my_words = input('Enter your word : ')
my_words=my_words.lower()

word_list = list(my_words)
word_list.reverse()
reversed_word = ''.join(word_list)

if my_words == reversed_word:
    print('this is palindrome')
else:
    print('this is not palindrome')