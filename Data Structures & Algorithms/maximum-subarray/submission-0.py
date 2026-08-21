class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # greedy means make a locally optimal choice
        # and that gives global optimum

        curr = nums[0]
        maxsum = nums[0]

        left = 0
        right = 1

        while left < right and right < len(nums):

            curr += nums[right]
            maxsum = max(curr, maxsum)
            while curr <= 0 and left < right:
                curr -= nums[left]
                left += 1
            right += 1

        return maxsum


