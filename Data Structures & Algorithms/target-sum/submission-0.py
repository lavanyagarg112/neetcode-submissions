class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dp(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            add = dp(i+1, total + nums[i])
            subtract = dp(i+1, total - nums[i])

            ans = add + subtract
            memo[(i, total)] = ans
            
            return ans

        return dp(0, 0)