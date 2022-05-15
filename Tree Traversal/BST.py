class TreeNode: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root

        while(True):
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                temp = temp.right
    
    def contains(self, num):
        if self.root is None:
            return False
        temp = self.root

        while not None:
            if temp.value == num:
                return True
            if num > temp.value:
                temp = temp.right
            else:
                temp = temp.left
            return False
    
    def min_value_node(self, current_node: TreeNode):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


myBst = BST()
myBst.insert(40)
myBst.insert(28)
myBst.insert(60)

print("---Complete tree---")
print(myBst.root.value)
print(myBst.root.left.value)
print(myBst.root.right.value)

print(myBst.contains(40))

print("Minimum value: ", myBst.min_value_node(myBst.root))