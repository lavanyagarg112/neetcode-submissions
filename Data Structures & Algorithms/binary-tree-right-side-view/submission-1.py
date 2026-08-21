# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        queue.append(root)
        res = [] 

        while queue:
            n = len(queue)
            last_in_level = None
            for _ in range(n):
                curr = queue.popleft()
                if curr != None:
                    last_in_level = curr.val
                else:
                    break
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(last_in_level)
        
        return res

        