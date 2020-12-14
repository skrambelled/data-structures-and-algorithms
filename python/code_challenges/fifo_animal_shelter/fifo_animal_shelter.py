from code_challenges.stacks_and_queues.stacks_and_queues import Queue


class Shelter(Queue):
    def enqueue(self, value):
        if value != 'cat' and value != 'dog':
            raise ValueError(f"Shelter is for 'cat' or 'dog' only, not '{value}'")
        super().enqueue(value)

    def dequeue(self, preference=None):
        if not preference:
            return super().dequeue()

        current = super().dequeue()
        q = Queue()
        while(current != preference):
            print(self)
            q.enqueue(current)
            current = super().dequeue()
        if(self.front):
            self.front.next = q.rear
        self.front = q.front
        return current
