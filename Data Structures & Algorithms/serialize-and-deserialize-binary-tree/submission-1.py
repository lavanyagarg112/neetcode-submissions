# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def __init__(self):
        self.SEPARATOR = "%"
        self.NOTREE = "None"
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            flag = 0
            temp = []
            for _ in range(n):
                curr = queue.popleft()
                if curr == self.NOTREE:
                    flag += 1
                    temp.append(self.NOTREE)
                    # queue.append(self.NOTREE)
                    # queue.append(self.NOTREE)
                    continue

                temp.append(str(curr.val))
                if curr.left:
                    queue.append(curr.left)
                else:
                    queue.append(self.NOTREE)
                if curr.right:
                    queue.append(curr.right)
                else:
                    queue.append(self.NOTREE)
            if flag == n:
                break
            res.extend(temp)

        result = self.SEPARATOR.join(res)
        return result


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:



        lst = data.split(self.SEPARATOR)
        if len(lst) == 0 or lst[0] == "":
            return None

        root = TreeNode(val = int(lst[0]))
        queue = deque()
        queue.append(root)

        i = 1
        ind = 1

        while ind < len(lst):
            n = len(queue)
            for j in range(ind, ind + (n*2), 2):
                curr = queue.popleft()
                if lst[j] != self.NOTREE:
                    left = TreeNode(val = int(lst[j]))
                    curr.left = left
                    queue.append(left)
                # else:
                # can remove because if this is none, the below ones
                # are also none
                #     left = TreeNode(val = lst[j])
                #     queue.append(left)
                if lst[j+1] != self.NOTREE:
                    right = TreeNode(val = int(lst[j+1]))
                    curr.right = right
                    queue.append(right)
                # else:
                #     right = TreeNode(val = lst[j+1])
                #     queue.append(right)
                
            ind += (n*2)
            i += 1

        return root

