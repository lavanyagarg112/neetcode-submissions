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

        if not head:
            return None

        nodes = []
        new_nodes = []
        node_to_pos = {}
        c = 0

        temp = head
        while temp:
            nodes.append(temp)
            new_nodes.append(Node(temp.val))
            node_to_pos[temp] = c
            c += 1
            temp = temp.next
        nodes.append(None)
        new_nodes.append(None)
        node_to_pos[None] = c

        for c in range(len(nodes)-1):
            curr = nodes[c]
            next_node = c + 1
            # random_node = nodes.index(curr.random)
            random_node = node_to_pos[curr.random]
            newcurr = new_nodes[c]
            newcurr.next = new_nodes[next_node]
            newcurr.random = new_nodes[random_node]

        return new_nodes[0]

            



        