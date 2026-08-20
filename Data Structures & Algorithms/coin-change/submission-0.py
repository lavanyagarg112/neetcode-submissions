class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for c in coins:
                if c > amt:
                    continue
                
                if dp[amt-c] == -1:
                    continue

                if dp[amt] == -1:
                    dp[amt] = dp[amt-c] + 1
                else:
                    dp[amt] = min(dp[amt], dp[amt-c] + 1)

        return dp[-1]
                