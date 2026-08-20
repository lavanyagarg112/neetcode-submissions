class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = {}

        for course in range(numCourses):
            adjlist[course] = set()

        for course, prereq in prerequisites:
            adjlist[course].add(prereq)

        def get_next_course():
            next_courses = set()
            for course in adjlist:
                if len(adjlist[course]) == 0:
                    next_courses.add(course)

            if not next_courses:
                return False

            for course in next_courses:
                adjlist.pop(course)
            
            for course in adjlist:
                for rcourse in next_courses:
                    if rcourse in adjlist[course]:
                        adjlist[course].remove(rcourse)
            
            return True

        while adjlist:
            if not get_next_course():
                return False

        return True

        
