# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # are all vals unique?
        # nope

        if not root and not subRoot:
            return True

        if not subRoot:
            return True # i think?

        if not root:
            return False

        stack = [root]

        while stack:
            curr = stack.pop()

            if curr.val == subRoot.val:
                if self.isSame(curr, subRoot):
                    return True

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)
        
        return False
            
            

            

        

        

        

        


        