class Solution:

    def __init__(self):
        self.truelist = []
        self.falselist = []

    def canFindSubset(self, nums, target):
        if (nums, target) in self.truelist:
            return True

        if (nums, target) in self.falselist:
            return False

        if target == 0:
            return True

        if len(nums) == 0:
            return False

        include = self.canFindSubset(nums[1:], target - nums[0])
        exclude = self.canFindSubset(nums[1:], target)

        if include or exclude:
            self.truelist.append((nums, target))
            return True

        self.falselist.append((nums, target))
        return False


    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        # cannot even get equal sum
        if total % 2 == 1:
            return False

        target = total//2

        if self.canFindSubset(nums, target):
            return True

        return False