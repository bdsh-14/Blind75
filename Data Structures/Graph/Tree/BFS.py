# Level order traversal
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None        

def bfs(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        result.append(current_level)
    return result


def main():
    root = TreeNode(3)
    root.left = TreeNode(8)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(str(bfs(root)))

main()