class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev = 1
        maxprod = float('-inf')

        for n in nums:
            maxprod = max(maxprod, max(n, prev * n))
            prev = prev * n

        return maxprod
