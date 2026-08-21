class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums) + 1):
            if nums[i] != i:
                return i

        return len(nums)
