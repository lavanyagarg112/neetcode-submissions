class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # the last index does not matter
        final = len(nums)-1

        curr = final - 1

        while curr >= 0:
            # check if what it can jump to can jump to min reachable state
            if nums[curr] >= (final - curr):
                final = curr
            else:
                if curr == 0:
                    return False

            curr -= 1

        return True


