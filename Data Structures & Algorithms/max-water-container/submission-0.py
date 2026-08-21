class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            left = heights[l]
            right = heights[r]
            area = min(left, right) * (r - l)
            maxArea = max(area, maxArea)
            
            if l + 1 < r:
                if heights[l + 1] > heights[r - 1]:
                    l += 1
                else:
                    r -= 1
            else:
                break

        return maxArea
        