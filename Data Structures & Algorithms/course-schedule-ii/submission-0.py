class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # sorting
        # in pair
        # out pair
        # graph

        in_degree = {}

        for c in range(numCourses):
            in_degree[c] = set()

        for course, prereq in prerequisites:
            in_degree[course].add(prereq)

        order = []

        for prereq in in_degree:
            if prereq not in order and len(in_degree[prereq]) == 0:
                order.append(prereq)
                for course in in_degree:
                    if prereq in in_degree[course]:
                        in_degree[course].remove(prereq)


        return order