import random
from functions import *


random.seed(10)

with open('words.txt') as f:
    words = f.read()


word = ''
word_list = []
for char in words:
    if char == '\n':
        word_list.append(word)
        word = ''
    else:
        word = word + char

starting_word = 'crane'

print('Enter Word: ' + starting_word)
print('Enter Result')

result = input('green = g, yellow = y, grey = o: ')

possible_answers = checkWord(starting_word, word_list, result)


found = False
while not found:
    starting_word = possible_answers[0]
    print('Enter Word: ' + starting_word)
    print('Enter Result')

    result = input('green = g, yellow = y, grey = o: ')

    possible_answers = checkWord(starting_word, possible_answers, result)
    #print('Possible answers:', possible_answers)

