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

    def contains(self, key):
        """
        Returns True if a key exists in a hashtable, otherwise return False
        """
        hashed_key_index = self._hash(key)

        bucket = self._buckets[hashed_key_index]

        # no bucket at all, so we cannot store the key in this bucket
        if not bucket:
            return False

        # collisions may occur in a bucket, so lets make sure
        # this key is in the bucket
        current = bucket.head
        while current and current.value[0] != key:
            current = current.next

        if not current:
            return False

        return True

    def get_hashes(self):
        """
        Returns a list of bucklets that have at least one key
        """
        buckets = []
        for bucket in self._buckets:
            if bucket:
                buckets.append(bucket)
        return buckets

    def join(self, other, right_join=False):
        """
        Return a matrix of 'self' joined with 'other' hashtatable, or LEFT JOIN

        right_join=True will perform a join of 'other' with 'self', or RIGHT JOIN
        """
        primary_hashtable = self if not right_join else other
        secondary_hashtable = other if not right_join else self

        buckets = primary_hashtable.get_hashes()
        output = []

        for bucket in buckets:
            current = bucket.head
            while current:
                key = current.value[0]
                value = current.value[1]

                this_set = [key, value]
                if secondary_hashtable.contains(key):
                    this_set.append(secondary_hashtable.get(key))
                else:
                    this_set.append(None)

                output.append(this_set)
                current = current.next

        return output
