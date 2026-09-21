class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # time limit exceed

        prev = set() 
        prev.add((heights[0], 1)) # h, w
        res = heights[0]

        for i in range(1, len(heights)):
            new_prev = set()
            for h, w in prev:
                nh = min(h, heights[i])
                nw = w + 1
                area = nh * nw
                res = max(res, area)
                new_prev.add((nh, nw))
            new_prev.add((heights[i], 1))
            res = max(res, heights[i])
            prev = new_prev

        return res
                


