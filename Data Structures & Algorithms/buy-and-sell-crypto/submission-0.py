class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # no transactions when descending
        # sliding window
        # we want min on left side and max from right side
        # q: how is sliding window diff from two pointers

        if len(prices) < 2:
            return 0

        right = 1
        buy = prices[0]
        sell = prices[0]
        profit = 0

        while right < len(prices):
            buy = min(buy, sell)
            sell = prices[right]
            profit = max(profit, sell - buy)
            right += 1

        return profit

        