class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            left = heights[l]
            right = heights[r]
            area = min(left, right) * (r - l)
            print(left, right, area)
            maxArea = max(area, maxArea)

            if left < right:
                l += 1
            else:
                r -= 1


        return maxArea
        