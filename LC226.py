# https://leetcode.com/problems/invert-binary-tree/

# Process: for every node, look at it's children and swap them, recursively run on left subtree and right subtree
# DFS - both pre and post order

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right        

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root