"""Stack, Queue, and the other classes to support them"""


class Node:
    """
    A node implementation, to be used by both stacks and also queues

    value - holds any value
    next  - points to next node
    """

    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return f'{self.value}'

    def __eq__(self, other):
        return self.value == other.value and self.next == other.next


class InvalidOperationError(Exception):
    pass


class Stack:
    """
    Stack implementation
    """

    def __init__(self):
        self.top = None

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return not self.top

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = node.next
        return node.value


class Queue:
    """
    Queue implementation
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        output = "FRONT -> "
        current = self.front
        while current:
            output += '{ ' + str(current) + ' } -> '
            current = current.next
        output += 'REAR'
        return output

    def __add__(self, other):
        if not isinstance(other, Queue):
            raise TypeError("Method only allowed with another Queue")
        if self.rear:
            self.rear.next = other.front
            if other.rear:
                self.rear = other.rear
        else:
            self.front = other.front
            self.rear = other.rear

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return not self.front and not self.rear

    def enqueue(self, value=None):
        if self.is_empty():
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")

        node = self.front
        # dont forget to clear the rear if queue only has one node!
        if self.front == self.rear:
            self.rear = None

        self.front = self.front.next
        return node.value
