class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []

        curr = nums[0]

        if len(nums) == 1:
            return [[curr]]

        next_perm = self.permute(nums[1:])

        result = []
        possible_pos = len(next_perm[0]) + 1

        for perm in next_perm:
            for i in range(possible_pos):
                new_perm = perm[:i] + [curr] + perm[i:]
                result.append(new_perm)
        
        return result
            