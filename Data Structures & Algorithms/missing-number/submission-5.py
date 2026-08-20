class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = 0
        maxnum = len(nums) + 1
        for i in range(maxnum):
            res = res ^ i

        # the numbers that are there will get xored out
        # A xor A = 0
        for i in nums:
            res = res ^ i

        return res

        