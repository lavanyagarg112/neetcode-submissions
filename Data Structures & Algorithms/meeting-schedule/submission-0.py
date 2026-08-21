"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()

        if len(intervals) == 0:
            return True

        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prev_end:
                return False
            prev_end = intervals[i].end

        return True
