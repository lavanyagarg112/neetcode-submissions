"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = {}

        def dfs(node):
            if not node:
                return None
            
            clonedGraph = Node(node.val)
            neighbs = []

            visited[node.val] = clonedGraph

            for n in node.neighbors:
                if n.val in visited:
                    neighbs.append(visited[n.val])
                else:
                    neighbs.append(dfs(n))

            clonedGraph.neighbors = neighbs
            return clonedGraph

        return dfs(node)