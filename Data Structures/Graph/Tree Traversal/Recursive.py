# Recursive tree traversal
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/?ref=gcse


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# inorder: Left, root, right
# preorder: root, left, right
# postorder: left, right, root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.value, end= " ")
        preOrder(root.left)
        inOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end= " ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder---")
preOrder(root)

print("InOrder---")
inOrder(root)

print("Postorder---")
postOrder(root)