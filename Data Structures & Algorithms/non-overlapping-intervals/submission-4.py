class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # keep the one which ends earlier
        # greedy approach

        # lol i just got this.. see other solutions
        intervals.sort(key=lambda x: (x[1], x[0]))

        res = 0
        limit = float("-inf")

        for start, end in intervals:
            if start < limit:
                res += 1
                continue
            limit = end


        return res