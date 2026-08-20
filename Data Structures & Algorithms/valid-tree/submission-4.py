class DSU:

    def __init__(self, n):
        # initialise with n components
        self.comps = n
        self.Parent = list(range(n))
        self.Size = [1] * (n)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False

        self.comps -= 1
        if self.Size[parent_u] < self.Size[parent_v]:
            parent_u, parent_v = parent_v, parent_u

        self.Size[parent_u] += self.Size[parent_v]
        self.Parent[parent_v] = parent_u
        return True

    def components(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dsu !!
        # disjoint set union
        # each node is its own component
        # connect 2 nodes
        # if they were already in same component before means cycle
        # else merge
        # finally a valid tree would have exactly 1 connected component
        # and n nodes tree means atmost n-1 edges

        if len(edges) > n-1:
            return False

        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False

        return dsu.components() == 1