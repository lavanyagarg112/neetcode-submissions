# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getLists(self, inorder: List[int], val: int) -> List[int]:
        result1 = []
        result2 = []
        isSecond = False
        for v in inorder:
            if v == val:
                isSecond = True
                continue

            if not isSecond:
                result1.append(v)
            else:
                result2.append(v)

        return result1, result2

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        curr = preorder[0]
        inorder_left, inorder_right = self.getLists(inorder, curr)
        
        left_tree = self.buildTree(preorder[1: len(inorder_left) + 1], inorder_left)
        right_tree = self.buildTree(preorder[len(inorder_left) + 1: ], inorder_right)

        return TreeNode(curr, left_tree, right_tree)
        