class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        def recurs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i,j)]

            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + recurs(i+1, j+1)
            else:
                ans = max(recurs(i+1, j), recurs(i, j+1))
            memo[(i, j)] = ans
            return ans

        res = recurs(0, 0)
        return res