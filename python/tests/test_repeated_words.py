from code_challenges.repeated_words.repeated_words import find_first_repeated_word, count_words
import pytest


def test_find_first_repeated_word_with_repeat():
    string = "Once upon a time in a castle"

    expect = 'a'
    actual = find_first_repeated_word(string)
    assert actual == expect


def test_find_first_repeated_word_without_repeat():
    string = "Once upon a time outside the castle"

    with pytest.raises(Exception) as e:
        find_first_repeated_word(string)

    expect = 'No repeated words in string'
    actual = str(e.value)
    assert actual == expect


def test_empty_string():
    string = ''

    with pytest.raises(Exception) as e:
        find_first_repeated_word(string)

    expect = 'No repeated words in string'
    actual = str(e.value)
    assert actual == expect


def test_count_words_with_repeats():
    string = "Once upon a time in a castle"

    expect = 2
    actual = count_words(string)['a']
    assert actual == expect


def test_repeated_words_with_capitalization():
    string = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'

    expect = 'it'
    actual = find_first_repeated_word(string)
    assert actual == expect


def test_repeated_words_with_puncuation():
    string = "it's head was beneath it's tail."

    expect = "it's"
    actual = find_first_repeated_word(string)
    assert actual == expect
