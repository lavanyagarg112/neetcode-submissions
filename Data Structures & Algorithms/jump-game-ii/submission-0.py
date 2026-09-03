class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # go backwards
        # go the earliest that can reach that point
        # continue

        if len(nums) == 1:
            return 0

        jumps = 0

        right = len(nums) - 1
        left = right - 1
        sofar = right - 1

        while right != 0:
            if nums[left] >= right - left:
                sofar = left
            if left == 0:
                right = sofar
                jumps += 1
                left = right - 1
            else:
                left -= 1

        return jumps