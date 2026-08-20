class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prevMax = 1
        prevMin = 1
        sofar = 1
        result = float("-inf")

        for n in nums:
            prevMax, prevMin = max(prevMax * n, max(prevMin * n, n)), min(prevMax * n, min(prevMin * n, n))
            sofar *= n

            result = max(result, max(sofar, prevMax))
        
        return result
            