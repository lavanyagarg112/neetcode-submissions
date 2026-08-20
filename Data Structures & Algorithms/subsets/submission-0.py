class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        curr = nums[0]
        rest = self.subsets(nums[1:])
        result = []
        for r in rest:
            result.append(r)
            result.append([curr] + r)
        
        return result

