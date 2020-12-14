import random
from code_challenges.stacks_and_queues.stacks_and_queues import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None


class BinaryTree(Tree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def walk(root):
            if not root.left:
                root.left = Node(value)
                return
            if not root.right:
                root.right = Node(value)
                return

            # randomly select a left or right node to walk through
            if random.randint(0, 1):
                walk(root.left)
            else:
                walk(root.right)

        walk(self.root)

    def find_maximum_value(self):
        def walk(root):
            max = root.value
            if root.left:
                left = walk(root.left)
                if left > max:
                    max = left
            if root.right:
                right = walk(root.right)
                if right > max:
                    max = right
            return max

        return walk(self.root)

    def breadth_traverse(self):
        if not self.root:
            raise Exception('tree is empty')

        output = []
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            output.append(current.value)
        return output


class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def walk(root):
            if value < root.value:
                if not root.left:
                    root.left = Node(value)
                else:
                    walk(root.left)
            else:
                if not root.right:
                    root.right = Node(value)
                else:
                    walk(root.right)

        walk(self.root)

    def contains(self, value):
        def walk(root):
            if root.value == value:
                return True
            if value < root.value:
                if not root.left:
                    return False
                return walk(root.left)
            else:
                if not root.right:
                    return False
                return walk(root.right)

        return walk(self.root)

    def _get_values(self, root, flag="in-order"):
        values = []

        def walk(root, flag):
            if not root:
                return

            if(flag == 'pre-order'):
                values.append(root.value)
            walk(root.left, flag)
            if(flag == 'in-order'):
                values .append(root.value)
            walk(root.right, flag)
            if(flag == 'post-order'):
                values.append(root.value)
            return values

        walk(self.root, flag)
        return values

    def pre_order(self):
        return self._get_values(self.root, 'pre-order')

    def in_order(self):
        return self._get_values(self.root, 'in-order')

    def post_order(self):
        return self._get_values(self.root, 'post-order')
