from code_challenges.pascal_triangle.pascal_triangle import pascal


def test_import():
    assert pascal


def test_empty_pascal():
    actual = pascal(0)
    expect = []

    assert actual == expect


def test_pascal_1():
    actual = pascal(1)
    expect = [[1]]

    assert actual == expect


def test_pascal_2():
    actual = pascal(2)
    expect = [[1], [1,1]]

    assert actual == expect


def test_pascal_3():
    actual = pascal(3)
    expect = [[1], [1, 1], [1, 2, 1]]

    assert actual == expect


def test_pascal_4():
    actual = pascal(4)
    expect = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

    assert actual == expect
