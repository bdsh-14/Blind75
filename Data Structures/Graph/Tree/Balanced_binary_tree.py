# https://leetcode.com/problems/balanced-binary-tree/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def height_of_tree(root: TreeNode):
            if not root:
                return 0

            left_height = height_of_tree(root.left)
            right_height = height_of_tree(root. right)

            if abs(left_height - right_height) > 1:
                return -1
            return 1+max(left_height, right_height)

        return height_of_tree(root) != -1
        


def main():
    # root = TreeNode(3)
    # root.left = TreeNode(8)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)

    # solution = Solution()
    # print(solution.isBalanced(root))


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    solution = Solution()
    print(solution.isBalanced(root))

main()

        