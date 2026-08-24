class Solution:

    # using index
    # better memoization

    def __init__(self):
        self.memo = {}
        self.nums = []

    def canFindSubset(self, i, target):
        if (i, target) in self.memo:
            return self.memo[(i, target)]

        if target == 0:
            return True

        if i == len(self.nums):
            return False

        include = False
        if self.nums[i] <= target:
            include = self.canFindSubset(i + 1, target - self.nums[i])
        exclude = self.canFindSubset(i + 1, target)

        ans = include or exclude
        self.memo[(i, target)] = ans
        return ans


    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        self.nums = nums

        # cannot even get equal sum
        if total % 2 == 1:
            return False

        target = total//2

        nums = tuple(nums)

        if self.canFindSubset(0, target):
            return True

        return False