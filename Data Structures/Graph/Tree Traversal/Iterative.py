# https://www.geeksforgeeks.org/iterative-preorder-traversal/?ref=gcse
from typing import List

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def iterativePreorder(root: Node) -> List[int]:
    if root is None:
        return []

    result = []
    stack = []

    stack.append(root)

    while(stack):
        node = stack.pop()
        result.append(node.value)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    
    return result
            

def iterativeInorder(root: Node) -> List[int]:
    result = []
    stack = []
    temp = root

    if root is None:
        return []

    while True:
        if temp is not None:
            stack.append(temp)
            temp = temp.left
        elif(stack):
            node = stack.pop()
            result.append(node.value)
            temp = node.right
        else:
            break
    return result

# https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/

def iterativePostorder(root: Node) -> List[int]:
    result = []
    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                result.append(node.value)
            else:
                # postorder
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return result
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder")
print(iterativePreorder(root))

print("Inorder")
print(iterativeInorder(root))

print("Postorder")
print(iterativePostorder(root))