"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # too expensive

        nodes = []
        new_nodes = []
        pos_to_random = {}

        temp = head
        while temp:
            nodes.append(temp)
            new_nodes.append(Node(temp.val))
            temp = temp.next
        nodes.append(None)
        new_nodes.append(None)

        for c in range(len(nodes)-1):
            curr = nodes[c]
            next_node = c + 1
            random_node = nodes.index(curr.random)
            newcurr = new_nodes[c]
            newcurr.next = new_nodes[next_node]
            newcurr.random = new_nodes[random_node]

        return new_nodes[0]

            



        