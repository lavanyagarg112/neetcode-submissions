class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(len(nums)):
            res = res + i - nums[i]
            # add all numbers
            # remove numbers that are there

        res += len(nums)
        return res

