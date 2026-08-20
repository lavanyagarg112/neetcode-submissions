# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTrav(self, root: Optional[TreeNode]) -> bool:

        trav = []

        def  helper(root: Optional[TreeNode]):

            if root.left:
                helper(root.left)

            trav.append(root.val)

            if root.right:
                helper(root.right)

        helper(root)
        return trav

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inOrderTrav(root)[k-1]