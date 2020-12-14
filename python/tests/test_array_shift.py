from code_challenges.array_shift.array_shift import insertShiftArray


def test_import():
    assert insertShiftArray


def test_shift_odd():
    actual = insertShiftArray([1, 2, 3], 5)
    expect = [1, 5, 2, 3]
    assert actual == expect


def test_shift_even():
    actual = insertShiftArray(["value one", "value two"], "insert")
    expect = ["value one", "insert", "value two"]
    assert actual == expect
