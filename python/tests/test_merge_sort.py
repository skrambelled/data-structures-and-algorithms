from code_challenges.merge_sort.merge_sort import merge_sort


def test_import():
    assert merge_sort


def test_single_list():
    the_list = [5]
    merge_sort(the_list)
    actual = the_list
    expect = [5]
    assert actual == expect


def test_already_sorted_list():
    the_list = [1, 2, 3, 4, 5]
    merge_sort(the_list)
    actual = the_list
    expect = [1, 2, 3, 4, 5]
    assert actual == expect


def test_unsorted_list():
    the_list = [3, 6, 2, 4]
    merge_sort(the_list)
    actual = the_list
    expect = [2, 3, 4, 6]
    assert actual == expect


def test_unsorted_list_with_duplicates():
    the_list = [3, 6, 2, 4, 3]
    merge_sort(the_list)
    actual = the_list
    expect = [2, 3, 3, 4, 6]
    assert actual == expect


def test_unsorted_list_with_negatives():
    the_list = [3, -6, -2, 4, 3]
    merge_sort(the_list)
    actual = the_list
    expect = [-6, -2, 3, 3, 4]
    assert actual == expect


def test_unsorted_list_with_negatives_and_zero():
    the_list = [3, -6, -2, 4, 3, 0]
    merge_sort(the_list)
    actual = the_list
    expect = [-6, -2, 0, 3, 3, 4]
    assert actual == expect
