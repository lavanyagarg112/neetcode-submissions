class Node:

    def __init__(self, val=None, nex=None):
        self.val = val
        self.nex = nex


class MinStack:

    def __init__(self):
        self.linkedList = None
        self.length = 0
        

    def push(self, val: int) -> None:
        if self.length == 0:
            self.linkedList = Node(val)
        else:
            new_node = Node(val, self.linkedList)
            self.linkedList = new_node
        self.length += 1
        

    def pop(self) -> None:
        if self.length > 0:
            self.linkedList = self.linkedList.nex
            self.length -= 1
        

    def top(self) -> int:
        if self.length > 0:
            return self.linkedList.val
        else:
            return None
        

    def getMin(self) -> int:

        if self.length == 0:
            return None

        curr = self.linkedList
        res = float('inf')

        while curr:
            res = min(res, curr.val)
            curr = curr.nex

        return res

