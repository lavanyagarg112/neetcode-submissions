class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # see again!!
        # i had to see the ans to get this
        # see other methods as well
        
        dp = [1] * len(nums) # basically length of longest at that index

        for start in range(len(nums)-1, -1, -1):
            for end in range(start + 1, len(nums)):
                if nums[start] < nums[end]:
                    # add 1 + whatever the lis is at that num
                    dp[start] = max(dp[start], 1 + dp[end])
        
        return max(dp)