from code_challenges.quick_sort.quick_sort import quick_sort
import pytest


def test_import():
    assert quick_sort

@pytest.mark.skip
def test_single_list():
    the_list = [5]
    quick_sort(the_list)
    actual = the_list
    expect = [5]
    assert actual == expect

@pytest.mark.skip
def test_already_sorted_list():
    the_list = [1, 2, 3, 4, 5]
    quick_sort(the_list)
    actual = the_list
    expect = [1, 2, 3, 4, 5]
    assert actual == expect

@pytest.mark.skip
def test_unsorted_list():
    the_list = [3, 6, 2, 4]
    quick_sort(the_list)
    actual = the_list
    expect = [2, 3, 4, 6]
    assert actual == expect

@pytest.mark.skip
def test_unsorted_list_with_duplicates():
    the_list = [3, 6, 2, 4, 3]
    quick_sort(the_list)
    actual = the_list
    expect = [2, 3, 3, 4, 6]
    assert actual == expect

@pytest.mark.skip
def test_unsorted_list_with_negatives():
    the_list = [3, -6, -2, 4, 3]
    quick_sort(the_list)
    actual = the_list
    expect = [-6, -2, 3, 3, 4]
    assert actual == expect

@pytest.mark.skip
def test_unsorted_list_with_negatives_and_zero():
    the_list = [3, -6, -2, 4, 3, 0]
    quick_sort(the_list)
    actual = the_list
    expect = [-6, -2, 0, 3, 3, 4]
    assert actual == expect
