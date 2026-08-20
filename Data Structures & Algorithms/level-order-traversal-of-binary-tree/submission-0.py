# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        levels = []
        queue = deque()

        queue.append(root)

        while queue:

            curr_level = []
            n = len(queue) # current level length

            for _ in range(n):
                curr = queue.popleft()
                curr_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            levels.append(curr_level)

        return levels
        