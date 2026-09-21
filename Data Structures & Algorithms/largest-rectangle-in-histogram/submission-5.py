class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # time: O(n^2)
        # space: O(n)

        prev = {}
        prev[heights[0]] = 1 # h, w
        # for each height, we just need greatest width
        res = heights[0]

        for i in range(1, len(heights)):
            new_prev = {}
            for h in prev:
                w = prev[h]
                nh = min(h, heights[i])
                nw = w + 1
                area = nh * nw
                res = max(res, area)
                if nh not in new_prev:
                    new_prev[nh] = nw
                else:
                    new_prev[nh] = max(new_prev[nh], nw)

            if heights[i] not in new_prev:
                new_prev[heights[i]] = 1
            res = max(res, heights[i])
            prev = new_prev

        return res
                


