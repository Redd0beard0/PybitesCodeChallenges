from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        words_list = f.read().split()
    return words_list
    pass


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        if letter.isalpha():
            word_value += LETTER_SCORES(letter.upper())
    return word_value
    pass


def max_word_value(words_list = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    best_word = ''
    highest_value = 0
    word_value = 0
    for word in words_list:
        word_value = calc_word_value(word)
        if highest_value < word_value:
            highest_value = word_value
            best_word = word
    return best_word
    pass


if __name__ == "__main__":
    pass  # run unittests to validate
