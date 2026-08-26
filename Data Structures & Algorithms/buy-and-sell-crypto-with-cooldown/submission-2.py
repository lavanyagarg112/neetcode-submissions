class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # top down -> second approach
        
        memo = {}

        def dp(canBuy, today):
            if today >= len(prices):
                return 0

            if (canBuy, today) in memo:
                return memo[(canBuy, today)]

            ans = dp(canBuy, today+1) # do nothing on this day
            if not canBuy:
                ans = max(ans, dp(True, today+2) + prices[today]) # sell today
            else:
                ans = max(ans, dp(False, today+1) - prices[today]) # buy today

            memo[(canBuy, today)] = ans

            return ans

        ans = dp(True, 0)
        return ans