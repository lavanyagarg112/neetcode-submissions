# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxsofar):

            if node.val >= maxsofar:
                self.res += 1
            
            new_max = max(maxsofar, node.val)
            if node.left:
                dfs(node.left, new_max)
            if node.right:
                dfs(node.right, new_max)

        dfs(root, float('-inf'))

        return self.res
        