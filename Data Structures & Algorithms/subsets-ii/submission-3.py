class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # backtracking
        # if choosing the number, choose it and continue
        # if not choosing, exclude and continue
        # if excluding, exclude all duplicates as well

        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::]) # copy the subsets to result
                return

            subset.append(nums[i]) # single number
            backtrack(i+1, subset) # include number and continue
            subset.pop() # exclude number

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, subset)

        backtrack(0, [])

        return result