from code_challenges.linked_list.linked_list import LinkedList, Node, DoubleLinkedList, DoubleNode
import pytest


def test_import():
    assert LinkedList
    assert Node
    assert DoubleLinkedList
    assert DoubleNode


def test_empty_list():
    linked_list = LinkedList()
    assert linked_list
    assert isinstance(linked_list, LinkedList)
    assert linked_list.head is None


def test_first_node():
    node = Node()
    actual = node.next
    expect = None
    assert actual == expect


def test_node(node):
    assert node.value == "some value"


def test_fixture_node_in_linked_list(one_list):
    assert isinstance(one_list.head, Node)
    assert one_list.head.value == "one"


def test_insert_node():
    ll = LinkedList()
    ll.insert('first')
    assert ll.head.value == "first"
    ll.insert("second")
    assert ll.head.value == "second"


def test_includes():
    ll = LinkedList()
    ll.insert('first')
    assert ll.includes("second") is False
    assert ll.includes("first") is True
    ll.insert("another")
    assert ll.includes("another") is True


def test_to_string(empty_list):
    ll = LinkedList()
    assert str(ll) == "NULL"
    ll.insert('3')
    ll.insert(2)
    ll.insert('1')
    assert str(ll) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def one_list():
    ll = LinkedList()
    ll.insert('one')
    return ll


@pytest.fixture
def two_list():
    some_list = LinkedList(["one"])
    some_list.insert("two")
    return some_list


@pytest.fixture
def node():
    return Node("some value")


#######################
# Double linked lists #
#######################


def test_dlist():
    dlist = DoubleLinkedList()
    assert isinstance(dlist, DoubleLinkedList)


def test_insert_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    assert dlist.head.value == '1'


def test_append_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    dlist.append('2')
    assert dlist.tail.value == '2'


def test_str_dlist():
    dlist = DoubleLinkedList()
    dlist.insert('1')
    dlist.append('2')
    dlist.insert('3')
    dlist.append('4')
    print(str(dlist))
    assert str(dlist) == 'NULL <-> { 3 } <-> { 1 } <-> { 2 } <-> { 4 } <-> NULL'


#########################
# Extending linked list #
#########################

# test append()
def test_append_empty():
    ll = LinkedList()
    ll.append('test')
    assert str(ll.head) == "test"


def test_append_several():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.includes(3)
    assert str(ll) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


########################################################################
# test insert_before
def test_insert_before_empty():
    ll = LinkedList()
    with pytest.raises(Exception) as context:
        ll.insert_before(3, 5)
    assert str(context.value) == "Cannot `insert_before` on empty LinkedList"


def test_insert_before_reference_does_not_exist():
    ll = LinkedList()
    with pytest.raises(Exception) as context:
        ll.insert(1)
        ll.insert_before(3, 5)
    assert str(context.value) == 'No node containing: 5'


def test_insert_before_exists():
    ll = LinkedList()
    ll.insert(3)
    ll.insert(1)
    ll.insert_before(2, 3)
    assert str(ll) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


# test insert_after
def test_insert_after_empty():
    ll = LinkedList()
    with pytest.raises(Exception) as context:
        ll.insert_after(1, 1)
    assert str(context.value) == "Cannot `insert_after` on empty LinkedList"


def test_insert_after_does_not_exist():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    with pytest.raises(Exception) as context:
        ll.insert_after(3, 3)
    assert str(context.value) == "No node containing: 3"


def test_insert_after_exists():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(1)
    ll.insert_after(3, 2)
    assert str(ll) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


#####################################################################


# Where k is greater than the length of the linked list
def test_k_is_greater_than_list_length():
    ll = LinkedList()
    val = 1
    with pytest.raises(Exception) as context:
        ll.kth_from_end(val)
    assert str(context.value) == f'Invalid index: {val} is out of range on linked list'


# Where k and the length of the list are the same
def test_k_is_equal_to_list_length():
    ll = LinkedList([1, 2, 3])
    val = 3
    with pytest.raises(Exception) as context:
        ll.kth_from_end(val)
    assert str(context.value) == f'Invalid index: {val} is out of range on linked list'


# Where k is not a positive integer
def test_k_is_negative():
    ll = LinkedList()
    val = -1
    with pytest.raises(Exception) as context:
        ll.kth_from_end(val)
    assert str(context.value) == f'Invalid index: {val} is out of range on linked list'


# Where the linked list is of a size 1
def test_ll_is_size_one():
    ll = LinkedList([100])
    assert ll.kth_from_end(0) == 100


# “Happy Path” where k is not at the end, but somewhere in the middle of the li
def test_kth_is_in_ll_somewhere():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.kth_from_end(0) == 4
    assert ll.kth_from_end(1) == 3
    assert ll.kth_from_end(3) == 1


##############################
# Linked list zipper testing #
##############################

def test_zip_lists_of_same_size():
    ll_primary = LinkedList([1, 2, 3])
    ll_secondary = LinkedList(['a', 'b', 'c'])
    ll_primary.zip(ll_secondary)
    print(str(ll_primary))
    assert str(ll_primary) == '{ 1 } -> { a } -> { 2 } -> { b } -> { 3 } -> { c } -> NULL'


def test_zip_one_empty_list():
    ll_primary = LinkedList([1, 2, 3])
    ll_secondary = LinkedList()
    ll_primary.zip(ll_secondary)
    print(str(ll_primary))
    assert str(ll_primary) == '{ 1 } -> { 2 } -> { 3 } -> NULL'


def test_zip_primary_list_longer():
    ll_primary = LinkedList([1, 2, 3])
    ll_secondary = LinkedList(['a'])
    ll_primary.zip(ll_secondary)
    print(str(ll_primary))
    assert str(ll_primary) == '{ 1 } -> { a } -> { 2 } -> { 3 } -> NULL'


def test_zip_secondary_list_longer():
    ll_primary = LinkedList([1])
    ll_secondary = LinkedList(['a', 'b', 'c'])
    ll_primary.zip(ll_secondary)
    print(str(ll_primary))
    assert str(ll_primary) == '{ 1 } -> { a } -> { b } -> { c } -> NULL'


def test_zip_long_list():
    max = 100
    ll_primary = LinkedList([even for even in range(0, max, 2)])
    ll_secondary = LinkedList([odd for odd in range(1, max, 2)])
    ll_primary.zip(ll_secondary)
    ll_check = LinkedList([x for x in range(0, max)])
    print(str(ll_primary))
    assert str(ll_primary) == str(ll_check)
