class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def helper(target, nums, path):
            if target == 0:
                res.append(path)
                return

            if len(nums) == 0 or target < 0:
                return

            num1 = nums[0]
            # choose
            helper(target - num1, nums, path + [num1])
            # not choose
            helper(target, nums[1:], path)

            return

        helper(target, nums, [])
        return res
        