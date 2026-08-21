class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        sofar = 1
        prev = 1
        maxprod = float("-inf")

        for n in nums:
            sofar *= n
            prev = max(n, prev * n)
            maxprod = max(maxprod, max(prev, sofar))

        return maxprod