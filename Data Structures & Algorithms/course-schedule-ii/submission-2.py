class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # sorting
        # in pair
        # out pair
        # graph

        in_degree = {}
        graph = {}

        for c in range(numCourses):
            in_degree[c] = 0
            graph[c] = set()

        for course, prereq in prerequisites:
            in_degree[course] += 1
            graph[prereq].add(course)

        order = []

        queue = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)
                order.append(c)

        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                course = queue.popleft()
                visited.add(course)
                for nextcourse in graph[course]:
                    in_degree[nextcourse] -= 1
                    if in_degree[nextcourse] == 0:
                        if nextcourse not in visited:
                            queue.append(nextcourse)
                            order.append(nextcourse)

        if len(order) != numCourses:
            return []
            
        return order