# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # bfs

        queue = deque()
        queue.append((root, float('-inf')))
        res = 0

        while queue:
            node, maxsofar = queue.popleft()
            if node.val >= maxsofar:
                res += 1
            maxsofar = max(maxsofar, node.val)
            if node.left:
                queue.append((node.left, maxsofar))
            if node.right:
                queue.append((node.right, maxsofar))
        return res

        