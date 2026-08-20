class DSU:

    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n+1)) # list of 0 to n inclusive
        self.Size = [1] * (n+1) # size of those nodes
        # if its 0 -> n-1 then can be just range(n)

    def find(self, node):
        if self.Parent[node] != node: # if it is not the root node
            # find the root node and update
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)

        # if they are already in same component, ignore
        if p_u == p_v:
            return

        # merge
        self.comps -= 1

        # merge smaller one into larger one
        if self.Size[p_u] < self.Size[p_v]:
            p_u, p_v = p_v, p_u

        self.Size[p_u] += self.Size[p_v]
        self.Parent[p_v] = p_u

    def components(self):
        return self.comps


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dsu!!!
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)

        return dsu.components()