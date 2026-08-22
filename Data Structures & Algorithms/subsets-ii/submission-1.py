class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[nums[0]], []]

        curr = nums[0]
        remaining = self.subsetsWithDup(nums[1:]) # O(n)

        res = set()
        for s in remaining: # O(2^n)
            n = tuple(sorted([curr] + s))
            res.add(n)
            res.add(tuple(s))

        result = [list(s) for s in res]
        return result
        