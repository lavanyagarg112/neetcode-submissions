class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sum
        n = len(nums)
        return sum(range(0, n + 1)) - sum(nums)