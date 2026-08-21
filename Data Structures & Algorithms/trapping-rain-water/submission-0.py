class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0

        left = height[0]
        total = 0
        curr_water = 0

        for ind in range(1, len(height)):
            right = height[ind]

            if right >= left:
                total += curr_water
                curr_water = 0
                left = right
            
            else:
                curr_water += (left - right)


        return total

            