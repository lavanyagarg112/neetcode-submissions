class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # the last index does not matter
        final = len(nums)-1

        # consider if only length 1
        if len(nums) == 1:
            return True

        curr = final - 1
        canLand = [False] * (len(nums))
        canLand[final] = True

        while curr >= 0:
            # check if what it can jump to can jump to last
            if canLand[min(curr + nums[curr], final)]:
                canLand[curr] = True
            else:
                canLand[curr] = False

            curr -= 1

        return canLand[0]


