# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # iterative dfs

        if not root:
            return 0

        stack = []
        stack.append((root, 1))
        max_length = 0

        while stack:
            curr, result = stack.pop()
            if not curr.left and not curr.right:
                max_length = max(max_length, result)

            if curr.left:
                stack.append((curr.left, result + 1))

            if curr.right:
                stack.append((curr.right, result + 1))

        return max_length
            

        