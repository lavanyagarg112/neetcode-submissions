# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def contains(self, root: TreeNode, p: TreeNode) -> bool:

        if not root:
            return False

        if root.val == p.val:
            return True

        return self.contains(root.left, p) or self.contains(root.right, p)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # if self.contains(p, q):
        #     return p
        
        # if self.contains(q, p):
        #     return q

        if root.left and self.contains(root.left, p) and self.contains(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if root.right and self.contains(root.right, p) and self.contains(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        return root







        