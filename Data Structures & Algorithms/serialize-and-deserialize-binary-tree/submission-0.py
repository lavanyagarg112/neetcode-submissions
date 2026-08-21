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
        levels = 0

        while queue:
            n = len(queue)
            flag = 0
            temp = []
            for _ in range(n):
                curr = queue.popleft()
                if curr == self.NOTREE:
                    flag += 1
                    temp.append(self.NOTREE)
                    queue.append(self.NOTREE)
                    queue.append(self.NOTREE)
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
            levels += 1

        # res.append(str(levels))
        result = self.SEPARATOR.join(res)
        print(result)
        return result



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split(self.SEPARATOR)
        if len(lst) == 0:
            return None

        root = TreeNode(val = lst[0])
        queue = deque()
        queue.append(root)
        # levels = lst.pop()

        # for level in range(1, levels)
        i = 1
        ind = 1

        while ind < len(lst):

            for j in range(ind, ind + (2 ** i), 2):
                curr = queue.popleft()
                left = TreeNode(val = lst[j])
                right = TreeNode(val = lst[j+1])
                if lst[j] != self.NOTREE:
                    curr.left = left
                if lst[j+1] != self.NOTREE:
                    curr.right = right
                queue.append(left)
                queue.append(right)
                
            ind += (2 ** i)
            i += 1

        return root

