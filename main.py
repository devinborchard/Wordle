import random
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

starting_word = random.choice(word_list)
print('Enter Word: '+starting_word)
print('Enter Result')

result = input('green = g, yellow = y, grey = o: ')

starting_word_list = []
for char in starting_word:
    starting_word_list.append(char)

result_list = []
for char in result:
    result_list.append(char)

'''BEGINNING TO LOGIC CHECK'''

'''removing all words that have letters that came back grey'''
possible_answers = word_list
to_be_removed = []
letter_index = 0

for item in result_list:  # for each letter checked
    if item == 'o':  # if the letter was grey

        letter = starting_word_list[letter_index]

        for word in word_list:  # get word from word list
            index = 0
            not_done = True
            while index < 5 and not_done:
                if word[index] == letter:  # if the letter is found in the word
                    if word not in to_be_removed:
                        to_be_removed.append(word)  # add word to be removed later
                    not_done = False
                index = index + 1
    letter_index = letter_index + 1

# remove the words found from possible answers
for word in to_be_removed:
    possible_answers.remove(word)
print(possible_answers)
