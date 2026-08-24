class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = {} 

        def is_redundant(first, second):
            graph[first].remove(second)
            graph[second].remove(first)

            res = False
            if can_reach():
                res = True

            # add back
            graph[first].add(second)
            graph[second].add(first)

            print(first, second, res)
            return res
        
        def can_reach():
            visited = set()
            stack = [1] # start with random node

            while stack:
                node = stack.pop()
                visited.add(node)

                for n in graph[node]:
                    if n not in visited:
                        stack.append(n)
            print("visited:", visited)
            print(len(edges)-1)
            return len(visited) == len(edges)



        nodes_repeated = set()
        visited_nodes = set()

        for e in edges:
            first = e[0]
            second = e[1]

            if first in visited_nodes:
                nodes_repeated.add(first)
            if second in visited_nodes:
                nodes_repeated.add(second)
            visited_nodes.add(first)
            visited_nodes.add(second)

            if first not in graph:
                graph[first] = set()
            if second not in graph:
                graph[second] = set()

            graph[first].add(second)
            graph[second].add(first)


        for i in range(len(edges)-1, -1, -1):
            e = edges[i]
            first = e[0]
            second = e[1]
            if first not in nodes_repeated and second not in nodes_repeated:
                continue

            # else consider this edge
            if is_redundant(first, second):
                return e

        return []


