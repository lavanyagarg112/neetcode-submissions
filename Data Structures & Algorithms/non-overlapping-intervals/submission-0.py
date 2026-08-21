class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        intervals.sort(key=lambda x:x[0])

        res = 0
        limit = float("-inf")

        for start, end in intervals:
            if start < limit:
                res += 1
                continue
            limit = end


        return res