class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # dp[i][a]: number of ways to form amount a using
        # coins from index i onwards
        # so basically we are focusing on each step: include
        # this coin or not !

        for i in range(n+1):
            dp[i][0] = 1
            # 1 way to make 0 amount

        for i in range(n-1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i+1][a] # skip this coin
                    dp[i][a] += dp[i][a-coins[i]] # include this coin

        return dp[0][amount]


        