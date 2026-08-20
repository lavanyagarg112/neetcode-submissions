"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) == 0:
            return False

        prev_end = intervals[0].end
        indices_to_pop = [0]

        for i in range(1, len(intervals)):
            if intervals[i].start < prev_end:
                continue
            prev_end = intervals[i].end
            indices_to_pop.append(i)

        for i in range(len(indices_to_pop)):
            intervals.pop(indices_to_pop[i] - i)

        return True

    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)
        ans = 0

        while self.canAttendMeetings(intervals):
            ans += 1

        return ans
        