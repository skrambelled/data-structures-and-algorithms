from code_challenges.array_reverse.array_reverse import reverseArray


def test_import():
    assert reverseArray


def test_reverse():
    actual = reverseArray([1, 2, 3, 4, 5])
    expect = [5, 4, 3, 2, 1]
    assert actual == expect
