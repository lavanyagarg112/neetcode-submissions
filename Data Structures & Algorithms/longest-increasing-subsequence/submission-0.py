class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # include or dont include

        memo = {}

        def recurse(prev_max, i, maxsofar):
            if i == len(nums):
                return maxsofar

            ans1 = recurse(prev_max, i+1, maxsofar)
            ans2 = 0
            if nums[i] > prev_max:
                ans2 = recurse(nums[i], i+1, maxsofar+1)

            return max(ans1, ans2)

        return recurse(-1, 0, 0)
        