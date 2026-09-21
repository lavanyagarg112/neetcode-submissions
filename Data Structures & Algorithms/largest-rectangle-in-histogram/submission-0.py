class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        prev = [(heights[0], 1)] # h, w
        res = heights[0]

        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                for j in range(len(prev)):
                    prev[j] = (prev[j][0], prev[j][1] + 1)
                    area = prev[j][0] * prev[j][1]
                    res = max(res, area)
                prev.append((heights[i], 1))
                res = max(res, heights[i])

            else:
                to_remove = set()
                for j in range(len(prev)):
                    prev[j] = (min(prev[j][0], heights[i]), prev[j][1] + 1)
                    area = prev[j][0] * prev[j][1]
                    res = max(res, area)
                prev.append((heights[i], 1))
                res = max(res, heights[i])

        return res
                


