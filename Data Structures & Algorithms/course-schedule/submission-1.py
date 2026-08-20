class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = {}
        adjlist = {}

        q = deque()

        for c in range(numCourses):
            indegree[c] = 0
            adjlist[c] = set()

        for course, prereq in prerequisites:
            indegree[course] += 1
            adjlist[prereq].add(course)

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        result = 0

        while q:
            course = q.popleft()
            result += 1
            for c in adjlist[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)


        return result == numCourses

        