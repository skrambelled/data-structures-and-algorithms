import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Queue, InvalidOperationError
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Shelter


def test_import():
    assert Queue
    assert Shelter


def test_shelter_with_a_cat():
    q = Queue()
    q.enqueue('cat')
    assert q.front.value == 'cat'
    assert q.rear.value == 'cat'


def test_queue_add_error():
    q = Queue()
    with pytest.raises(TypeError) as e:
        q + 1
    assert str(e.value) == "Method only allowed with another Queue"


def test_add_filled_to_empty_queue():
    q1 = Queue()
    q2 = Queue()
    q2.enqueue('cat')
    q1 + q2
    assert q1.front.value == 'cat'
    assert q1.rear.value == 'cat'


def test_add_empty_to_filled_queue():
    q1 = Queue()
    q1.enqueue('cat')
    q2 = Queue()
    q1 + q2
    assert q1.front.value == 'cat'
    assert q1.rear.value == 'cat'


def test_add_two_queues():
    q1 = Queue()
    q1.enqueue('cat')
    q2 = Queue()
    q2.enqueue('dog')
    q1 + q2
    assert q1.front.value == 'cat'
    assert q1.rear.value == 'dog'


def test_cat_in_shelter():
    shelter = Shelter()
    shelter.enqueue('cat')
    assert shelter.peek() == 'cat'


def test_wrong_animal_in_shelter():
    shelter = Shelter()

    with pytest.raises(ValueError) as e:
        shelter.enqueue('snake')
    assert str(e.value) == "Shelter is for 'cat' or 'dog' only, not 'snake'"


def test_get_dog_by_itself():
    shelter = Shelter()

    shelter.enqueue('dog')
    dog = shelter.dequeue('dog')
    assert dog == 'dog'


def test_get_cat_behind_dog():
    shelter = Shelter()

    shelter.enqueue('dog')
    shelter.enqueue('cat')
    cat = shelter.dequeue('cat')
    assert cat == 'cat'


def test_get_cat_behind_dogs():
    shelter = Shelter()

    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    cat = shelter.dequeue('cat')
    assert cat == 'cat'


def test_get_cat_without_cat():
    shelter = Shelter()

    with pytest.raises(InvalidOperationError) as e:
        shelter.dequeue('cat')
    assert str(e.value) == "Method not allowed on empty collection"
