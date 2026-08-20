# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursion

        if not root:
            return root

        if not root.left and not root.right:
            return root

        # swap 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        # alternate
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)


        return root
        