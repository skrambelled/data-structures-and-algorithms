from code_challenges.hashtable.hashtable import Hashtable
import pytest


# tests from JB

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('JkhakjfhkjghjkwshgkjashgjkwhAGKJHGJKHWGEJKhahgfkjaghkjahgkjaghkjaghkjaghkjaghkjahgkjah')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_silent_and_listen():
    hashtable = Hashtable()
    hashtable.set('listen', 'to me')
    hashtable.set('silent', 'so quiet')

    assert hashtable.get('listen') == 'to me'
    assert hashtable.get('silent') == 'so quiet'


#########################
# testing join() method #
#########################


def test_contains():
    hashtable = Hashtable()
    hashtable.set('one', '1')

    actual = hashtable.contains('one')
    expect = True

    assert actual == expect


def test_not_contains():
    hashtable = Hashtable()
    hashtable.set('one', '1')

    actual = hashtable.contains('two')
    expect = False

    assert actual == expect


def test_get_hashes_length():
    hashtable = Hashtable()
    hashtable.set('one', '1')
    hashtable.set('two', '2')

    actual = len(hashtable.get_hashes())
    expect = 2

    assert actual == expect


def test_join_left_with_empty_right():
    left = Hashtable()
    right = Hashtable()

    left.set('fond', 'enamored')

    actual = left.join(right)
    expect = [['fond', 'enamored', None]]

    assert actual == expect


def test_right_join_with_empty_right():
    left = Hashtable()
    right = Hashtable()

    left.set('fond', 'enamored')

    actual = left.join(right, right_join=True)
    expect = []

    assert actual == expect


def test_left_join_with_antonym_right():
    left = Hashtable()
    right = Hashtable()

    left.set('fond', 'enamored')
    right.set('fond', 'averse')

    actual = left.join(right)
    expect = [['fond', 'enamored', 'averse']]

    assert actual == expect


def test_left_join_collisions_with_antonym_right():
    left = Hashtable()
    right = Hashtable()

    left.set('fond', 'enamored')
    right.set('fond', 'averse')
    right.set('donf', 'enamored')

    actual = left.join(right)
    expect = [['fond', 'enamored', 'averse']]

    assert actual == expect


def test_right_join_collisions():
    left = Hashtable()
    right = Hashtable()

    left.set('fond', 'enamored')
    left.set('donf', 'enamored')
    right.set('fond', 'averse')

    actual = left.join(right, right_join=True)
    expect = [['fond', 'averse', 'enamored']]

    assert actual == expect
