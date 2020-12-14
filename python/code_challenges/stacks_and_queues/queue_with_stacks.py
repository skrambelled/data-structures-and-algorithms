from code_challenges.stacks_and_queues.stacks_and_queues import Stack, Node


class PsuedoQueue:
    """
    This is a queue being implement using stack's
    push, pop and peek methods rather than having
    its own attributes and methods
    """

    def __init__(self):
        self.front_stack = Stack()
        self.rear_stack = Stack()
        # this is strictly here so that we may pass a test,
        self.front = None

    def peek(self):
        return self.front_stack.peek()

    def is_empty(self):
        return self.front_stack.is_empty()

    def enqueue(self, value=None):
        node = Node(value)
        if self.rear_stack.top:
            self.rear_stack.top.next = node
        self.rear_stack.top = node
        if not self.front_stack.top:
            self.front_stack.top = node
            # next line is solely here to pass a test
            self.front = self.front_stack.top

    def dequeue(self):
        # if the queue only holds one node, we must manually set the rear to None
        if(self.rear_stack.top == self.front_stack.top):
            self.rear_stack.top = None
        value = self.front_stack.pop()
        # next line is solely here to pass a test
        self.front = self.front_stack.top
        return value
