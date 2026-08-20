class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            # check if ith bit is 1 + the dp for remaining
            dp[i] = dp[i >> 1] + (i & 1)
        return dp