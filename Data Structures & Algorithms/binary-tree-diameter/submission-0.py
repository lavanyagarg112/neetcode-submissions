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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # idea (after seeing the solution)
        # the height of the left tree, height of the right three
        # so longest path for a specific node is height of left + height of right
        
        # bruteforce
        stack = [root]
        diameter = 0

        while stack:
            node = stack.pop()
            curr_diameter = self.height(node.left) + self.height(node.right)
            diameter = max(diameter, curr_diameter)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return diameter