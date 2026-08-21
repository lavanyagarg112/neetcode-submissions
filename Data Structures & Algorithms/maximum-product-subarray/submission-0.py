class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev = 1
        maxprod = float('-inf')

        for n in nums:
            prev = max(n, prev * n)
            maxprod = max(maxprod, prev)
            
        return maxprod
