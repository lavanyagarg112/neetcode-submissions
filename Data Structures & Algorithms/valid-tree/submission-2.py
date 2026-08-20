class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles
        # exactly n-1 edges

        if len(edges) != n-1:
            return False
        
        if n == 1:
            return True

        adjlist = {}

        for n1, n2 in edges:
            if n1 not in adjlist:
                adjlist[n1] = set()
            if n2 not in adjlist:
                adjlist[n2] = set()

            adjlist[n1].add(n2)
            adjlist[n2].add(n1)

        # an edge is missing
        for i in range(n):
            if i not in adjlist:
                return False

        # check if all are one connected component
        visited = set()
        stack = [0]

        while stack:
            curr = stack.pop()

            if curr in visited:
                continue

            visited.add(curr)

            for n1 in adjlist[curr]:
                stack.append(n1)

        if len(visited) != n:
            return False

        return True