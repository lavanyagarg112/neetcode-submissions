class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = []

        for i in range(m+1):
            temp = []
            for j in range(n+1):
                temp.append(0)
            dp.append(temp)

        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]