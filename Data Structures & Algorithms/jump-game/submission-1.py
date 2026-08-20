class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # the last index does not matter
        final = len(nums)-1

        # consider if only length 1
        if len(nums) == 1:
            return True

        curr = final - 1
        canLand = [False] * len(nums)
        canLand[-1] = True

        while curr >= 0:
            # check if what it can jump to can jump to min reachable state
            if nums[curr] >= (final - curr):
                canLand[curr] = True
                final = curr
            else:
                canLand[curr] = False

            curr -= 1

        return canLand[0]


