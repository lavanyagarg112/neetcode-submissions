# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getRootPathSum(self, node):
        # explore whole tree starting from node and 
        # get back max path sum
        if not node:
            return 0

        queue = deque()
        queue.append((node, node.val))
        maxSoFar = float('-inf')

        while queue:
            curr, res = queue.popleft()
            maxSoFar = max(res, maxSoFar)
            if not curr.left and not curr.right:
                continue
            if curr.left:
                queue.append((curr.left, res + curr.left.val))
            if curr.right:
                queue.append((curr.right, res + curr.right.val))
        
        return maxSoFar


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        curr_path_sum = self.getRootPathSum(root.left) + root.val + self.getRootPathSum(root.right)
        left_path_sum = self.maxPathSum(root.left)
        right_path_sum = self.maxPathSum(root.right)

        return max(curr_path_sum, max(left_path_sum, right_path_sum))
        