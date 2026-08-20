class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # with O(1) space

        i = 0

        while i < len(nums):
            curr = nums[i]
            if curr == i + 1:
                i += 1
                continue

            if i == curr - 1:
                i += 1
                continue

            if nums[curr - 1] == curr:
                return curr
            
            # swap
            nums[curr - 1], nums[i] = curr, nums[curr - 1]
            # i += 1

        return nums[-1]