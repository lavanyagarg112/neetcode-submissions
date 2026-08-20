class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        adjlist = {}

        # assuming the nodes are numbered 0 to n-1
        for i in range(n):
            adjlist[i] = set()

        for n1, n2 in edges:
            adjlist[n1].add(n2)
            adjlist[n2].add(n1)


        def dfs(node):

            stack = [node]

            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue

                visited.add(curr)

                for n1 in adjlist[curr]:
                    stack.append(n1)


        # dfs will count all connected components
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1

        return result




