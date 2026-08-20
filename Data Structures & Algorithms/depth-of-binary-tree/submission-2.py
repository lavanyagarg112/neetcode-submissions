# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # iterative bfs
        # number of levels

        if not root:
            return 0

        queue = deque()
        queue.append((root, 1))
        levels = 0

        while queue:
            curr, num = queue.popleft()
            levels = max(levels, num)

            if curr.left:
                queue.append((curr.left, num + 1))

            if curr.right:
                queue.append((curr.right, num + 1))

        return levels






