class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        hasStarted = False
        start = None
        i = 0

        while i < len(intervals):
            cstart, cend = intervals[i]
            if hasStarted == True:
                if cend < newInterval[1]:
                    intervals[i] = None
                    i += 1
                    continue
                else:
                    # if its the end
                    intervals[i][0] = start
                    break 

            # if new interval does not start in between
            # but this is interval insertion place
            if cstart > newInterval[1]:
                intervals.insert(i, newInterval)
                break

            # if interval is to be inserted in future
            if cend < newInterval[0]:
                i += 1
                continue
            
            hasStarted = True
            start = min(newInterval[0], cstart)

        while None in intervals:
            intervals.remove(None)

        return intervals




