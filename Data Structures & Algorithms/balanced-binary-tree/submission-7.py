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

        return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return abs(right - left) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        