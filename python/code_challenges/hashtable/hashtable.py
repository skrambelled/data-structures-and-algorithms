from code_challenges.linked_list.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    # hashing for strings
    def _hash(self, key):
        if not isinstance(key, str):
            raise Exception(f'{key} must be a string in order to be hashed')

        sum = 0

        for char in key:
            sum += ord(char)

        primed = sum * 23

        index = primed % self._size

        return index

    def set(self, key, value):
        # this hashtable only supports strings as keys
        hashed_key_index = self._hash(key)

        # if we dont have a LinkedList yet at this bucket, instantiate one
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        # insert both the key and the value as a tuple in the linked list
        self._buckets[hashed_key_index].insert((key, value))

    def get(self, key):
        hashed_key_index = self._hash(key)

        bucket = self._buckets[hashed_key_index]

        # can improve this exception
        if not bucket:
            raise Exception(f'No values for: {key} in hashtable')

        current = bucket.head

        while current and current.value[0] != key:
            current = current.next

        if not current:
            raise Exception(f'No value for: {key} in hashtable')

        return current.value[1]
