
def checkWord(starting_word, word_list, result):

    starting_word_list = []
    for char in starting_word:
        starting_word_list.append(char)

    result_list = []
    for char in result:
        result_list.append(char)

    '''BEGINNING TO LOGIC CHECK'''

    possible_answers = word_list
    to_be_removed = []
    letter_index = 0

    '''removing all words that have letters that came back grey'''

    for char in starting_word_list:
        for word in possible_answers:
            if result_list[letter_index] == 'o' and word.__contains__(char):
                to_be_removed.append(word)
        letter_index = letter_index + 1;

    for word in to_be_removed:
        if possible_answers.__contains__(word):
            possible_answers.remove(word)

    # print(possible_answers)

    '''removing words with yellow letters'''

    yellow_letters = []
    yellow_indexes = []
    to_be_removed = []

    for count, letter in enumerate(starting_word_list):
        if result_list[count] == 'y':
            yellow_letters.append(letter)
            yellow_indexes.append(count)

    for count, letter in enumerate(yellow_letters):
        for word in possible_answers:
            if not word.__contains__(letter):
                to_be_removed.append(word)
            else:
                if word.index(letter) == yellow_indexes[count]:
                    to_be_removed.append(word)

    for word in to_be_removed:
        if possible_answers.__contains__(word):
            possible_answers.remove(word)

    '''filtering out for green letters'''

    green_letters = []
    green_indexes = []
    to_be_removed = []

    for count, letter in enumerate(starting_word_list):
        if result_list[count] == 'g':
            green_letters.append(letter)
            green_indexes.append(count)

    for word in possible_answers:
        for count, letter in enumerate(green_letters):
            if word[green_indexes[count]] != letter:
                to_be_removed.append(word)

    for word in to_be_removed:
        if possible_answers.__contains__(word):
            possible_answers.remove(word)

    return possible_answers
