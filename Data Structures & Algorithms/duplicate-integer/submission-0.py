class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set(nums)
        if len(d) != len(nums):
            return True
        else:
            return False