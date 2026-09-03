class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # O(n)
        # go forward
        # keep getting the farthest we can go in current window

        jumps = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest = 0 # right now i cant go anywhere
            for i in range(left, right + 1):
                # see how far i can go in my current window
                farthest = max(farthest, i + nums[i])

            # next window
            left = right + 1
            right = farthest
            jumps += 1
        
        return jumps