from code_challenges.tree.tree import BinaryTree, Node


#     1
#   2   3
# 4  5 6  7
def test_heaviest_balanced_tree():
    tree = BinaryTree()
    tree.add(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right = Node(3)
    tree.root.right.left = Node(6)
    heaviest_leaf = Node(7)
    tree.root.right.right = heaviest_leaf
    result = tree.highest_weight()
    assert result[0] == heaviest_leaf
    assert result[1] == 11
