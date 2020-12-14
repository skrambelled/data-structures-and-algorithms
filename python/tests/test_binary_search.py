from code_challenges.binary_search.binary_search import binary_search


def test_import():
    assert binary_search


def test_binary_too_low():
    actual = binary_search([1, 2, 3], 0)
    expect = -1
    assert actual == expect


def test_binary_too_high():
    actual = binary_search([1, 2, 3], 4)
    expect = -1
    assert actual == expect


def test_binary():
    actual = binary_search([1, 2, 3], 2)
    expect = 1
    assert actual == expect


def test_binary_tiny_list():
    actual = binary_search([1], 1)
    expect = 0
    assert actual == expect


def test_binary_right():
    actual = binary_search([5, 6, 7, 9, 8, 10], 10)
    expect = 5
    assert actual == expect


def test_binary_left():
    actual = binary_search([5, 6, 7, 9, 8, 10], 5)
    expect = 0
    assert actual == expect


def test_binary_val_does_not_exist():
    actual = binary_search([5, 6, 9, 8, 10], 7)
    expect = -1
    assert actual == expect


def test_binary_negative_numbers():
    actual = binary_search([-9, -8, -7, -6, -5], -7)
    expect = 2
    assert actual == expect


def test_binary_spanning_0():
    actual = binary_search([-1, 0, 1], 0)
    expect = 1
    assert actual == expect
