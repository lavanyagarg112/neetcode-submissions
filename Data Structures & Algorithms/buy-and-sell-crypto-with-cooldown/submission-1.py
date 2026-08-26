class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dp(buyday, today):
            if today >= len(prices):
                return 0

            if (buyday, today) in memo:
                return memo[(buyday, today)]

            ans = dp(buyday, today+1) # do nothing on this day
            if buyday != None:
                ans = max(ans, dp(None, today+2) + (prices[today] - prices[buyday])) # sell today
            else:
                ans = max(ans, dp(today, today+1)) # buy today

            memo[(buyday, today)] = ans

            return ans

        # ans = dp(0, 1) # wrong: we are forcing a buy on day 0
        ans = dp(None, 0)
        return ans