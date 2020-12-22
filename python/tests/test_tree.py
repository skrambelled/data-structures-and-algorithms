from code_challenges.tree.tree import BinaryTree, BinarySearchTree, Node
import pytest


def test_import():
    assert BinaryTree
    assert BinarySearchTree


def test_empty_tree():
    tree = BinarySearchTree()
    assert isinstance(tree, BinarySearchTree)
    assert tree.root is None


def test_tree_with_root():
    tree = BinarySearchTree('test')
    assert tree.root.value == 'test'


def test_add_two_nodes():
    tree = BinarySearchTree(5)
    tree.add(3)
    tree.add(19)
    assert tree.root.left.value == 3
    assert tree.root.right.value == 19


def test_preorder():
    tree = BinarySearchTree(5)
    tree.add(3)
    tree.add(19)
    assert tree.pre_order() == [5, 3, 19]


def test_inorder():
    tree = BinarySearchTree(5)
    tree.add(3)
    tree.add(19)
    assert tree.in_order() == [3, 5, 19]


def test_postorder():
    tree = BinarySearchTree(5)
    tree.add(3)
    tree.add(19)
    assert tree.post_order() == [3, 19, 5]


#####################
# Binary Tree Tests #
#####################

def test_empty_binary_tree():
    tree = BinaryTree()
    assert isinstance(tree, BinaryTree)
    assert tree.root is None


def test_binary_tree_root():
    tree = BinaryTree(5)
    assert tree.root.value == 5


def test_binary_tree_add_once():
    tree = BinaryTree(4)
    tree.add(3)
    assert tree.root.left.value == 3


def test_binary_tree_add_twice():
    tree = BinaryTree(4)
    tree.add(2)
    tree.add(3)
    assert tree.root.right.value == 3


def test_max():
    tree = BinaryTree()
    tree.add(3)
    tree.add(4)
    tree.add(11)
    tree.add(5)
    tree.add(9)
    assert tree.find_maximum_value() == 11


def test_all_negatives():
    tree = BinaryTree()
    tree.add(-3)
    tree.add(-4)
    tree.add(-11)
    tree.add(-5)
    tree.add(-9)
    assert tree.find_maximum_value() == -3

####################
# breadth_traverse #
####################


def test_breadth_on_empty_tree():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.breadth_traverse()
    assert str(e.value) == "tree is empty"


#   1
#  2 3
def test_breadth_on_small_tree():
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    assert tree.breadth_traverse() == [1, 2, 3]


#         1
#        2
#       3
#      4
#     5
def test_breadth_on_big_left_branch():
    tree = BinaryTree()
    tree.add(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.left.left = Node(4)
    tree.root.left.left.left.left = Node(5)
    assert tree.breadth_traverse() == [1, 2, 3, 4, 5]


#     1
#   2   3
# 4  5 6  7
def test_breadth_balanced_tree():
    tree = BinaryTree()
    tree.add(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right = Node(3)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.breadth_traverse() == [1, 2, 3, 4, 5, 6, 7]


#     1     (all negatives though)
#   2   3
# 4  5 6  7
def test_breadth_balanced_negative_tree():
    tree = BinaryTree()
    tree.add(-1)
    tree.root.left = Node(-2)
    tree.root.left.left = Node(-4)
    tree.root.left.right = Node(-5)
    tree.root.right = Node(-3)
    tree.root.right.left = Node(-6)
    tree.root.right.right = Node(-7)
    assert tree.breadth_traverse() == [-1, -2, -3, -4, -5, -6, -7]


######################
# Tree intersections #
######################

def test_no_intersections():
    tree1 = BinarySearchTree()

    tree1.add(1)
    tree1.add(2)
    tree1.add(3)

    tree2 = BinarySearchTree()

    tree2.add(4)
    tree2.add(5)
    tree2.add(6)

    actual = tree1.tree_intersections(tree2)
    expect = []

    assert actual == expect


def test_one_interstions():
    tree1 = BinarySearchTree()

    tree1.add(2)
    tree1.root.left = Node(1)
    tree1.root.right = Node(3)

    tree2 = BinarySearchTree()

    tree2.add(2)
    tree2.root.left = Node(0)
    tree2.root.right = Node(4)

    actual = tree1.tree_intersections(tree2)
    expect = [2]

    assert actual == expect


def test_multiple_intersections():
    tree1 = BinarySearchTree()

    tree1.add(2)
    tree1.root.left = Node(1)
    tree1.root.right = Node(3)

    tree2 = BinarySearchTree()

    tree2.add(2)
    tree2.root.left = Node(1)
    tree2.root.right = Node(3)

    actual = tree1.tree_intersections(tree2)
    expect = [1, 2, 3]

    assert actual == expect
