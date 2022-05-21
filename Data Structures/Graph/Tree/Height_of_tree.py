class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None   

def height_of_tree(root: TreeNode) -> int:
    result = 0
    if root is None:
        return result
    
    leftHeight = height_of_tree(root.left)
    if root.left is not None:
        print("Left = ", "height of tree(",root.left.value,")", leftHeight)

    rightHeight = height_of_tree(root.right)
    if root.right is not None:
        print("Right = ", "height of tree(",root.right.value,")", rightHeight)

    result = 1 + max(leftHeight, rightHeight)
    return result

def main():
    root = TreeNode(3)
    root.left = TreeNode(8)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(height_of_tree(root))
main()