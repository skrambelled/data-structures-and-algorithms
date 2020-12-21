import re


def find_first_repeated_word(long_string):
    long_string = long_string.lower()

    counter = set()

    # strip out any punctuation, except apostrophes in compound words
    words = re.findall(r'(\w+(\'\w?)?)', long_string)

    words = [word[0] for word in words]

    for word in words:
        if word in counter:
            return word
        else:
            counter.add(word)

    raise Exception('No repeated words in string')


def count_words(long_string):
    long_string = long_string.lower()

    counter = {}

    words = re.findall(r'(\w+)', long_string)
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

    return counter
