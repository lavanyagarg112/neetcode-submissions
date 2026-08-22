class Solution:
    def deduplicate(self, subsets):
        
        def create_freqmap(nums):
            d = {}
            for i in nums:
                if i not in d:
                    d[i] = 0
                d[i] += 1

            return d

        visited = []
        result = []

        for s in subsets:
            numsfreq = create_freqmap(s)
            if numsfreq not in visited:
                result.append(s)
                visited.append(numsfreq)

        return result


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[nums[0]], []]

        curr = nums[0]
        remaining = self.subsetsWithDup(nums[1:]) # O(n)

        newsets = []
        for s in remaining: # O(2^n)
            newsets.append([curr] + s)

        result = self.deduplicate(newsets + remaining)
        return result
        