class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # greedy means make a locally optimal choice
        # and that gives global optimum

        curr = nums[0]
        maxsum = nums[0]

        left = 0
        right = 1

        while left < right and right < len(nums):

            
            while curr < 0 and left < right:
                curr -= nums[left]
                left += 1

            # i initially had the below line before the loop
            # now i moved it after the loop and it worked??
            # eg: nums = [-2, 3]
            # SEE AGAIN
            curr += nums[right]
            right += 1
            maxsum = max(curr, maxsum)

        return maxsum


