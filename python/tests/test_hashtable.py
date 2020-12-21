from code_challenges.hashtable.hashtable import Hashtable


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
