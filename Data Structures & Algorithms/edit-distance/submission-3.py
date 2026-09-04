class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo: # this could also just use index
                return memo[(i, j)]
            
            if i == len(word1) and j == len(word2):
                return 0

            if i >= len(word1):
                return len(word2) - j # add remaining chars

            if j >= len(word2):
                return len(word1) - i # delete remaining chars

            curr1 = word1[i]
            curr2 = word2[j]

            if curr1 == curr2:
                ans = dp(i + 1, j + 1)
            else:
                replace = 1 + dp(i + 1, j + 1)
                delete = 1 + dp(i + 1, j)
                add = 1 + dp(i, j + 1)
                ans = min(replace, min(delete, add))

            memo[(i, j)] = ans
            return ans

        return dp(0, 0)

        