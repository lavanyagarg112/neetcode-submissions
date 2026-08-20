# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # CHECK AGAIN

    def height(self, node):
        if not node:
            return -1

        if not node.left and not node.right:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        print(node.val, left_height, right_height)

        if type(left_height) == bool or type(right_height) == bool:
            return False

        if abs(right_height - left_height) > 1:
            return False
        
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = self.height(root)
        if type(res) == bool:
            return False

        return True
        