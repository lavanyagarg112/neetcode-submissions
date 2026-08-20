class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        result = []

        for start, end in intervals:
            if len(result) == 0:
                result.append([start, end])
                continue
            
            pstart, pend = result[-1]

            if start <= pend:
                result[-1][1] = max(pend, end)
            else:
                result.append([start, end])

        return result