# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, node):
        if not node:
            return 0

        if not node.left and not node.right:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left:
            return self.height(root.right) < 1
        if not root.right:
            return self.height(root.left) < 1

        return abs(self.height(root.left) - self.height(root.right)) <= 1
        