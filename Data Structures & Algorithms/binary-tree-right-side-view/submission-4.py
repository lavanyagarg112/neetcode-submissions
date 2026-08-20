# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # dfs logic
        # the first item we visit at THAT level/depth
        # assuming we are traversing right
        if not root:
            return []
        res = []
        stack = [(root,0)]

        while stack:
            node, depth = stack.pop()
            if depth == len(res):
                res.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right: # the first right that makes it -> right will be popped first
                stack.append((node.right, depth + 1))

        return res
        