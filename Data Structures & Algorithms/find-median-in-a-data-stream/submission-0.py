class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
        self.count = 1
        self.leftHeight = 0
        self.rightHeight = 0

    def leftRotate(self, node):
        old_root = node
        old_root_replace = node.right.left
        new_root = node.right

        old_root.right = old_root_replace
        new_root.left = old_root

        return new_root

    def rightRotate(self, node):
        old_root = node
        old_root_replace = node.left.right
        new_root = node.left

        old_root.left = old_root_replace
        new_root.right = old_root

        return new_root



    def insertNode(self, parent, node):
        if not parent:
            return node
        
        if node.val < parent.val:
            if not parent.left:
                parent.left = node
            else:
                parent.left = self.insertNode(parent.left, node)
        else:
            if not parent.right:
                parent.right = node
            else:
                parent.right = self.insertNode(parent.right, node)

        parentLeft = self.heightTree(parent.left)
        parentRight = self.heightTree(parent.right) 

        if parentLeft > parentRight and node.val < parent.val:
            return self.rightRotate(parent)
        
        if parentLeft > parentRight and node.val > parent.val:
            parent.left = self.leftRotate(parent.left)
            return self.rightRotate(parent)

        if parentLeft < parentRight and node.val > parent.val:
            return self.leftRotate(parent)

        if parentLeft < parentRight and node.val < parent.val:
            parent.right = self.rightRotate(parent.right)
            return self.leftRotate(parent)

        return parent

        

    def heightTree(self, node):

        if not node:
            return 0

        queue = deque()
        queue.append(node)

        height = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            height += 1

        return height

    def addNode(self, node):

        self.count += 1
        self.root = self.insertNode(self.root, node)
        self.leftHeight = self.heightTree(self.root.left)
        self.rightHeight = self.heightTree(self.root.right)
        


    def getMedian(self):
        if self.count % 2 != 0:
            return self.root.val
        else:
            if self.leftHeight > self.rightHeight:
                res = (self.root.val  + self.root.left.val)/2.0
                return res
            else:
                res = (self.root.val  + self.root.right.val)/2.0
                return res

class MedianFinder:

    def __init__(self):
        self.tree = None
        

    def addNum(self, num: int) -> None:
        if not self.tree:
            self.tree = Tree(TreeNode(num))
        else:
            self.tree.addNode(TreeNode(num))
        

    def findMedian(self) -> float:
        return self.tree.getMedian()
        
        