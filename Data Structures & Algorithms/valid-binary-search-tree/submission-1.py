# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inOrderTrav(self, root: Optional[TreeNode]) -> bool:

        prev = [None]
        flag = [True]

        def  helper(root: Optional[TreeNode], prev, flag):

            if flag[0] == False:
                return False

            if root.left:
                helper(root.left, prev, flag)

            if prev[0] != None and prev[0] > root.val:
                flag[0] = False
                return
            prev[0] = root.val

            if root.right:
                helper(root.right, prev, flag)

        helper(root, prev, flag)
        return flag[0]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.inOrderTrav(root)
        